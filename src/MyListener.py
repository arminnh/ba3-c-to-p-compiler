from SmallCListener import SmallCListener
from SmallCParser import SmallCParser
from AbstractSyntaxTree import *


class MyListener(SmallCListener):
    def __init__(self, tree:AbstractSyntaxTree):
        super(MyListener, self).__init__()
        self.ast = tree
        self.currentNode = self.ast.root
        self.nodes = {}

    def enterProgram(self, ctx:SmallCParser.ProgramContext):
        self.currentNode = self.currentNode.addChild("program")
        return

    def exitProgram(self, ctx:SmallCParser.ProgramContext):
        return


    def enterHeader(self, ctx:SmallCParser.ProgramContext):
        self.currentNode = self.currentNode.addChild("header")
        return

    # Exit a parse tree produced by SmallCParser#header.
    def exitHeader(self, ctx:SmallCParser.HeaderContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#include.
    def enterInclude(self, ctx:SmallCParser.IncludeContext):
        self.currentNode = self.currentNode.addChild("include")
        pass

    # Exit a parse tree produced by SmallCParser#include.
    def exitInclude(self, ctx:SmallCParser.IncludeContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#stdInclude.
    def enterStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        self.currentNode = self.currentNode.addChild("stdInclude")
        pass

    # Exit a parse tree produced by SmallCParser#stdInclude.
    def exitStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#customInclude.
    def enterCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        self.currentNode = self.currentNode.addChild("customInclude")
        pass

    # Exit a parse tree produced by SmallCParser#customInclude.
    def exitCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#statements.
    def enterStatements(self, ctx:SmallCParser.StatementsContext):
        self.currentNode = self.currentNode.addChild("statements")
        pass

    # Exit a parse tree produced by SmallCParser#statements.
    def exitStatements(self, ctx:SmallCParser.StatementsContext):
        self.currentNode = self.currentNode.parent
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
        self.currentNode = self.currentNode.addChild("expression")
        pass

    # Exit a parse tree produced by SmallCParser#expression.
    def exitExpression(self, ctx:SmallCParser.ExpressionContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#expression.
    def enterReturnExpression(self, ctx:SmallCParser.ExpressionContext):
        self.currentNode = self.currentNode.addChild("returnExpression")
        pass

    # Exit a parse tree produced by SmallCParser#expression.
    def exitReturnExpression(self, ctx:SmallCParser.ExpressionContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel15.
    def enterOplevel15(self, ctx:SmallCParser.Oplevel15Context):
        self.currentNode = self.currentNode.addChild("oplevel15")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel15.
    def exitOplevel15(self, ctx:SmallCParser.Oplevel15Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel14.
    def enterOplevel14(self, ctx:SmallCParser.Oplevel14Context):
        self.currentNode = self.currentNode.addChild("oplevel14")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel14.
    def exitOplevel14(self, ctx:SmallCParser.Oplevel14Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel13.
    def enterOplevel13(self, ctx:SmallCParser.Oplevel13Context):
        self.currentNode = self.currentNode.addChild("oplevel13")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel13.
    def exitOplevel13(self, ctx:SmallCParser.Oplevel13Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel12.
    def enterOplevel12(self, ctx:SmallCParser.Oplevel12Context):
        self.currentNode = self.currentNode.addChild("oplevel12")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel12.
    def exitOplevel12(self, ctx:SmallCParser.Oplevel12Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel11.
    def enterOplevel11(self, ctx:SmallCParser.Oplevel11Context):
        self.currentNode = self.currentNode.addChild("oplevel11")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel11.
    def exitOplevel11(self, ctx:SmallCParser.Oplevel11Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel10.
    def enterOplevel10(self, ctx:SmallCParser.Oplevel10Context):
        self.currentNode = self.currentNode.addChild("oplevel10")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel10.
    def exitOplevel10(self, ctx:SmallCParser.Oplevel10Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel9.
    def enterOplevel9(self, ctx:SmallCParser.Oplevel9Context):
        self.currentNode = self.currentNode.addChild("oplevel9")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel9.
    def exitOplevel9(self, ctx:SmallCParser.Oplevel9Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel8.
    def enterOplevel8(self, ctx:SmallCParser.Oplevel8Context):
        self.currentNode = self.currentNode.addChild("oplevel8")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel8.
    def exitOplevel8(self, ctx:SmallCParser.Oplevel8Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel7.
    def enterOplevel7(self, ctx:SmallCParser.Oplevel7Context):
        self.currentNode = self.currentNode.addChild("oplevel7")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel7.
    def exitOplevel7(self, ctx:SmallCParser.Oplevel7Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel6.
    def enterOplevel6(self, ctx:SmallCParser.Oplevel6Context):
        self.currentNode = self.currentNode.addChild("oplevel6")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel6.
    def exitOplevel6(self, ctx:SmallCParser.Oplevel6Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel5.
    def enterOplevel5(self, ctx:SmallCParser.Oplevel5Context):
        self.currentNode = self.currentNode.addChild("oplevel5")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel5.
    def exitOplevel5(self, ctx:SmallCParser.Oplevel5Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel4.
    def enterOplevel4(self, ctx:SmallCParser.Oplevel4Context):
        self.currentNode = self.currentNode.addChild("oplevel4")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel4.
    def exitOplevel4(self, ctx:SmallCParser.Oplevel4Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel3.
    def enterOplevel3(self, ctx:SmallCParser.Oplevel3Context):
        self.currentNode = self.currentNode.addChild("oplevel3")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel3.
    def exitOplevel3(self, ctx:SmallCParser.Oplevel3Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel2.
    def enterOplevel2(self, ctx:SmallCParser.Oplevel2Context):
        self.currentNode = self.currentNode.addChild("oplevel2")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel2.
    def exitOplevel2(self, ctx:SmallCParser.Oplevel2Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#oplevel1.
    def enterOplevel1(self, ctx:SmallCParser.Oplevel1Context):
        self.currentNode = self.currentNode.addChild("oplevel1")
        pass

    # Exit a parse tree produced by SmallCParser#oplevel1.
    def exitOplevel1(self, ctx:SmallCParser.Oplevel1Context):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        self.currentNode = self.currentNode.addChild("variableDeclaration")
        pass

    # Exit a parse tree produced by SmallCParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#variable.
    def enterVariable(self, ctx:SmallCParser.VariableContext):
        self.currentNode = self.currentNode.addChild("variable")
        pass

    # Exit a parse tree produced by SmallCParser#variable.
    def exitVariable(self, ctx:SmallCParser.VariableContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        self.currentNode = self.currentNode.addChild("functionDeclaration")
        pass

    # Exit a parse tree produced by SmallCParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        self.currentNode = self.currentNode.addChild("functionDefinition")
        pass

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#mainFunction.
    def enterMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        self.currentNode = self.currentNode.addChild("mainFunction")
        return

    # Exit a parse tree produced by SmallCParser#mainFunction.
    def exitMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        self.currentNode = self.currentNode.parent
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        self.currentNode = self.currentNode.addChild("typeDeclaration")
        self.currentNode.addChild("\"" + ctx.getText() + "\"")
        pass

    # Exit a parse tree produced by SmallCParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#functionCall.
    def enterFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        self.currentNode = self.currentNode.addChild("functionCall")
        pass

    # Exit a parse tree produced by SmallCParser#functionCall.
    def exitFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#arguments.
    def enterArguments(self, ctx:SmallCParser.ArgumentsContext):
        self.currentNode = self.currentNode.addChild("arguments")
        pass

    # Exit a parse tree produced by SmallCParser#arguments.
    def exitArguments(self, ctx:SmallCParser.ArgumentsContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#argument.
    def enterArgument(self, ctx:SmallCParser.ArgumentContext):
        pass

    # Exit a parse tree produced by SmallCParser#argument.
    def exitArgument(self, ctx:SmallCParser.ArgumentContext):
        pass


    # Enter a parse tree produced by SmallCParser#floatLiteral.
    def enterFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        self.currentNode = self.currentNode.addChild("floatLiteral")
        self.currentNode.addChild(ctx.getText())
        pass

    # Exit a parse tree produced by SmallCParser#floatLiteral.
    def exitFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        self.currentNode = self.currentNode.addChild("integerLiteral")
        self.currentNode.addChild(ctx.getText())
        pass

    # Exit a parse tree produced by SmallCParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#numberLiteral.
    def enterNumberLiteral(self, ctx:SmallCParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by SmallCParser#numberLiteral.
    def exitNumberLiteral(self, ctx:SmallCParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by SmallCParser#characterLiteral.
    def enterCharacterLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        self.currentNode = self.currentNode.addChild("characterLiteral")
        self.currentNode.addChild("\"" + ctx.getText() + "\"")
        pass

    # Exit a parse tree produced by SmallCParser#characterLiteral.
    def exitCharacterLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#stringLiteral.
    def enterStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        self.currentNode = self.currentNode.addChild("stringLiteral")
        self.currentNode.addChild("\"" + ctx.getText() + "\"")
        pass

    # Exit a parse tree produced by SmallCParser#stringLiteral.
    def exitStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#characterLiteral.
    def enterTextLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        pass

    # Exit a parse tree produced by SmallCParser#characterLiteral.
    def exitTextLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        pass


    # Enter a parse tree produced by SmallCParser#identifier.
    def enterIdentifier(self, ctx:SmallCParser.IdentifierContext):
        self.currentNode = self.currentNode.addChild("identifier")
        self.currentNode.addChild("\"" + ctx.getText() + "\"")
        pass

    # Exit a parse tree produced by SmallCParser#identifier.
    def exitIdentifier(self, ctx:SmallCParser.IdentifierContext):
        self.currentNode = self.currentNode.parent
        pass
