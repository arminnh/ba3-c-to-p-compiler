# Generated from lists.g4 by ANTLR 4.5.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by listsParser.

class listsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by listsParser#lst.
    def visitLst(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by listsParser#seq.
    def visitSeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by listsParser#item.
    def visitItem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by listsParser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


