from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorSymbolTable(Visitor):
    def __init__(self, symbolTable, errorHandler):
        self.table = symbolTable
        self.errorHandler = errorHandler

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
            node.error = True
            # result is (error, line, column)
            self.errorHandler.addError(*result)
            return False

    def visitParameterNode(self, node):
        # in a function definition, all parameters need to have identifiers
        parametersCount = len(node.parent.children)

        if node.basetype == "void":
            if node.identifier is None and parametersCount > 1:
                line, column = node.getLineAndColumn()
                node.error = True
                self.errorHandler.addError("‘void’ must be the only parameter", line, column)
                return

            elif node.identifier is not None and node.getType().indirections == 0:
                line, column = node.getLineAndColumn()
                node.error = True
                self.errorHandler.addError("Parameter has incomplete type", line, column)
                return

        elif node.identifier is None and isinstance(node.parent.parent, ASTFunctionDefinitionNode):
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Parameter name omitted", line, column)
            return

        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return

        self.visitChildren(node)

    def visitMainFunctionNode(self, node):
        self.visitFunctionDefinitionNode(node)

    def visitStatementsNode(self, node):
        openedScope = False

        if not isinstance(node.parent, ASTFunctionDefinitionNode):
            openedScope = True
            self.table.openScope()

        self.visitChildren(node)

        if openedScope:
            self.table.closeScope()