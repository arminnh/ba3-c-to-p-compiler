
class Visitor:
    def __init__(self, errorHandler):
        self.errorHandler = errorHandler

    def visitChildren(self, node):
        for child in node.children:
            if not self.shouldVisitNextChild(node):
                pass

            child.accept(self)

    def shouldVisitNextChild(self, node):
        True


    def visitProgramNode(self, node):
        raise NotImplementedError


    def visitIncludeNode(self, node):
        raise NotImplementedError


    def visitFunctionDeclarationNode(self, node):
        raise NotImplementedError


    def visitFunctionDefinitionNode(self, node):
        raise NotImplementedError


    def visitMainFunctionNode(self, node):
        raise NotImplementedError


    def visitParametersNode(self, node):
        raise NotImplementedError


    def visitParameterNode(self, node):
        raise NotImplementedError


    def visitArgumentsNode(self, node):
        raise NotImplementedError


    def visitInitializerListNode(self, node):
        raise NotImplementedError


    def visitStatementsNode(self, node):
        raise NotImplementedError


    def visitStatementNode(self, node):
        raise NotImplementedError


    def visitReturnNode(self, node):
        raise NotImplementedError


    def visitIfNode(self, node):
        raise NotImplementedError


    def visitElseNode(self, node):
        raise NotImplementedError


    def visitWhileNode(self, node):
        raise NotImplementedError


    def visitDoWhileNode(self, node):
        raise NotImplementedError


    def visitVariableDeclarationNode(self, node):
        raise NotImplementedError


    def visitDeclaratorInitializerNode(self, node):
        raise NotImplementedError


    def visitIntegerLiteralNode(self, node):
        raise NotImplementedError


    def visitFloatLiteralNode(self, node):
        raise NotImplementedError


    def visitCharacterLiteralNode(self, node):
        raise NotImplementedError


    def visitStringLiteralNode(self, node):
        raise NotImplementedError


    def visitVariableNode(self, node):
        raise NotImplementedError


    def visitFunctionCallNode(self, node):
        raise NotImplementedError


    def typeCheckUnaryOperatorNode(self, node):
        raise NotImplementedError


    def typeCheckBinaryOperatorNode(self, node):
        raise NotImplementedError


    def visitTernaryConditionalOperatorNode(self, node):
        raise NotImplementedError


    def visitSimpleAssignmentOperatorNode(self, node):
        raise NotImplementedError


    def visitLogicOperatorNode(self, node):
        raise NotImplementedError


    def visitComparisonOperatorNode(self, node):
        raise NotImplementedError


    def visitUnaryArithmeticOperatorNode(self, node):
        raise NotImplementedError


    def visitAddressOfoperatorNode(self, node):
        raise NotImplementedError


    def visitDereferenceNode(self, node):
        raise NotImplementedError


    def visitLogicalNotOperatorNode(self, node):
        raise NotImplementedError


    def visitArraySubscriptNode(self, node):
        raise NotImplementedError


    def visitBinaryArithmeticNode(self, node):
        raise NotImplementedError