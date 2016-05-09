from antlr4 import *
from AbstractSyntaxTree import *
from VisitorSymbolTable import *

class VisitorDefinitionProcessor(VisitorSymbolTable):

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
        self.table.openScope(node.identifier)
        self.visitChildren(node)
        self.table.closeScope()


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
