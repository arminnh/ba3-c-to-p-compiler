# Generated from smallc.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .smallcParser import smallcParser
else:
    from smallcParser import smallcParser

# This class defines a complete generic visitor for a parse tree produced by smallcParser.

class smallcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by smallcParser#program.
    def visitProgram(self, ctx:smallcParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smallcParser#header.
    def visitHeader(self, ctx:smallcParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smallcParser#includes.
    def visitIncludes(self, ctx:smallcParser.IncludesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smallcParser#mainFunction.
    def visitMainFunction(self, ctx:smallcParser.MainFunctionContext):
        return self.visitChildren(ctx)



del smallcParser