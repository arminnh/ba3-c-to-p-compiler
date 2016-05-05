from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorFillSymbolTable(Visitor):
    def __init__(self, symbolTable, errorHandler):
        self.table = symbolTable
        self.errorHandler = errorHandler


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
            # result is (error, line, column)
            node.error = True
            self.errorHandler.addError(*result)
            return False


    def visitIncludeNode(self, node):
        pass


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

        self.table.openScope(node.identifier)
        self.visitChildren(node)
        self.table.closeScope()


    def visitMainFunctionNode(self, node):
        self.visitFunctionDefinitionNode(node)


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


    def visitStatementsNode(self, node):
        openedScope = False

        if not isinstance(node.parent, ASTFunctionDefinitionNode):
            openedScope = True
            self.table.openScope()

        self.visitChildren(node)

        if openedScope:
            self.table.closeScope()


    # int a[myFun(5)] = {1, 2+"a", 3}
    # put variables and parameters into the currently open scope, but not parameters of a function declaration
    def visitDeclaratorInitializerNode(self, node):
        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return

        self.visitChildren(node)


    def visitIntegerLiteralNode(self, node):
        pass


    def visitFloatLiteralNode(self, node):
        pass


    def visitCharacterLiteralNode(self, node):
        pass


    def visitStringLiteralNode(self, node):
        pass


    def visitVariableNode(self, node):
        symbolInfo = self.table.retrieveSymbol(node.identifier)

        if symbolInfo is None:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Variable '{0}' used before it was declared".format(node.identifier), line, column)
            return
        else:
            node.typeInfo = symbolInfo.typeInfo


    # check if function is declared and defined
    def visitFunctionCallNode(self, node):
        symbolInfo = self.table.retrieveSymbol(node.identifier)

        if symbolInfo is None:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Function '{0}' used before it was declared".format(node.identifier), line, column)
            return
        elif not symbolInfo.defined:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Function: undefined reference", line, column)
            return

        node.definitionNode = symbolInfo.astnode

        self.visitChildren(node)
