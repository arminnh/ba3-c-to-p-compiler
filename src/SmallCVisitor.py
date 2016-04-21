# Generated from SmallC.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallCParser import SmallCParser
else:
    from SmallCParser import SmallCParser

# This class defines a complete generic visitor for a parse tree produced by SmallCParser.

class SmallCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmallCParser#program.
    def visitProgram(self, ctx:SmallCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#header.
    def visitHeader(self, ctx:SmallCParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#include.
    def visitInclude(self, ctx:SmallCParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#stdInclude.
    def visitStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#customInclude.
    def visitCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#mainFunction.
    def visitMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeDecl.
    def visitTypeDecl(self, ctx:SmallCParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionBody.
    def visitFunctionBody(self, ctx:SmallCParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#number.
    def visitNumber(self, ctx:SmallCParser.NumberContext):
        return self.visitChildren(ctx)



del SmallCParser