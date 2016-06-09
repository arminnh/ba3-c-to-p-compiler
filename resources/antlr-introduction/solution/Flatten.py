import sys
from antlr4 import *
from listsLexer import listsLexer
from listsParser import listsParser
from listsListener import listsListener
from listsVisitor import listsVisitor

def main(filename):
    input = FileStream(filename)
    lexer = listsLexer(input)
    stream = CommonTokenStream(lexer)
    parser = listsParser(stream)
    tree = parser.lst() # top rule
    # check order
    try:
        ParseTreeWalker().walk(CheckOrderListener(), tree) # using a listener
    except Exception as e:
        print  e
        return
    # flatten
    flatten(tree) # ad hoc
    print
    ParseTreeWalker().walk(FlattenListener(), tree) # using a listener
    print
    tree.accept(FlattenVisitor()) # using a visitor

# A listener
# When using a listener, the AST traversal is predetermined.
class CheckOrderListener(listsListener):
    def __init__(self):
        listsListener.__init__(self)
        self.highest = None
    def enterNumber(self, ctx):
        if self.highest == None or self.highest <= int(ctx.getText()):
            self.highest = int(ctx.getText())
        else:
            raise error.Errors.ParseCancellationException("Wrong order at (%d:%d): %d is smaller than %d" % (ctx.children[0].getSymbol().line, ctx.children[0].getSymbol().start, int(ctx.getText()), self.highest))

# ad hoc (DO NOT USE THIS IN YOUR COMPILER!)
def flatten(node):
    if node.__class__ == listsParser.NumberContext:
        print node.getText(), 
    elif node.getChildCount() > 0:
        for child in node.children:
            flatten(child)

# A listener
# When using a listener, the AST traversal is predetermined.
class FlattenListener(listsListener):
    def enterNumber(self, ctx):
        print ctx.getText(),

# A visitor
# When using a visitor, the AST traversal can be customized.
# By default, the visitChildren method is called (see listsVisitor.py).
class FlattenVisitor(listsVisitor):
    def visitNumber(self, ctx):
        print ctx.getText(),

if __name__ == '__main__':
    main('test.lists')
