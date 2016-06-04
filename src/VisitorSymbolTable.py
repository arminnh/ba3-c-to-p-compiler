from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorSymbolTable(Visitor):
    def __init__(self, symbolTable, errorHandler):
        super(VisitorSymbolTable, self).__init__(errorHandler)
        self.table = symbolTable

    # checks if it is ok to enter a symbol into the symbol table, otherwise it puts an error in errorhandler
    def insertSymbol(self, node, isFunction):
        result = None
        if isFunction:
            result = self.table.isInsertionOk(node, isFunction=True)
        else:
            result = self.table.isInsertionOk(node, isFunction=False)

        if result == True:
            if isFunction:
                self.table.insertFunctionSymbol(node)
            else:
                self.table.insertVariableSymbol(node)
        elif result != False:
            # result is (error, node)
            self.addError(result[0], result[1])
            return False


    def visitMainFunctionNode(self, node):
        self.visitFunctionDefinitionNode(node)


    def visitStatementsNode(self, node):
        openedScope = False

        if not isinstance(node.parent, (ASTFunctionDefinitionNode, ASTForNode)):
            openedScope = True
            self.table.openScope()

        self.visitChildren(node)

        if openedScope:
            self.table.closeScope()

    def visitForNode(self, node):
        self.table.openScope()
        if node.initializer:
            node.initializer.accept(self)
        if node.condition:
            node.condition.accept(self)
        if node.iteration:
            node.iteration.accept(self)
        self.visitChildren(node)
        self.table.closeScope()