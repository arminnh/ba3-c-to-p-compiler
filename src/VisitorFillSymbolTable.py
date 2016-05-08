from antlr4 import *
from AbstractSyntaxTree import *
from VisitorSymbolTable import *

class VisitorFillSymbolTable(VisitorSymbolTable):

    # int a[myFun(5)] = {1, 2+"a", 3}
    # put variables and parameters into the currently open scope, but not parameters of a function declaration
    def visitDeclaratorInitializerNode(self, node):
        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return

        self.visitChildren(node)

    # insert function declaration into symbol table
    def visitFunctionDeclarationNode(self, node):
        result = self.insertSymbol(node, isFunction=True)
        if result == False:
            return

        self.visitChildren(node)


    # insert function definition into symbol table
    def visitFunctionDefinitionNode(self, node):
        result = self.insertSymbol(node, isFunction=True)
        if result == False:
            return
        # print("function visitor: opening scope for " + node.identifier)
        self.table.openScope(node.identifier)
        self.visitChildren(node)
        self.table.closeScope()