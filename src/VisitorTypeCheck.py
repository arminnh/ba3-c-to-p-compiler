from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorTypeCheck(Visitor):
    def __init__(self, errorHandler):
        self.errorHandler = errorHandler


    def visitIncludeNode(self, node):
        pass


    def visitReturnNode(self, node):
        functionDefinition = node

        while functionDefinition is not None and not isinstance(functionDefinition, ASTFunctionDefinitionNode):
            functionDefinition = functionDefinition.parent

        if functionDefinition is None:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Return statement outside of function definition", line, column) # this should never happen: grammar prevents it
            return

        if not functionDefinition.getType().isCompatible(node.children[0].getType(), ignoreRvalue=True):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Incompatible conversion returning '{0}' from a function with result type '{1}'".format(node.children[0].getType(), functionDefinition.getType()), line, column)


    # int a[myFun(5)] = {1, 2+"a", 3}
    def visitDeclaratorInitializerNode(self, node):
        self.visitChildren(node)

        for child in node.children:
            # if child is expression node, it is the array length value
            if isinstance(child, ASTExpressionNode):
                if not child.getType().isCompatible(TypeInfo(basetype="int", rvalue=True), ignoreConst=True):
                    line, column = node.getLineAndColumn()
                    node.error = True
                    self.errorHandler.addError("Array length type must be compatible with int (have {0})".format(str(child.getType())), line, column)
                    return

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
                            line, column = node.getLineAndColumn()
                            node.error = True
                            self.errorHandler.addError("Variable initialization must have the same type (have {0} and {1})".format(str(ownType), str(initListElement.getType())), line, column)
                            return

                #typecheck with only 1st element of initializer list, example: int a = {1, 2.0, "aaa", 'a'} is ok
                else:
                    # if initializer list does not have any children (int a = {}), error
                    if not child.children:
                        line, column = node.getLineAndColumn()
                        node.error = True
                        self.errorHandler.addError("Empty scalar initializer", line, column)
                        return

                    # only 1st element matters, if multiple initialization elements: warning: excess elements in scalar initializer [enabled by default]
                    if not node.getType().isCompatible(child.children[0].getType(), ignoreRvalue=True, ignoreConst=True):
                        line, column = node.getLineAndColumn()
                        node.error = True
                        self.errorHandler.addError("Variable initialization must have the same type (have {0} and {1})".format(str(node.getType()), str(child.children[0].getType())), line, column)
                        return

                    # if len(child.children) > 1:
                    #     line, column = node.getLineAndColumn()
                    #     self.errorHandler.addWarning("excess elements in scalar initializer", line, column)


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

    def checkStdioFunction(self, node):
        raise Exception("PLS Implement stdio type check")

    #TODO check constness of arguments/parameters
    def visitFunctionCallNode(self, node):
        self.visitChildren(node)

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
                line, column = node.getLineAndColumn()
                node.error = True
                self.errorHandler.addError("Number of arguments to function {0} does not match definition (have {1}, need {2})" \
                    .format(node.identifier, len(arguments.children), len(parameterNodes)), line, column)
                return

            for i, argument in enumerate(arguments.children):
                if not argument.getType().isCompatible(parameterNodes[i].getType(), ignoreRvalue=True, ignoreConst=True):
                    node.errorParameter = i
                    line, column = node.getLineAndColumn()
                    node.error = True
                    self.errorHandler.addError("Arguments to function '{0}' don't match: {1} vs {2}".format(node.identifier, str(argument.getType()), str(parameterNodes[i].getType())), line, column)
                    return
        else:
            raise Exception("Did not find arguments node in ASTFunctionCallNode")


    def typeCheckBinaryOperatorNode(self, node):
        self.visitChildren(node)

        if not node.children[0].getType().toRvalue().isCompatible(node.children[1].getType().toRvalue(), ignoreConst=True):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Binary operator operands must have the same type (have {0} and {1})".format(str(node.children[0].getType()), str(node.children[1].getType())), line, column)
            return


    def visitTernaryConditionalOperatorNode(self, node):
        self.visitChildren(node)

        if not node.children[0].getType().toRvalue().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            node.errorOperand = 0
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Ternary conditional operator needs int as first operand", line, column)
            return

        if node.children[1].getType() != node.children[2].getType():
            node.errorOperand = 1
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Ternary conditional operator alternatives should be of equal type", line, column)
            return


    def visitSimpleAssignmentOperatorNode(self, node):
        self.visitChildren(node)

        if node.children[0].getType().rvalue:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Expression is not assignable", line, column)
            return

        if not node.children[0].getType().toRvalue().isCompatible(node.children[1].getType().toRvalue(), ignoreConst=True):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Incompatible types when assigning to type '{0}' from type '{1}'".format(str(node.children[0].getType()), str(node.children[1].getType())), line, column)
            return


    def visitLogicOperatorNode(self, node):
        self.visitChildren(node)

        if node.children[0].getType().toRvalue() != node.children[1].getType().toRvalue():
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Logic operator operands must have the same type (have {0} and {1})".format(str(node.children[0].getType()), str(node.children[1].getType())), line, column)
            return

        if not node.children[0].getType().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Logic operator operands not compatible with int", line, column)
            return


    def visitComparisonOperatorNode(self, node):
        self.visitChildren(node)

        if not node.children[0].getType().equals(node.children[1].getType(), ignoreRvalue=True, ignoreConst=True):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Comparison operator operands need to be of same type (have {0} and {1})".format(str(node.children[0].getType()), str(node.children[1].getType())), line, column)
            return


    def visitUnaryArithmeticOperatorNode(self, node):
        self.visitChildren(node)

        if node.children[0].getType().rvalue and (node.arithmeticType is ASTUnaryArithmeticOperatorNode.ArithmeticType['increment'] or node.arithmeticType is ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("lvalue required as {0} operand".format(node.arithmeticType.wordStr()), line, column)
            return


    def visitAddressOfoperatorNode(self, node):
        self.visitChildren(node)

        if node.children[0].getType().rvalue:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Cannot take the address of an rvalue of type '{0}'".format(str(node.children[0].getType())), line, column)
            return


    def visitDereferenceNode(self, node):
        self.visitChildren(node)

        ttype = node.getType()
        if ttype.indirections < 0:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("invalid type argument of unary '*' (have '{0}')".format(str(ttype)), line, column)
            return


    def visitLogicalNotOperatorNode(self, node):
        self.visitChildren(node)

        if not node.children[0].getType().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Logical not operator operand not compatible with {0}".format(node.children[0].getType()), line, column)
            return


    def visitArraySubscriptNode(self, node):
        self.typeCheckUnaryOperatorNode(node)


    def visitBinaryArithmeticNode(self, node):
        self.typeCheckBinaryOperatorNode(node)
