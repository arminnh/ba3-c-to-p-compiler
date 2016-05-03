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
                    self.errorHandler.addError("Variable '{0}' used before it was declared".format(node.identifier), line, column)
                elif isinstance(node, ASTFunctionCallNode):
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("Function '{0}' used before it was declared".format(node.identifier), line, column)
            elif isinstance(node, ASTFunctionCallNode):
                if not symbolInfo.defined:
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("Function: undefined reference", line, column)
                node.definitionNode = symbolInfo.astnode
            elif isinstance(node, ASTVariableNode):
                node.typeInfo = symbolInfo.typeInfo

        # insert function declaration or definition into symbol table
        elif isinstance(node, ASTFunctionDeclarationNode):
            self.table.insertFunctionSymbol(node)

            # in function definition, open new scope (earlier than normal) to add paramaters
            if isinstance(node, (ASTFunctionDefinitionNode)):
                openedScope = True
                self.table.openScope(node.identifier)

        # put variables and parameters into the currently open scope, but not parameters of a function declaration
        elif isinstance(node, ASTDeclaratorInitializerNode) and type(node.parent.parent) is not ASTFunctionDeclarationNode:
            self.table.insertVariableSymbol(node)

        # put variables and parameters into the currently open scope, but not parameters of a function declaration
        elif isinstance(node, ASTParameterNode):
            # in a function definition, all parameters need to have identifiers
            parametersCount = len(node.parent.children)

            if node.basetype == "void":
                if node.identifier is None and parametersCount > 1:
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("‘void’ must be the only parameter", line, column)
                elif node.identifier is not None and node.getType().indirections == 0:
                    line, column = node.getLineAndColumn()
                    self.errorHandler.addError("Parameter has incomplete type", line, column)

            elif node.identifier is None and isinstance(node.parent.parent, ASTFunctionDefinitionNode):
                line, column = node.getLineAndColumn()
                self.errorHandler.addError("Parameter name omitted", line, column)

            if type(node.parent.parent) is not ASTFunctionDeclarationNode:
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
