from AbstractSyntaxTree import *
from SymbolTable import *
import sys

class ASTSymbolTableFiller:
    def __init__(self, ast:AbstractSyntaxTree, table:SymbolTable):
        self.ast = ast
        self.table = table

    def fill(self, node=None): # call without arguments initially
        if node is None:
            node = self.ast.root
            # self.table.insertSymbol("printf")
            # self.table.insertSymbol("scanf")

        openedScope = False

        if isinstance(node, (ASTVariableNode, ASTFunctionCallNode)):
            if self.table.retrieveSymbol(node.identifier) is None:
                print("Identifier '" + node.identifier + "' used before it was declared.")
                sys.exit()

        elif isinstance(node, ASTFunctionDeclarationNode):
            self.table.insertFunctionSymbol(node)

        elif isinstance(node, (ASTDeclaratorInitializerNode, ASTParameterNode)):
            self.table.insertVariableSymbol(node)

        elif isinstance(node, ASTStatementsNode):
            openedScope = True
            self.table.openScope()

        for child in node.children:
            self.fill(child)

        if openedScope:
            self.table.closeScope()
