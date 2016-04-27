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

        # check if variable is declared and if function is declared and defined
        if isinstance(node, (ASTVariableNode, ASTFunctionCallNode)):
            symbolInfo = self.table.retrieveSymbol(node.identifier)

            if symbolInfo is None:
                if isinstance(node, ASTVariableNode):
                    raise Exception("Variable '" + node.identifier + "' used before it was declared")
                elif isinstance(node, ASTFunctionCallNode):
                    raise Exception("Function '" + node.identifier + "' used before it was declared")
            else:
                if isinstance(node, ASTFunctionCallNode) and not symbolInfo.defined:
                    raise Exception("Function: undefined reference")

        # insert function declaration or definition into symbol table
        elif isinstance(node, ASTFunctionDeclarationNode):
            self.table.insertFunctionSymbol(node)

            # in function definition, open new scope (earlier than normal) to add paramaters
            if isinstance(node, (ASTFunctionDefinitionNode)):
                openedScope = True
                self.table.openScope()

        # put variables and parameters into the currently open scope, but not parameters of a function declaration
        elif isinstance(node, (ASTDeclaratorInitializerNode, ASTParameterNode)) and type(node.parent.parent) is not ASTFunctionDeclarationNode:
            self.table.insertVariableSymbol(node)

        # statements node does not have to open another scope: was already opened by function definition
        elif isinstance(node, ASTStatementsNode) and not isinstance(node.parent, ASTFunctionDefinitionNode):
            openedScope = True
            self.table.openScope()

        # handle children scopes
        for child in node.children:
            self.fill(child)

        # close opened scope
        if openedScope:
            self.table.closeScope()
