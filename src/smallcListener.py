# Generated from smallc.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .smallcParser import smallcParser
else:
    from smallcParser import smallcParser

# This class defines a complete listener for a parse tree produced by smallcParser.
class smallcListener(ParseTreeListener):

    # Enter a parse tree produced by smallcParser#program.
    def enterProgram(self, ctx:smallcParser.ProgramContext):
        pass

    # Exit a parse tree produced by smallcParser#program.
    def exitProgram(self, ctx:smallcParser.ProgramContext):
        pass


    # Enter a parse tree produced by smallcParser#header.
    def enterHeader(self, ctx:smallcParser.HeaderContext):
        pass

    # Exit a parse tree produced by smallcParser#header.
    def exitHeader(self, ctx:smallcParser.HeaderContext):
        pass


    # Enter a parse tree produced by smallcParser#includes.
    def enterIncludes(self, ctx:smallcParser.IncludesContext):
        pass

    # Exit a parse tree produced by smallcParser#includes.
    def exitIncludes(self, ctx:smallcParser.IncludesContext):
        pass


    # Enter a parse tree produced by smallcParser#mainFunction.
    def enterMainFunction(self, ctx:smallcParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by smallcParser#mainFunction.
    def exitMainFunction(self, ctx:smallcParser.MainFunctionContext):
        pass


