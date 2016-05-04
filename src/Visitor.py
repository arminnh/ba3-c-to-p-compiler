
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
        self.visitChildren(node)


    def visitIncludeNode(self, node):
        self.visitChildren(node)


    def visitFunctionDeclarationNode(self, node):
        self.visitChildren(node)


    def visitFunctionDefinitionNode(self, node):
        self.visitChildren(node)


    def visitMainFunctionNode(self, node):
        self.visitChildren(node)


    def visitParametersNode(self, node):
        self.visitChildren(node)


    def visitParameterNode(self, node):
        self.visitChildren(node)


    def visitArgumentsNode(self, node):
        self.visitChildren(node)


    def visitInitializerListNode(self, node):
        self.visitChildren(node)


    def visitStatementsNode(self, node):
        self.visitChildren(node)


    def visitStatementNode(self, node):
        self.visitChildren(node)


    def visitReturnNode(self, node):
        self.visitChildren(node)


    def visitIfNode(self, node):
        self.visitChildren(node)


    def visitElseNode(self, node):
        self.visitChildren(node)


    def visitWhileNode(self, node):
        self.visitChildren(node)


    def visitDoWhileNode(self, node):
        self.visitChildren(node)


    def visitVariableDeclarationNode(self, node):
        self.visitChildren(node)


    def visitDeclaratorInitializerNode(self, node):
        self.visitChildren(node)


    def visitIntegerLiteralNode(self, node):
        self.visitChildren(node)


    def visitFloatLiteralNode(self, node):
        self.visitChildren(node)


    def visitCharacterLiteralNode(self, node):
        self.visitChildren(node)


    def visitStringLiteralNode(self, node):
        self.visitChildren(node)


    def visitVariableNode(self, node):
        self.visitChildren(node)


    def visitFunctionCallNode(self, node):
        self.visitChildren(node)


    def typeCheckUnaryOperatorNode(self, node):
        self.visitChildren(node)


    def typeCheckBinaryOperatorNode(self, node):
        self.visitChildren(node)


    def visitTernaryConditionalOperatorNode(self, node):
        self.visitChildren(node)


    def visitSimpleAssignmentOperatorNode(self, node):
        self.visitChildren(node)


    def visitLogicOperatorNode(self, node):
        self.visitChildren(node)


    def visitComparisonOperatorNode(self, node):
        self.visitChildren(node)


    def visitUnaryArithmeticOperatorNode(self, node):
        self.visitChildren(node)


    def visitAddressOfoperatorNode(self, node):
        self.visitChildren(node)


    def visitDereferenceNode(self, node):
        self.visitChildren(node)


    def visitLogicalNotOperatorNode(self, node):
        self.visitChildren(node)


    def visitArraySubscriptNode(self, node):
        self.visitChildren(node)


    def visitBinaryArithmeticNode(self, node):
        self.visitChildren(node)
