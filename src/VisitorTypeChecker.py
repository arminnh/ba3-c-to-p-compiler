from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *
import re
import sys


class VisitorTypeChecker(Visitor):
    def __init__(self, errorHandler):
        super(VisitorTypeChecker, self).__init__(errorHandler)

        self.stdioCodes = {
            'd' : TypeInfo(rvalue=True, basetype="int"),
            'i' : TypeInfo(rvalue=True, basetype="int"),
            'f' : TypeInfo(rvalue=True, basetype="float"),
            'c' : TypeInfo(rvalue=True, basetype="char"),
            's' : TypeInfo(rvalue=True, basetype="char", indirections=1, const=[False], isArray=True)
        }


    def visitIncludeNode(self, node):
        pass


    def visitReturnNode(self, node):
        functionDefinition = node

        while functionDefinition is not None and not isinstance(functionDefinition, ASTFunctionDefinitionNode):
            functionDefinition = functionDefinition.parent

        if functionDefinition is None:
            #TODO: test this
            self.addError("return statement outside of function definition", node)
            return

        if not node.children:
            return

        if not functionDefinition.getType().isCompatible(node.children[0].getType(), ignoreRvalue=True):
            #TODO: warning: ‘return’ with a value, in function returning void [enabled by default]
            self.addError("incompatible conversion returning '{0}' from a function with return type '{1}'".format(node.children[0].getType(), functionDefinition.getType()), node)


    # int a[myFun(5)] = {1, 2+"a", 3}
    def visitDeclaratorInitializerNode(self, node):
        if self.visitChildren(node) == "error":
            return

        for child in node.children:
            # if child is expression node, it is the array length value
            if isinstance(child, ASTExpressionNode):
                arrayLengthExpression = True
                if not child.getType().isCompatible(TypeInfo(basetype="int", rvalue=True), ignoreConst=True):
                    #TODO: test this
                    self.addError("array length type must be compatible with 'int' (have '{0}')".format(str(child.getType())), node)
                    continue

            elif isinstance(child, ASTInitializerListNode):
                # if basetype is array, typecheck with each elements of initializer list
                if node.isArray:
                    for initListElement in child.children:
                        # get basetype for typechecking with initializer list elements, example: int a[] = {1, 2, 3, 4};
                        ownType = copy.deepcopy(node.getType())
                        if not isinstance(initListElement, ASTStringLiteralNode):
                            ownType.isArray = False
                            ownType.indirections -= 1

                        if not ownType.isCompatible(initListElement.getType(), ignoreRvalue=True, ignoreConst=True):
                            self.addError("incompatible types when initializing type '{0}' using type '{1}'".format(str(ownType), str(initListElement.getType())), node)
                            continue

                #typecheck with only 1st element of initializer list, example: int a = {1, 2.0, "aaa", 'a'} is ok
                else:
                    # if initializer list does not have any children (int a = {}), error
                    if not child.children:
                        self.addError("empty scalar initializer", node)
                        continue

                    # only 1st element matters, if multiple initialization elements: warning: excess elements in scalar initializer [enabled by default]
                    if not node.getType().isCompatible(child.children[0].getType(), ignoreRvalue=True, ignoreConst=True):
                        self.addError("incompatible types when initializing type '{0}' using type '{1}'".format(str(node.getType()), str(child.children[0].getType())), node)
                        continue

                    # if len(child.children) > 1:
                    #     line, column = node.getLineAndColumn()
                    #     self.errorHandler.addWarning("excess elements in scalar initializer", line, column)

        if not node.children and node.isArray:
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

        formatArgument = arguments.children[0]
        stringLiteralType = TypeInfo(rvalue=True, basetype="char", indirections=1, const=[False], isArray=True)

        if not formatArgument.getType().isCompatible(stringLiteralType):
            #TODO: test this
            self.addError("argument 1 of function '{0}' should be of type '{1}' but is of type '{2}'".format(node.identifier, str(stringLiteralType), str(formatArgument.getType())), node)

        codes = re.findall(r'%([0-9]*)([a-z%])', formatArgument.value)

        if len(codes) < len(arguments.children) - 1:
            # print("warning: too many arguments for format")
            pass

        # print (codes, len(arguments.children))
        for i, (width, code) in enumerate(codes):
            if i+1 > len(arguments.children): #ex: printf("%i %i", 1)
                # print("warning: format ‘%i’ expects a matching ‘int’ argument")
                continue

            if code == "%":
                continue

            if code not in self.stdioCodes:
                #TODO: test this
                self.addError("unknown format code '{0}'".format(code), node)

            elif not self.stdioCodes[code].isCompatible(arguments.children[i+1].getType(), ignoreConst=True):
                self.addError("format '{0}' expects argument of type '{1}', but argument {3} has type '{2}'".format(code, self.stdioCodes[code], arguments.children[i+1].getType(), i+2), node)

        # print (codes)

    #TODO for extras: check constness of arguments/parameters
    def visitFunctionCallNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.identifier in ["printf", "scanf"]:
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
                if not argument.getType().isCompatible(parameterNodes[i].getType(), ignoreRvalue=True, ignoreConst=True):
                    node.errorParameter = i
                    self.addError("expected '{0}' but argument is of type '{1}'".format(str(parameterNodes[i].getType()), str(argument.getType())), node)
                    return
        else:
            raise Exception("Did not find arguments node in ASTFunctionCallNode")


    def typeCheckBinaryOperatorNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if not node.children[0].getType().toRvalue().isCompatible(node.children[1].getType().toRvalue(), ignoreConst=True):
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

        if not node.children[0].getType().toRvalue().isCompatible(node.children[1].getType().toRvalue(), ignoreConst=True):
            self.addError("incompatible types when assigning to type '{0}' from type '{1}'".format(str(node.children[0].getType()), str(node.children[1].getType())), node)
            return


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

        if not node.children[0].getType().equals(node.children[1].getType(), ignoreRvalue=True, ignoreConst=True):
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
        if ttype.indirections < 0:
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
