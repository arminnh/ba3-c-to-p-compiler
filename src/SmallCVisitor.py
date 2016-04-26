# Generated from SmallC.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallCParser import SmallCParser
else:
    from SmallCParser import SmallCParser

# This class defines a complete generic visitor for a parse tree produced by SmallCParser.

class SmallCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmallCParser#oplevel15.
    def visitOplevel15(self, ctx:SmallCParser.Oplevel15Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel14.
    def visitOplevel14(self, ctx:SmallCParser.Oplevel14Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel13.
    def visitOplevel13(self, ctx:SmallCParser.Oplevel13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel12.
    def visitOplevel12(self, ctx:SmallCParser.Oplevel12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel11.
    def visitOplevel11(self, ctx:SmallCParser.Oplevel11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel10.
    def visitOplevel10(self, ctx:SmallCParser.Oplevel10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel9.
    def visitOplevel9(self, ctx:SmallCParser.Oplevel9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel8.
    def visitOplevel8(self, ctx:SmallCParser.Oplevel8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel7.
    def visitOplevel7(self, ctx:SmallCParser.Oplevel7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel6.
    def visitOplevel6(self, ctx:SmallCParser.Oplevel6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel5.
    def visitOplevel5(self, ctx:SmallCParser.Oplevel5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel4.
    def visitOplevel4(self, ctx:SmallCParser.Oplevel4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel3.
    def visitOplevel3(self, ctx:SmallCParser.Oplevel3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel2.
    def visitOplevel2(self, ctx:SmallCParser.Oplevel2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#oplevel1.
    def visitOplevel1(self, ctx:SmallCParser.Oplevel1Context):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by SmallCParser#functions.
    def visitFunctions(self, ctx:SmallCParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#parameters.
    def visitParameters(self, ctx:SmallCParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#parameter.
    def visitParameter(self, ctx:SmallCParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#arrayParameter.
    def visitArrayParameter(self, ctx:SmallCParser.ArrayParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#mainFunction.
    def visitMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#parametersMain.
    def visitParametersMain(self, ctx:SmallCParser.ParametersMainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#statements.
    def visitStatements(self, ctx:SmallCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#statement.
    def visitStatement(self, ctx:SmallCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#expression.
    def visitExpression(self, ctx:SmallCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#arguments.
    def visitArguments(self, ctx:SmallCParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#ifCond.
    def visitIfCond(self, ctx:SmallCParser.IfCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#elseCond.
    def visitElseCond(self, ctx:SmallCParser.ElseCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#whileCond.
    def visitWhileCond(self, ctx:SmallCParser.WhileCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#doWhileCond.
    def visitDoWhileCond(self, ctx:SmallCParser.DoWhileCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:SmallCParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#cvQualifier.
    def visitCvQualifier(self, ctx:SmallCParser.CvQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#declaratorInitializer.
    def visitDeclaratorInitializer(self, ctx:SmallCParser.DeclaratorInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:SmallCParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#returnExpression.
    def visitReturnExpression(self, ctx:SmallCParser.ReturnExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#functionCall.
    def visitFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#variable.
    def visitVariable(self, ctx:SmallCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#textLiteral.
    def visitTextLiteral(self, ctx:SmallCParser.TextLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#numberLiteral.
    def visitNumberLiteral(self, ctx:SmallCParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#identifier.
    def visitIdentifier(self, ctx:SmallCParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#pointer.
    def visitPointer(self, ctx:SmallCParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#reference.
    def visitReference(self, ctx:SmallCParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#floatLiteral.
    def visitFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#characterLiteral.
    def visitCharacterLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallCParser#stringLiteral.
    def visitStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        return self.visitChildren(ctx)



del SmallCParser