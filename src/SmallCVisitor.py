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


    # Visit a parse tree produced by SmallCParser#statements.
    def visitStatements(self, ctx:SmallCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#statement.
    def visitStatement(self, ctx:SmallCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#statementBody.
    def visitStatementBody(self, ctx:SmallCParser.StatementBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#expression.
    def visitExpression(self, ctx:SmallCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#variable.
    def visitVariable(self, ctx:SmallCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#arithmeticop.
    def visitArithmeticop(self, ctx:SmallCParser.ArithmeticopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#mainFunction.
    def visitMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionCall.
    def visitFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#arguments.
    def visitArguments(self, ctx:SmallCParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#argument.
    def visitArgument(self, ctx:SmallCParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#floatLiteral.
    def visitFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#stringLiteral.
    def visitStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#identifier.
    def visitIdentifier(self, ctx:SmallCParser.IdentifierContext):
        return self.visitChildren(ctx)



del SmallCParser