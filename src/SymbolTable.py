from AbstractSyntaxTree import *

offset = "    "

class SymbolInfo:
    def __init__(self, astnode):
        astnode.symbolInfo = self
        self.address = None
        self.astnode = astnode
        self.typeInfo = astnode.getType()

class VariableSymbolInfo(SymbolInfo):
    def __init__(self, astnode):
        # astnode is ASTDeclaratorInitializerNode
        self.seen = False
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
    def __init__(self, parent=None, isFunctionScope=False, name=None):
        self.isFunctionScope = isFunctionScope
        self.addressCounter = None
        self.addressedVariables = []
        self.name = name
        self.parent = parent
        self.currentChild = 0
        self.children = []
        self.symbols = {}

    def getAddressCounter(self):
        if self.parent is None or self.isFunctionScope:
            if self.addressCounter is None:
                self.addressCounter = -1 # initialize
            return self.addressCounter
        return self.parent.getAddressCounter()

    def assignAddress(self, variable):
        if self.parent is None or self.isFunctionScope:
            if self.addressCounter is None:
                self.addressCounter = -1 # initialize
            self.addressedVariables.append(variable) # put variable into function scope variable address list
            self.addressCounter += 1 # increment counter
            variable.address = self.addressCounter # set variable's address
            return self.addressCounter
        return self.parent.assignAddress(variable)

    def addChild(self, scope):
        scope.parent = self
        self.children.append(scope)
        return scope

    def insertSymbol(self, info:SymbolInfo):
        #print("inserted id " + str(info.astnode.identifier) + " into symbol table")
        if (info.typeInfo.basetype != "void" or info.typeInfo.indirections != 0) and isinstance(info, VariableSymbolInfo):
            self.assignAddress(info)
        self.symbols[info.astnode.identifier] = info

    def retrieveSymbol(self, name, requireSeen):
        if name is None:
            return None

        symbolInfo = self.symbols.get(name)

        if symbolInfo is not None and requireSeen:
            if isinstance(symbolInfo, VariableSymbolInfo) and symbolInfo.seen == False:
                return None
        return symbolInfo

    def isInsertionOk(self, new:SymbolInfo):
        old = self.retrieveSymbol(new.astnode.identifier, requireSeen=False)

        if old is not None:
            if isinstance(old.astnode, ASTDeclaratorInitializerNode):
                return ("Identifier {0} already taken by variable".format(old.astnode.identifier), new.astnode)

            if type(new) is FunctionSymbolInfo:
                if isinstance(new.astnode, ASTFunctionDefinitionNode):
                    if type(old.astnode) is ASTFunctionDeclarationNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return True # definition can overwrite declaration
                        else:
                            return ("Function definition parameters don't match with previous declaration", new.astnode)

                    elif isinstance(old.astnode, ASTFunctionDefinitionNode):
                        return ("Redefinition of function '{0}'".format(new.astnode.identifier), new.astnode)

                elif isinstance(new.astnode, ASTFunctionDeclarationNode):
                    if type(old.astnode) is ASTFunctionDefinitionNode:
                        if not old.astnode.getType().isCompatible(new.astnode.getType()):
                            return ("Conflicting types for function declaration " + str(new.astnode.identifier), new.astnode)

                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return False # declaration cannot overwrite definition
                        else:
                            return ("Function declaration parameters don't match previous definition", new.astnode)

                    elif type(old.astnode) is ASTFunctionDeclarationNode:
                        if old.astnode.getParameters() == new.astnode.getParameters():
                            return False # declaration cannot overwrite definition
                        else:
                            return ("Function declaration parameters don't match previous declaration", new.astnode)

            elif type(new) is VariableSymbolInfo:
                return ("Identifier {0} already taken by function".format(old.astnode.identifier), old.astnode)

        else:
            return True


    def out(self, level):
        out = offset * level + "Scope" + (" " + self.name if self.name is not None else "") + ":\n"
        if self.isFunctionScope:
            out += offset * (level + 1) + str([info.typeInfo.basetype for info in self.addressedVariables]) + "\n"
        for key, value in self.symbols.items():
            out += offset * (level + 1) + str(key) + ": " + str(value.astnode.getType())
            if value.address is not None:
                out += " | " + str(value.address)
            out += "\n"

        for child in self.children:
            out += child.out(level + 1)

        return out

class SymbolTable(object):
    def __init__(self):
        self.traverse = False
        self.root = Scope()
        self.currentScope = self.root

    def openScope(self, isFunctionScope=False, name=None):
        if self.traverse:
            if self.currentScope.currentChild >= len(self.currentScope.children):
                raise Exception("Trying to open nonexisting scope; current scope:\n" + self.currentScope.out(0) + "am at child " + str(self.currentScope.currentChild))
            self.currentScope.currentChild += 1
            self.currentScope = self.currentScope.children[self.currentScope.currentChild - 1]
            if name != self.currentScope.name:
                print("Warning: Symbol table open scope traverse: expected {0}, got {1}".format(self.currentScope.name, name))
            self.currentScope.currentChild = 0
        else:
            scope = self.currentScope
            self.currentScope = self.currentScope.addChild(Scope(isFunctionScope=isFunctionScope, name=name))

    def closeScope(self):
        self.currentScope = self.currentScope.parent

    def insertVariableSymbol(self, astnode):
        self.currentScope.insertSymbol(VariableSymbolInfo(astnode))

    def insertFunctionSymbol(self, astnode):
        self.currentScope.insertSymbol(FunctionSymbolInfo(astnode))

    def isInsertionOk(self, astnode, isFunction):
        if isFunction:
            return self.currentScope.isInsertionOk(FunctionSymbolInfo(astnode))
        else:
            return self.currentScope.isInsertionOk(VariableSymbolInfo(astnode))

    def retrieveSymbol(self, name, requireSeen=True):
        scope = self.currentScope
        while scope is not None:
            nametype = scope.retrieveSymbol(name, requireSeen)
            if nametype is not None:
                return nametype
            scope = scope.parent

    def __str__(self):
        return self.root.out(0)

    def traverseOn(self):
        self.traverse = True
        self.resetToRoot()

    def traverseOff(self):
        self.traverse = False

    def resetToRoot(self):
        self.currentScope = self.root
        self.root.currentChild = 0
