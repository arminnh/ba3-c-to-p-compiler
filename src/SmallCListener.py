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


    # Enter a parse tree produced by SmallCParser#statements.
    def enterStatements(self, ctx:SmallCParser.StatementsContext):
        pass

    # Exit a parse tree produced by SmallCParser#statements.
    def exitStatements(self, ctx:SmallCParser.StatementsContext):
        pass


    # Enter a parse tree produced by SmallCParser#statement.
    def enterStatement(self, ctx:SmallCParser.StatementContext):
        pass

    # Exit a parse tree produced by SmallCParser#statement.
    def exitStatement(self, ctx:SmallCParser.StatementContext):
        pass


    # Enter a parse tree produced by SmallCParser#statementBody.
    def enterStatementBody(self, ctx:SmallCParser.StatementBodyContext):
        pass

    # Exit a parse tree produced by SmallCParser#statementBody.
    def exitStatementBody(self, ctx:SmallCParser.StatementBodyContext):
        pass


    # Enter a parse tree produced by SmallCParser#expression.
    def enterExpression(self, ctx:SmallCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SmallCParser#expression.
    def exitExpression(self, ctx:SmallCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SmallCParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#variable.
    def enterVariable(self, ctx:SmallCParser.VariableContext):
        pass

    # Exit a parse tree produced by SmallCParser#variable.
    def exitVariable(self, ctx:SmallCParser.VariableContext):
        pass


    # Enter a parse tree produced by SmallCParser#arithmeticop.
    def enterArithmeticop(self, ctx:SmallCParser.ArithmeticopContext):
        pass

    # Exit a parse tree produced by SmallCParser#arithmeticop.
    def exitArithmeticop(self, ctx:SmallCParser.ArithmeticopContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SmallCParser#mainFunction.
    def enterMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by SmallCParser#mainFunction.
    def exitMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by SmallCParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionCall.
    def enterFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SmallCParser#functionCall.
    def exitFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SmallCParser#arguments.
    def enterArguments(self, ctx:SmallCParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by SmallCParser#arguments.
    def exitArguments(self, ctx:SmallCParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by SmallCParser#argument.
    def enterArgument(self, ctx:SmallCParser.ArgumentContext):
        pass

    # Exit a parse tree produced by SmallCParser#argument.
    def exitArgument(self, ctx:SmallCParser.ArgumentContext):
        pass


    # Enter a parse tree produced by SmallCParser#floatLiteral.
    def enterFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by SmallCParser#floatLiteral.
    def exitFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by SmallCParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SmallCParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SmallCParser#stringLiteral.
    def enterStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SmallCParser#stringLiteral.
    def exitStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SmallCParser#identifier.
    def enterIdentifier(self, ctx:SmallCParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#identifier.
    def exitIdentifier(self, ctx:SmallCParser.IdentifierContext):
        pass


