class SymbolInfo:
	def __init__(self, nametype):
		self.type = nametype

class Scope:
	def __init__(self, parent=None):
		self.parent = parent
		self.children = []
		self.symbols = {}

	def addChild(self):
		new = Scope(self)
		self.children.append(new)
		return new

	def insertSymbol(self, name, nametype):
		self.symbols[name] = nametype

	def retrieveSymbol(self, name):
		return self.symbols.get(name)

class SymbolTable(object):
	def __init__(self):
		self.root = Scope()
		self.currentScope = self.root

	def openScope(self):
		self.currentScope = self.currentScope.addChild()

	def closeScope(self):
		self.currentScope = self.currentScope.parent

	def insertSymbol(self, name, nametype):
		self.currentScope.insertSymbol(name, nametype)

	def retrieveSymbol(self, name):
		scope = self.currentScope
		while scope is not None:
			nametype = scope.retrieveSymbol(name)
			if nametype is not None:
				return nametype
			scope = scope.parent



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
