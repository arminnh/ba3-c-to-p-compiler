from antlr4 import *
from AbstractSyntaxTree import *
from VisitorSymbolTable import *

class VisitorDeclarationProcessing(VisitorSymbolTable):

    def visitIncludeNode(self, node):
        if node.isStdInclude and node.name == "stdio.h":
            printf = ASTFunctionDefinitionNode()
            printf.identifier = "printf"
            printf.basetype = "void"
            printf.isStdPrintf = True

            scanf = ASTFunctionDefinitionNode()
            scanf.identifier = "scanf"
            scanf.basetype = "void"
            scanf.isStdScanf =  True

            printfOk = self.table.isInsertionOk(printf, isFunction=True)
            scanfOk = self.table.isInsertionOk(scanf, isFunction=False)

            if printfOk:
                self.table.insertFunctionSymbol(printf)
            if scanfOk:
                self.table.insertFunctionSymbol(scanf)


    def visitParameterNode(self, node):
        # node.identifier is None in case of void argument
        if type(node.parent.parent) is not ASTFunctionDeclarationNode and node.identifier is not None:
            symbolInfo = self.table.retrieveSymbol(node.identifier, requireSeen=False)
            if symbolInfo is None:
                raise Exception("Expected to find " + str(node.identifier) + " in symbol table")

            symbolInfo.seen = True


    # int a[myFun(5)] = {1, 2+"a", 3}
    # put variables and parameters into the currently open scope, but not parameters of a function declaration
    def visitDeclaratorInitializerNode(self, node):
        # if type(node.parent.parent) is not ASTFunctionDeclarationNode:
        symbol = self.table.retrieveSymbol(node.identifier, requireSeen=False)
        if symbol is None:
            raise Exception("Expected to find " + str(node.identifier) + " in symbol table")

        symbol.seen = True

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

        if symbolInfo is None or symbolInfo.seen == False:
            line, column = node.getLineAndColumn()
            node.error = True
            self.errorHandler.addError("Variable '{0}' used before it was declared".format(node.identifier), line, column)
            return
        else:
            node.typeInfo = symbolInfo.typeInfo

    def visitFunctionDefinitionNode(self, node):
        self.table.openScope(node.identifier)
        self.visitChildren(node)
        self.table.closeScope()

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
