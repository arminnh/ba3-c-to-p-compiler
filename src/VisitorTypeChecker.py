from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *
import re
import sys


class VisitorTypeChecker(Visitor):
    def __init__(self, errorHandler):
        super(VisitorTypeChecker, self).__init__(errorHandler)

        self.stdioCodes = {
            # types are rvalues
            'd' : TypeInfo(rvalue=True, basetype="int"),
            'i' : TypeInfo(rvalue=True, basetype="int"),
            'f' : TypeInfo(rvalue=True, basetype="float"),
            'c' : TypeInfo(rvalue=True, basetype="char"),
            's' : TypeInfo(rvalue=True, basetype="char", indirections=[(False, False), (False, False)])
        }


    def visitIncludeNode(self, node):
        pass


    def visitReturnNode(self, node):
        if self.visitChildren(node) == "error":
            return

        functionDefinition = node

        while functionDefinition is not None and not isinstance(functionDefinition, ASTFunctionDefinitionNode):
            functionDefinition = functionDefinition.parent

        if not node.children:
            if functionDefinition.getType().basetype != "void" or functionDefinition.getType().nrIndirections() != 0:
                self.addWarning("'return' with no value, in function returning non-void", node)
            return

        if not functionDefinition.getType().isCompatible(node.children[0].getType(), ignoreRvalue=True):
            if functionDefinition.getType().isCompatible(TypeInfo(rvalue=True, basetype="void", indirections=[(False, False)]), ignoreRvalue=True):
                self.addWarning("'return' with a value, in function returning void", node)
            else:
                self.addError("incompatible conversion returning '{0}' from a function with return type '{1}'".format(node.children[0].getType(), functionDefinition.getType()), node)


    # int a[myFun(5)] = {1, 2+"a", 3}
    def visitDeclaratorInitializerNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.getType().isCompatible(TypeInfo(rvalue=True, basetype="void", indirections=[(False, False)])):
            self.addError("variable or field '{0}' declared void".format(node.identifier), node)

        for child in node.children:
            # if child is expression node, it is the array length value
            if isinstance(child, ASTExpressionNode):
                arrayLengthExpression = True
                if not child.getType().isCompatible(TypeInfo(basetype="int", rvalue=True)):
                    self.addError("size of array '{0}' has non-integer type (have '{1}')".format(node.identifier, str(child.getType())), node)
                    continue

            elif isinstance(child, ASTInitializerListNode):
                # if basetype is array, typecheck with each elements of initializer list
                if node.getType().isArray():
                    for initListElement in child.children:
                        # get basetype for typechecking with initializer list elements, example: int a[] = {1, 2, 3, 4};
                        ownType = copy.deepcopy(node.getType())
                        if not isinstance(initListElement, ASTStringLiteralNode):
                            ownType.indirections.pop()
                        t2 = initListElement.getType().toRvalue()

                        #  char a[] = "uitzondering";
                        if isinstance(child.children[0], ASTStringLiteralNode) and node.getType().equals(TypeInfo(basetype="char", indirections=[(False, False), (True, False)], rvalue=False)):
                            continue

                        if t2.isCompatible(TypeInfo(rvalue=True, basetype="void", indirections=[(False, False)]), ignoreRvalue=True):
                            self.addError("void value not ignored as it ought to be", node)
                            continue
                        elif not ownType.isCompatible(t2, ignoreRvalue=True):
                            self.addError("incompatible types when initializing type '{0}' using type '{1}'".format(ownType, t2), node)
                            continue

                        if not ownType.isConstCompatible(t2):
                            # this is a warning in c, but an error in c++
                            self.addWarning("initialization discards 'const' qualifier, expected '{0}' but got '{1}'".format(ownType, t2), node)
                            continue

                #typecheck with only 1st element of initializer list, example: int a = {1, 2.0, "aaa", 'a'} is ok
                else:
                    # if initializer list does not have any children (int a = {}), error
                    if not child.children:
                        self.addError("empty scalar initializer", node)
                        continue

                    t1 = node.getType().toRvalue()
                    t2 = child.children[0].getType().toRvalue()

                    if t2.isCompatible(TypeInfo(rvalue=True, basetype="void", indirections=[(False, False)]), ignoreRvalue=True):
                        self.addError("void value not ignored as it ought to be", node)
                        continue
                    # only 1st element matters, if multiple initialization elements: warning: excess elements in scalar initializer
                    elif not t1.isCompatible(t2, ignoreRvalue=True):
                        self.addError("incompatible types when initializing type '{0}' using type '{1}'".format(t1, t2), node)
                        continue

                    if not t1.isConstCompatible(t2):
                        self.addWarning("initialization discards 'const' qualifier, expected '{0}' but got '{1}'".format(t1, t2), node)

                    if len(child.children) > 1:
                        line, column = node.getLineAndColumn()
                        self.errorHandler.addWarning("excess elements in scalar initializer", line, column)

        # TODO: adapt for multidimensional arrays
        # possibility: count in indirections array the amount of arrays from right to left, up until the first non-array
        #              these are the arrays that need an array length specifier
        if not node.children and node.getType().isArray():
            self.addError("array size missing in '{0}'".format(node.identifier), node)
            return


    def visitIntegerLiteralNode(self, node):
        pass


    def visitFloatLiteralNode(self, node):
        pass


    def visitCharacterLiteralNode(self, node):
        pass


    def visitStringLiteralNode(self, node):
        pass


    def visitVariableNode(self, node):
        pass


    # the format string allows interpretation of sequences of the form %[width][code] (width only in case of output).
    # Provide support for at least for the type codes d(int), i(int), s(char *) and c(char), f(float). You may consider the char* types to be char arrays.
    def checkStdioFunction(self, node):
        arguments = None
        for child in node.children:
            if isinstance(child, ASTArgumentsNode):
                arguments = child
                break

        if arguments is None:
            raise Exception("Did not find arguments node in ASTFunctionCallNode")

        # take first argument of scanf/printf function
        formatArgument = arguments.children[0]

        # first argument should be of string rvalue type
        if type(formatArgument) is not ASTStringLiteralNode:
            self.addError("argument 1 of function '{0}' should be a string literal".format(node.identifier), node)
            return

        # get the text of the first argument (the format argument) and get the format codes out of it
        format = formatArgument.value
        formatSpecifiers = re.finditer(r'%([0-9]*)([a-z%])', format)

        # print (codes, len(arguments.children))
        endOfLastMatch = 0
        cutIntoPieces = []
        codesCount = 0
        if formatSpecifiers:
            for i, match in enumerate(formatSpecifiers):
                cutIntoPieces.append(format[endOfLastMatch:match.start()])
                width, code = match.groups()
                codesCount += 1

                if code == "%":
                    continue

                if code not in self.stdioCodes:
                    self.addWarning("unknown format code '{0}'".format(code), node)
                    continue

                if i + 1 >= len(arguments.children): #ex: printf("%i %i", 1)
                    self.addWarning("format '%{0}' expects a matching '{1}' argument".format(code, str(self.stdioCodes[code])), node)
                    continue
                else:
                    t1 = self.stdioCodes[code]
                    t2 = arguments.children[i+1].getType().toRvalue()
                    if not t1.isCompatible(t2):
                        self.addError("format '{0}' expects argument of type '{1}', but argument {2} has type '{3}'".format(code, t1, i+2, t2), node)

                cutIntoPieces.append((width, arguments.children[i + 1]))
                endOfLastMatch = match.end()

        cutIntoPieces.append(format[endOfLastMatch:])
        node.parsedFormat = cutIntoPieces

        if codesCount < len(arguments.children) - 1:
            self.addWarning("too many arguments for format", node)

    # TODO: prevent function call with void return type from appearing in a subexpression
    def visitFunctionCallNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.identifier in ["printf", "scanf"] and node.definitionNode.isStdioFunction:
            return self.checkStdioFunction(node)

        arguments = None
        for child in node.children:
            if isinstance(child, ASTArgumentsNode):
                arguments = child
                break

        parameterNodes = node.definitionNode.getParameters().children
        if arguments is not None:
            if len(arguments.children) != len(parameterNodes):
                self.addError("number of arguments to function '{0}' does not match definition (have {1}, need {2})".format(node.identifier, len(arguments.children), len(parameterNodes)), node)
                return

            for i, argument in enumerate(arguments.children):
                if argument.error:
                    continue
                t1 = parameterNodes[i].getType().toRvalue()
                t2 = argument.getType().toRvalue()
                if not t1.isCompatible(t2, ignoreRvalue=True):
                    node.errorParameter = i
                    self.addError("parameter {2} of '{3}' expected '{0}' but got '{1}'".format(t1, t2, i+1, node.identifier), node)
                    continue

                if not t1.isConstCompatible(t2):
                    self.addWarning("passing argument {2} of '{3}' discards 'const' qualifier, expected '{0}' but got '{1}' ".format(t1, t2, i+1, node.identifier), node)
                    continue

        else:
            raise Exception("Did not find arguments node in ASTFunctionCallNode")


    def typeCheckBinaryOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if not node.children[0].getType().toRvalue().isCompatible(node.children[1].getType().toRvalue()):
            self.addError("invalid operands to binary '{2}' (have '{0}' and '{1}')".format(str(node.children[0].getType()), str(node.children[1].getType()), node.label), node)
            return


    def visitTernaryConditionalOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if not node.children[0].getType().toRvalue().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            node.errorOperand = 0
            self.addError("invalid first operand to ternary '?:' (have '{0}', need 'int')".format(node.children[0].getType()), node)
            return

        if node.children[1].getType() != node.children[2].getType():
            node.errorOperand = 1
            self.addError("invalid operands to ternary '?:', alternatives should be of equal type (have '{0}' and '{1}')".format(node.children[1].getType(), node.children[2].getType()), node)
            return


    def visitSimpleAssignmentOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.children[0].getType().rvalue:
            #TODO: test this
            self.addError("expression is not assignable", node)
            return

        t1 = node.children[0].getType()
        t2 = node.children[1].getType().toRvalue()

        if not t1.isCompatible(t2):
            self.addError("incompatible types when assigning to type '{0}' from type '{1}'".format(str(t1), str(t2)), node)
            return

        if t1.isConst():
            if isinstance(node.children[0], ASTVariableNode):
                self.addError("assignment of read-only variable '{0}'".format(node.children[0].identifier), node)
            elif isinstance(node.children[0], (ASTArraySubscriptNode, ASTDereferenceOperatorNode)):
                self.addError("assignment of read-only location '{0}'".format(node.children[0].ctx.getText()), node)
            else:
                self.addError("assignment of read-only variable", node)
            return

        if not t1.isConstCompatible(t2):
            self.addError("assigning to '{0}' from '{1}' discards 'const' qualifier".format(t1, t2), node)


    def visitLogicOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.children[0].getType().toRvalue() != node.children[1].getType().toRvalue():
            self.addError("invalid operands to logical '{2}' (have '{0}' and '{1}')".format(str(node.children[0].getType()), str(node.children[1].getType()), str(node.logicOperatorType)), node)
            return

        if not node.children[0].getType().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            self.addError("invalid operands to logical '{2}' (have '{0}' and '{1}', need 'int' and 'int')".format(str(node.children[0].getType()), str(node.children[1].getType()), str(node.logicOperatorType)), node)
            return


    def visitComparisonOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if not node.children[0].getType().isCompatible(node.children[1].getType(), ignoreRvalue=True):
            self.addError("invalid operands to comparison '{2}' (have '{0}' and '{1}')".format(str(node.children[0].getType()), str(node.children[1].getType()), str(node.comparisonType)), node)
            return


    def visitUnaryArithmeticOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.children[0].getType().rvalue and (node.arithmeticType is ASTUnaryArithmeticOperatorNode.ArithmeticType['increment'] or node.arithmeticType is ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']):
            self.addError("lvalue required as {0} operand".format(node.arithmeticType.wordStr()), node)
            return False


    def visitAddressOfoperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.children[0].getType().rvalue:
            #TODO: test this
            self.addError("cannot take the address of an rvalue of type '{0}'".format(str(node.children[0].getType())), node)
            return


    def visitDereferenceNode(self, node):
        if self.visitChildren(node) == "error":
            return

        ttype = node.getType()
        if ttype.nrIndirections() < 0:
            self.addError("invalid type argument of unary '*' (have '{0}')".format(str(ttype)), node)
            return


    def visitLogicalNotOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if not node.children[0].getType().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            self.addError("invalid operands to logical '!' (have '{0}', need 'int')".format(node.children[0].getType()), node)
            return


    def visitArraySubscriptNode(self, node):
        self.typeCheckUnaryOperatorNode(node)


    def visitBinaryArithmeticNode(self, node):
        self.typeCheckBinaryOperatorNode(node)
