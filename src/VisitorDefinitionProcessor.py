from antlr4 import *
from AbstractSyntaxTree import *
from VisitorSymbolTable import *

class VisitorDefinitionProcessor(VisitorSymbolTable):

    def visitProgramNode(self, node):
        self.visitChildren(node)
        self.table.resetToRoot()


    def visitStringLiteralNode(self, node):
        self.table.insertStringLiteral(node)


    def visitBreakNode(self, node):
        breakFrom = node
        while not isinstance(breakFrom, (ASTForNode, ASTWhileNode)) and breakFrom is not None:
            breakFrom = breakFrom.parent

        if breakFrom is None:
            self.addError("'break' statement not in loop statement", node)

        node.breakFrom = breakFrom


    def visitContinueNode(self, node):
        continueTo = node
        while not isinstance(continueTo, (ASTForNode, ASTWhileNode)) and continueTo is not None:
            continueTo = continueTo.parent

        if continueTo is None:
            self.addError("'continue' statement not in loop statement", node)

        node.continueTo = continueTo


    def visitTypeCastNode(self, node):
        if not node.typeSpecifierPresent:
            self.addWarning("type specifier missing, defaults to 'int'", node)


    # int a[myFun(5)] = {1, 2+"a", 3}
    # put variables and parameters into the currently open scope, but not parameters of a function declaration
    def visitDeclaratorInitializerNode(self, node):
        arrayLength = []
        for child in reversed(node.children):
            if isinstance(child, ASTIntegerLiteralNode):
                arrayLength.append(child)

        i = 0
        for j in range(len(node.indirections)):
            if node.indirections[j][0]:
                if i >= len(arrayLength):
                    # raise Exception("not enough array length nodes")
                    break

                node.indirections[j] = (arrayLength[i].value, node.indirections[j][1])
                i += 1

        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            if not node.parent.typeSpecifierPresent:
                self.addWarning("type specifier missing in declaration of '{0}', type defaults to 'int'".format(node.identifier), node)
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return

        self.visitChildren(node)


    # insert function declaration into symbol table
    def visitFunctionDeclarationNode(self, node):
        if not node.typeSpecifierPresent:
            self.addWarning("data definition has no type or storage class, type defaults to 'int' in declaration of '{0}'".format(node.identifier), node)
        result = self.insertSymbol(node, isFunction=True)
        if result == False:
            return

        self.visitChildren(node)


    # insert function definition into symbol table
    def visitFunctionDefinitionNode(self, node):
        if not node.typeSpecifierPresent:
            self.addWarning("type specifier missing, return type defaults to 'int'", node)
        result = self.insertSymbol(node, isFunction=True)
        if result == False:
            return
        self.table.openScope(True, node.identifier)
        self.visitChildren(node)
        self.table.closeScope()


    def visitParameterNode(self, node):
        # in a function definition, all parameters need to have identifiers
        parametersCount = len(node.parent.children)

        if node.baseType == "void" and node.getType().nrIndirections() == 0:
            if node.identifier is None and parametersCount > 1:
                self.addError("'void' must be the only parameter", node)
                return

            elif node.identifier is not None:
                self.addError("parameter '{0}' has incomplete type".format(node.identifier), node)
                return
            return

        elif node.identifier is None and isinstance(node.parent.parent, ASTFunctionDefinitionNode):
            self.addError("parameter name omitted", node)
            return

        elif not node.typeSpecifierPresent:
            self.addWarning("type specifier missing in declaration of '{0}', type defaults to 'int'".format(node.identifier), node)

        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return

        self.visitChildren(node)
