# Generated from SmallC.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallCParser import SmallCParser
else:
    from SmallCParser import SmallCParser

# This class defines a complete listener for a parse tree produced by SmallCParser.
class SmallCListener(ParseTreeListener):

    # Enter a parse tree produced by SmallCParser#program.
    def enterProgram(self, ctx:SmallCParser.ProgramContext):
        pass

    # Exit a parse tree produced by SmallCParser#program.
    def exitProgram(self, ctx:SmallCParser.ProgramContext):
        pass


    # Enter a parse tree produced by SmallCParser#header.
    def enterHeader(self, ctx:SmallCParser.HeaderContext):
        pass

    # Exit a parse tree produced by SmallCParser#header.
    def exitHeader(self, ctx:SmallCParser.HeaderContext):
        pass


    # Enter a parse tree produced by SmallCParser#include.
    def enterInclude(self, ctx:SmallCParser.IncludeContext):
        pass

    # Exit a parse tree produced by SmallCParser#include.
    def exitInclude(self, ctx:SmallCParser.IncludeContext):
        pass


    # Enter a parse tree produced by SmallCParser#stdInclude.
    def enterStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        pass

    # Exit a parse tree produced by SmallCParser#stdInclude.
    def exitStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        pass


    # Enter a parse tree produced by SmallCParser#customInclude.
    def enterCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        pass

    # Exit a parse tree produced by SmallCParser#customInclude.
    def exitCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        pass


    # Enter a parse tree produced by SmallCParser#mainFunction.
    def enterMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by SmallCParser#mainFunction.
    def exitMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeDecl.
    def enterTypeDecl(self, ctx:SmallCParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by SmallCParser#typeDecl.
    def exitTypeDecl(self, ctx:SmallCParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionBody.
    def enterFunctionBody(self, ctx:SmallCParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by SmallCParser#functionBody.
    def exitFunctionBody(self, ctx:SmallCParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by SmallCParser#number.
    def enterNumber(self, ctx:SmallCParser.NumberContext):
        pass

    # Exit a parse tree produced by SmallCParser#number.
    def exitNumber(self, ctx:SmallCParser.NumberContext):
        pass


