from NestedListsLexer import *
from NestedListsListener import *
from NestedListsVisitor import *
from antlr4 import *


class MyNestedListsListener(NestedListsListener):
    def enterItm(self, ctx):
        print (ctx.INT())


# class MyNestedListsVisitor(NestedListsVisitor):
#	def 

if __name__ == '__main__':
    lijst1 = "(1,2,3)"
    lijst2 = "(1,2,3,(1,2),())"
    lijst3 = "(1,2,3,(1,2),(),(((()))), (1))"

    lexer = NestedListsLexer(InputStream(lijst2))
    stream = CommonTokenStream(lexer)
    parser = NestedListsParser(stream)

    tree = parser.nstdlst()
    walk = ParseTreeWalker()
    listener = MyNestedListsListener()
    # listener.enterItm(context)
    walk.walk(listener, tree)
