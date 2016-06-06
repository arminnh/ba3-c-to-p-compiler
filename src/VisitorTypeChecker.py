from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *
from TypeInfo import types
import re
import sys


class VisitorTypeChecker(Visitor):
    def __init__(self, errorHandler):
        super(VisitorTypeChecker, self).__init__(errorHandler)

        self.stdioCodes = {
            # types are rvalues
            'd' : types["int"].toRvalue(),
            'i' : types["int"].toRvalue(),
            'f' : types["float"].toRvalue(),
            'c' : types["char"].toRvalue(),
            's' : types["string"].toRvalue()
        }


    def visitIncludeNode(self, node):
        pass


    def visitReturnNode(self, node):
        if self.visitChildren(node) == "error":
            return

        functionDefinition = node

        while functionDefinition is not None and not isinstance(functionDefinition, ASTFunctionDefinitionNode):
            functionDefinition = functionDefinition.parent

        funDefType = functionDefinition.getType()

        if not node.children:
            if funDefType.basetype != "void" or funDefType.nrIndirections() != 0:
                self.addWarning("'return' with no value, in function returning non-void", node)
            return

        returnType = node.children[0].getType().toRvalue()
        if not funDefType.isCompatible(returnType):
            if funDefType.isCompatible(types["void"].toRvalue()):
                self.addWarning("'return' with a value, in function returning void", node)
            else:
                self.addError("incompatible conversion returning '{0}' from a function with return type '{1}'".format(returnType, funDefType), node)


    # int a[myFun(5)] = {1, 2+"a", 3}
    def visitDeclaratorInitializerNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.getType().isCompatible(types["void"].toRvalue()):
            self.addError("variable or field '{0}' declared void".format(node.identifier), node)

        for child in node.children:
            # if child is expression node, it is the array length value
            if isinstance(child, ASTExpressionNode):
                arrayLengthType = child.getType().toRvalue()
                if not arrayLengthType.isCompatible(types["int"].toRvalue()):
                    self.addError("size of array '{0}' has non-integer type (have '{1}')".format(node.identifier, str(arrayLengthType)), node)
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
                        if isinstance(child.children[0], ASTStringLiteralNode) and node.getType().equals(types["string"]):
                            continue

                        if t2.isCompatible(types["void"].toRvalue()):
                            self.addError("void value not ignored as it ought to be", node)
                            continue
                        elif not ownType.isCompatible(t2):
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

                    if t2.isCompatible(types["void"].toRvalue()):
                        self.addError("void value not ignored as it ought to be", node)
                        continue
                    # only 1st element matters, if multiple initialization elements: warning: excess elements in scalar initializer
                    elif not t1.isCompatible(t2):
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
                if not t1.isCompatible(t2):
                    node.errorParameter = i
                    self.addError("parameter {2} of '{3}' expected '{0}' but got '{1}'".format(t1, t2, i+1, node.identifier), node)
                    continue

                if not t1.isConstCompatible(t2):
                    self.addWarning("passing argument {2} of '{3}' discards 'const' qualifier, expected '{0}' but got '{1}' ".format(t1, t2, i+1, node.identifier), node)
                    continue

        else:
            raise Exception("Did not find arguments node in ASTFunctionCallNode")


    def hasVoidType(self, typeList, node):
        for ttype in typeList:
            if ttype.isCompatible(types["void"].toRvalue()):
                self.addError("void value not ignored as it ought to be", node)
                return True
        return False


    def visitTernaryConditionalOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        t1 = node.children[0].getType().toRvalue()
        t2 = node.children[1].getType().toRvalue()
        t3 = node.children[2].getType().toRvalue()

        if self.hasVoidType([t1, t2, t3], node):
            return

        if not t1.isCompatible(types["int"].toRvalue()):
            node.errorOperand = 0
            self.addError("invalid first operand to ternary '?:' (have '{0}', need 'int')".format(t1), node)
            return

        if t2 != t3 :
            node.errorOperand = 1
            self.addError("invalid operands to ternary '?:', alternatives should be of equal type (have '{0}' and '{1}')".format(t2, t3), node)
            return


    def visitBinaryArithmeticNode(self, node):
        if self.visitChildren(node) == "error":
            return

        t1 = node.children[0].getType().toRvalue()
        t2 = node.children[1].getType().toRvalue()

        if self.hasVoidType([t1, t2], node):
            return

        if not t1.isCompatible(t2):
            self.addError("invalid operands to binary '{2}' (have '{0}' and '{1}')".format(str(t1), str(t2), node.label), node)
            return


    def visitSimpleAssignmentOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        t1 = node.children[0].getType()
        t2 = node.children[1].getType().toRvalue()

        if t1.rvalue:
            self.addError("lvalue required as left operand of assignment", node)
            return

        if self.hasVoidType([t1, t2], node):
            return

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

        t1 = node.children[0].getType().toRvalue()
        t2 = node.children[1].getType().toRvalue()

        if self.hasVoidType([t1, t2], node):
            return

        if t1 != t2:
            self.addError("invalid operands to logical '{2}' (have '{0}' and '{1}')".format(str(t1), str(t2), str(node.logicOperatorType)), node)
            return

        if not t1.isCompatible(types["int"].toRvalue()) or not t2.isCompatible(types["int"].toRvalue()):
            self.addError("invalid operands to logical '{2}' (have '{0}' and '{1}', need 'int' and 'int')".format(str(t1), str(t2), str(node.logicOperatorType)), node)
            return


    def visitComparisonOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        t1 = node.children[0].getType().toRvalue()
        t2 = node.children[1].getType().toRvalue()

        if self.hasVoidType([t1, t2], node):
            return

        if not t1.isCompatible(t2):
            self.addError("invalid operands to comparison '{2}' (have '{0}' and '{1}')".format(str(t1), str(t2), str(node.comparisonType)), node)
            return


    def visitUnaryArithmeticOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        ttype = node.children[0].getType()

        if ttype.isCompatible(types["void"].toRvalue()):
            self.addError("invalid use of void expression", node)
            return

        if ttype.rvalue and (node.arithmeticType is ASTUnaryArithmeticOperatorNode.ArithmeticType["increment"] or node.arithmeticType is ASTUnaryArithmeticOperatorNode.ArithmeticType["decrement"]):
            self.addError("lvalue required as {0} operand".format(node.arithmeticType.wordStr()), node)
            return False


    def visitAddressOfoperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        ttype = node.children[0].getType()

        if ttype.isCompatible(types["void"].toRvalue()):
            self.addWarning("taking address of expression of type ‘void’", node)

        if ttype.rvalue:
            self.addError("lvalue required as unary '&' operand, (got rvalue of type '{0}')".format(str(ttype)), node)
            return


    def visitDereferenceNode(self, node):
        if self.visitChildren(node) == "error":
            return

        ttype = node.children[0].getType()

        if ttype.isCompatible(types["void"].toRvalue()):
            self.addError("void value not ignored as it ought to be", node)
            return

        if ttype.nrIndirections() <= 0:
            self.addError("invalid type argument of unary '*' (have '{0}')".format(str(ttype)), node)
            return


    def visitLogicalNotOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        ttype = node.children[0].getType().toRvalue()

        if ttype.isCompatible(types["void"].toRvalue()):
            self.addError("invalid use of void expression", node)
            return

        if not ttype.isCompatible(types["int"].toRvalue()):
            self.addError("invalid operand to logical '!' (have '{0}', need 'int')".format(ttype), node)
            return


    def visitArraySubscriptNode(self, node):
        if self.visitChildren(node) == "error":
            return

        ttype = node.children[0].getType()

        if ttype.nrIndirections() == 0 and not ttype.isArray():
            self.addError("subscripted value is neither array nor pointer nor vector", node)
            return
