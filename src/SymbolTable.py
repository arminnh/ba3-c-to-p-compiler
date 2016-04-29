from AbstractSyntaxTree import *

offset = "    "

class SymbolInfo:
    def __init__(self, astnode):
        self.astnode = astnode
        self.typeInfo = astnode.getType()

class VariableSymbolInfo(SymbolInfo):
    def __init__(self, astnode):
        # astnode is ASTDeclaratorInitializerNode
        super(VariableSymbolInfo, self).__init__(astnode)

    @property
    def defined(self):
        for child in self.astnode.children:
            if isinstance(child, ASTExpressionNode):
                return True
        return False


class FunctionSymbolInfo(SymbolInfo):
    def __init__(self, astnode):
        super(FunctionSymbolInfo, self).__init__(astnode)

    @property
    def defined(self):
        return isinstance(self.astnode, ASTFunctionDefinitionNode)


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.symbols = {}

    def addChild(self):
        new = Scope(self)
        self.children.append(new)
        return new

    def insertSymbol(self, info:SymbolInfo):
        if self.isInsertionOk(info):
            #print("inserted id " + str(info.astnode.identifier) + " into symbol table")
            self.symbols[info.astnode.identifier] = info

    def retrieveSymbol(self, name):
        return self.symbols.get(name)

    def isInsertionOk(self, new:SymbolInfo):
        old = self.retrieveSymbol(new.astnode.identifier)

        if old is not None:
            if isinstance(old.astnode, ASTDeclaratorInitializerNode):
                line, column = new.astnode.getLineAndColumn()
                new.astnode.errorHandler.addError("Identifier " + old.astnode.identifier + " already taken by variable", line, column)

            if type(new) is FunctionSymbolInfo:
                if type(new.astnode) is ASTFunctionDefinitionNode:
                    if type(old.astnode) is ASTFunctionDeclarationNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return True # definition can overwrite declaration
                        else:
                            line, column = new.astnode.getLineAndColumn() # TODO: get line, column of old declaration as well
                            new.astnode.errorHandler.addError("Function definition parameters don't match with previous declaration", line, column)
                            return False

                    elif type(old.astnode) is ASTFunctionDefinitionNode:
                        if not old.astnode.getType().isCompatible(new.astnode.getType()):
                            line, column = new.astnode.getLineAndColumn()
                            new.astnode.errorHandler.addError("Conflicting types for function definition " + str(new.astnode.identifier), line, column)
                            return False
                        else:
                            line, column = new.astnode.getLineAndColumn()
                            new.astnode.errorHandler.addError("Redefinition of function", line, column)
                            return False

                elif isinstance(new.astnode, ASTFunctionDeclarationNode):
                    if type(old.astnode) is ASTFunctionDefinitionNode:
                        if not old.astnode.getType().isCompatible(new.astnode.getType()):
                            line, column = new.astnode.getLineAndColumn()
                            new.astnode.errorHandler.addError("Conflicting types for function declaration " + str(new.astnode.identifier), line, column)
                            return False

                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return False # declaration cannot overwrite definition
                        else:
                            line, column = new.astnode.getLineAndColumn()
                            new.astnode.errorHandler.addError("Function declaration parameters don't match previous definition", line, column)
                            return False

                    elif type(old.astnode) is ASTFunctionDeclarationNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return False # declaration cannot overwrite definition
                        else:
                            line, column = new.astnode.getLineAndColumn()
                            new.astnode.errorHandler.addError("Function declaration parameters don't match previous declaration", line, column)
                            return False

            elif type(new) is VariableSymbolInfo:
                line, column = old.astnode.getLineAndColumn()
                new.astnode.errorHandler.addError("Identifier " + old.astnode.identifier + " already taken by function", line, column)
                return False

        else:
            return True


    def out(self, level):
        out = offset * level + "Scope:\n"
        for key, value in self.symbols.items():
            out += offset * (level + 1) + key + ": " + str(value.astnode.getType()) + "\n"

        for child in self.children:
            out += child.out(level + 1)

        return out

class SymbolTable(object):
    def __init__(self):
        self.root = Scope()
        self.currentScope = self.root

    def openScope(self):
        self.currentScope = self.currentScope.addChild()

    def closeScope(self):
        self.currentScope = self.currentScope.parent

    def insertVariableSymbol(self, astnode):
        self.currentScope.insertSymbol(VariableSymbolInfo(astnode))

    def insertFunctionSymbol(self, astnode):
        self.currentScope.insertSymbol(FunctionSymbolInfo(astnode))

    def retrieveSymbol(self, name):
        scope = self.currentScope
        while scope is not None:
            nametype = scope.retrieveSymbol(name)
            if nametype is not None:
                return nametype
            scope = scope.parent

    def __str__(self):
        return self.root.out(0)

if __name__ == "__main__":
    table = SymbolTable()
    table.insertSymbol("a", int)
    table.insertSymbol("b", float)
    table.openScope()
    table.insertSymbol("c", str)
    print(table.retrieveSymbol("a"))
    print(table.retrieveSymbol("b"))
    print(table.retrieveSymbol("c"))
    print(table.retrieveSymbol("d"))
    table.closeScope()
    table.openScope()
    table.insertSymbol("d", float)
    table.insertSymbol("b", int)
    print()
    print(table.retrieveSymbol("a"))
    print(table.retrieveSymbol("b"))
    print(table.retrieveSymbol("c"))
    print(table.retrieveSymbol("d"))
    table.closeScope()
    print()
    print(table.retrieveSymbol("a"))
    print(table.retrieveSymbol("b"))
    print(table.retrieveSymbol("c"))
    print(table.retrieveSymbol("d"))
