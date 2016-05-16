from antlr4 import *
from AbstractSyntaxTree import *
from VisitorSymbolTable import *

class VisitorDeclarationProcessor(VisitorSymbolTable):

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


    def visitVariableNode(self, node):
        symbolInfo = self.table.retrieveSymbol(node.identifier)

        if symbolInfo is None or symbolInfo.seen == False:
            self.addError("variable '{0}' undeclared".format(node.identifier), node)
            return
        else:
            node.typeInfo = symbolInfo.typeInfo

    def visitFunctionDefinitionNode(self, node):
        self.table.openScope(True, node.identifier)
        self.visitChildren(node)
        self.table.closeScope()

    # check if function is declared and defined
    def visitFunctionCallNode(self, node):
        symbolInfo = self.table.retrieveSymbol(node.identifier)

        if symbolInfo is None:
            self.addError("function '{0}' undeclared".format(node.identifier), node)
            return
        elif not symbolInfo.defined:
            self.addError("function: undefined reference to '{0}'".format(node.identifier), node)
            return

        node.definitionNode = symbolInfo.astnode

        self.visitChildren(node)
