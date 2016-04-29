from AbstractSyntaxTree import *
from SymbolTable import *
import sys

class ASTSymbolTableFiller:
    def __init__(self, ast:AbstractSyntaxTree, table:SymbolTable, errorHandler:CompilerErrorHandler):
        self.ast = ast
        self.table = table
        self.errorHandler = errorHandler

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
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("Variable '" + node.identifier + "' used before it was declared", line, column)
                elif isinstance(node, ASTFunctionCallNode):
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("Function '" + node.identifier + "' used before it was declared", line, column)
            elif isinstance(node, ASTFunctionCallNode):
                if not symbolInfo.defined:
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("Function: undefined reference", line, column)
                node.definitionNode = symbolInfo.astnode
            elif isinstance(node, ASTVariableNode):
                node.type = symbolInfo.typeInfo

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
