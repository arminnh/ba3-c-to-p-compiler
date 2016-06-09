# Generated from NestedLists.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NestedListsParser import NestedListsParser
else:
    from NestedListsParser import NestedListsParser

# This class defines a complete generic visitor for a parse tree produced by NestedListsParser.

class NestedListsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NestedListsParser#nstdlst.
    def visitNstdlst(self, ctx:NestedListsParser.NstdlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NestedListsParser#lst.
    def visitLst(self, ctx:NestedListsParser.LstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NestedListsParser#itm.
    def visitItm(self, ctx:NestedListsParser.ItmContext):
        return self.visitChildren(ctx)



del NestedListsParser