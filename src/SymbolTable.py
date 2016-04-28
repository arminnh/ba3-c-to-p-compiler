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
        for child in self.astnode.getChildren():
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
                raise Exception("identifier " + old.astnode.identifier + " already taken by variable")

            if type(new) is FunctionSymbolInfo:
                if type(new.astnode) is ASTFunctionDefinitionNode:
                    if type(old.astnode) is ASTFunctionDeclarationNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return True #definition can overwrite declaration
                        else:
                            raise Exception("parameters don't match")

                    elif type(old.astnode) is ASTFunctionDefinitionNode:
                        raise Exception("redefinition of function")

                    elif type(old.astnode) is ASTDeclaratorInitializerNode:
                        raise Exception("identifier already taken by function")

                elif isinstance(new.astnode, ASTFunctionDeclarationNode):
                    if type(old.astnode) is ASTFunctionDefinitionNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return False # declaration cannot overwrite definition
                        else:
                            raise Exception("parameters don't match")

                    elif type(old.astnode) is ASTFunctionDeclarationNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return False # declaration cannot overwrite definition
                        else:
                            raise Exception("parameters don't match")

            elif type(new) is VariableSymbolInfo:
                raise Exception("identifier " + old.astnode.identifier + " already taken")

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
