from SmallCListener import SmallCListener
from SmallCParser import SmallCParser
from AbstractSyntaxTree import *
from antlr4 import tree
from antlr4 import ParserRuleContext
import sys


class MyListener(SmallCListener):
    def __init__(self, tree):
        super(MyListener, self).__init__()
        self.ast = tree
        self.currentNode = self.ast.root
        self.createdNode = []

    def enterProgram(self, ctx:SmallCParser.ProgramContext):
        self.ast.root = ASTProgramNode()
        self.currentNode = self.ast.root

    def exitProgram(self, ctx:SmallCParser.ProgramContext):
        pass


    # Enter a parse tree produced by SmallCParser#stdInclude.
    def enterStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        self.currentNode = self.currentNode.addChildNode(ASTIncludeNode(True, ctx.getText()))

    # Exit a parse tree produced by SmallCParser#stdInclude.
    def exitStdInclude(self, ctx:SmallCParser.StdIncludeContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#customInclude.
    def enterCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        self.currentNode = self.currentNode.addChildNode(ASTIncludeNode(False, ctx.getText()[1:-1]))

    # Exit a parse tree produced by SmallCParser#customInclude.
    def exitCustomInclude(self, ctx:SmallCParser.CustomIncludeContext):
        self.currentNode.children = []
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#statements.
    def enterStatements(self, ctx:SmallCParser.StatementsContext):
        self.currentNode = self.currentNode.addChildNode(ASTStatementsNode())

    # Exit a parse tree produced by SmallCParser#statements.
    def exitStatements(self, ctx:SmallCParser.StatementsContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#statement.
    def enterStatement(self, ctx:SmallCParser.StatementContext):
        # self.currentNode = self.currentNode.addChildNode(ASTStatementNode())
        pass

    # Exit a parse tree produced by SmallCParser#statement.
    def exitStatement(self, ctx:SmallCParser.StatementContext):
        # self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#expression.
    def enterExpression(self, ctx:SmallCParser.ExpressionContext):
        # self.currentNode = self.currentNode.addChildNode(ASTExpressionNode())
        pass

    # Exit a parse tree produced by SmallCParser#expression.
    def exitExpression(self, ctx:SmallCParser.ExpressionContext):
        # self.currentNode = self.currentNode.parent
        pass


    # Enter a parse tree produced by SmallCParser#expression.
    def enterReturnStmt(self, ctx:SmallCParser.ExpressionContext):
        self.currentNode = self.currentNode.addChildNode(ASTReturnNode(ctx))

    # Exit a parse tree produced by SmallCParser#expression.
    def exitReturnStmt(self, ctx:SmallCParser.ExpressionContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        self.currentNode = self.currentNode.addChildNode(ASTVariableDeclarationNode())


    # Exit a parse tree produced by SmallCParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SmallCParser.VariableDeclarationContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:SmallCParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by SmallCParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:SmallCParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#cvQualifier.
    def enterCvQualifier(self, ctx:SmallCParser.CvQualifierContext):
        self.currentNode.isConstant = True

    # Exit a parse tree produced by SmallCParser#cvQualifier.
    def exitCvQualifier(self, ctx:SmallCParser.CvQualifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#declaratorInitializer.
    def enterDeclaratorInitializer(self, ctx:SmallCParser.DeclaratorInitializerContext):
        self.currentNode = self.currentNode.addChildNode(ASTDeclaratorInitializerNode(ctx))

    # Exit a parse tree produced by SmallCParser#declaratorInitializer.
    def exitDeclaratorInitializer(self, ctx:SmallCParser.DeclaratorInitializerContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#variable.
    def enterVariable(self, ctx:SmallCParser.VariableContext):
        self.currentNode = self.currentNode.addChildNode(ASTVariableNode(ctx.getText(), ctx))

    # Exit a parse tree produced by SmallCParser#variable.
    def exitVariable(self, ctx:SmallCParser.VariableContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        self.currentNode = self.currentNode.addChildNode(ASTFunctionDeclarationNode(ctx=ctx))

    # Exit a parse tree produced by SmallCParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:SmallCParser.FunctionDeclarationContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        child = ctx.getChild(0, SmallCParser.IdentifierContext)
        if child is not None and child.getText() == "main":
            self.currentNode = self.currentNode.addChildNode(ASTMainFunctionNode(ctx=ctx))
        else:
            self.currentNode = self.currentNode.addChildNode(ASTFunctionDefinitionNode(ctx=ctx))

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SmallCParser.FunctionDefinitionContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterParameters(self, ctx:SmallCParser.ParametersContext):
        self.currentNode = self.currentNode.addChildNode(ASTParametersNode())

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitParameters(self, ctx:SmallCParser.ParametersContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterParameter(self, ctx:SmallCParser.ParameterContext):
        self.currentNode = self.currentNode.addChildNode(ASTParameterNode(ctx=ctx))

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitParameter(self, ctx:SmallCParser.ParameterContext):
        self.currentNode.children = []
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#functionDefinition.
    def enterArrayPart(self, ctx:SmallCParser.ArrayPartContext):
        self.currentNode.isArray = True
        self.currentNode.indirections += 1

    # Exit a parse tree produced by SmallCParser#functionDefinition.
    def exitArrayPart(self, ctx:SmallCParser.ArrayPartContext):
        pass


    # Enter a parse tree produced by SmallCParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        self.currentNode.basetype = ctx.getText()

    # Exit a parse tree produced by SmallCParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:SmallCParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by SmallCParser#functionCall.
    def enterFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        self.currentNode = self.currentNode.addChildNode(ASTFunctionCallNode(ctx))

    # Exit a parse tree produced by SmallCParser#functionCall.
    def exitFunctionCall(self, ctx:SmallCParser.FunctionCallContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#arguments.
    def enterArguments(self, ctx:SmallCParser.ArgumentsContext):
        self.currentNode = self.currentNode.addChildNode(ASTArgumentsNode(ctx))

    # Exit a parse tree produced by SmallCParser#arguments.
    def exitArguments(self, ctx:SmallCParser.ArgumentsContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#initializer.
    def enterInitializer(self, ctx:SmallCParser.InitializerContext):
        self.currentNode = self.currentNode.addChildNode(ASTInitializerListNode(ctx))

    # Exit a parse tree produced by SmallCParser#initializer.
    def exitInitializer(self, ctx:SmallCParser.InitializerContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#ifCond.
    def enterIfCond(self, ctx:SmallCParser.IfCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTIfNode(ctx))

    # Exit a parse tree produced by SmallCParser#ifCond.
    def exitIfCond(self, ctx:SmallCParser.IfCondContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#elseCond.
    def enterElseCond(self, ctx:SmallCParser.ElseCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTElseNode(ctx))

    # Exit a parse tree produced by SmallCParser#elseCond.
    def exitElseCond(self, ctx:SmallCParser.ElseCondContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#whileCond.
    def enterWhileCond(self, ctx:SmallCParser.WhileCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTWhileNode(ctx))

    # Exit a parse tree produced by SmallCParser#whileCond.
    def exitWhileCond(self, ctx:SmallCParser.WhileCondContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#doWhileCond.
    def enterDoWhileCond(self, ctx:SmallCParser.DoWhileCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTDoWhileNode(ctx))

    # Exit a parse tree produced by SmallCParser#doWhileCond.
    def exitDoWhileCond(self, ctx:SmallCParser.DoWhileCondContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#floatLiteral.
    def enterFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTFloatLiteralNode(float(ctx.getText()), ctx))

    # Exit a parse tree produced by SmallCParser#floatLiteral.
    def exitFloatLiteral(self, ctx:SmallCParser.FloatLiteralContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTIntegerLiteralNode(int(ctx.getText()), ctx))

    # Exit a parse tree produced by SmallCParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SmallCParser.IntegerLiteralContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#characterLiteral.
    def enterCharacterLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTCharacterLiteralNode(ctx.getText(), ctx))

    # Exit a parse tree produced by SmallCParser#characterLiteral.
    def exitCharacterLiteral(self, ctx:SmallCParser.CharacterLiteralContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#stringLiteral.
    def enterStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTStringLiteralNode(ctx.getText(), ctx))

    # Exit a parse tree produced by SmallCParser#stringLiteral.
    def exitStringLiteral(self, ctx:SmallCParser.StringLiteralContext):
        self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#identifier.
    def enterIdentifier(self, ctx:SmallCParser.IdentifierContext):
        if hasattr(self.currentNode, "identifier"):
            self.currentNode.identifier = ctx.getText()

    # Exit a parse tree produced by SmallCParser#identifier.
    def exitIdentifier(self, ctx:SmallCParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SmallCParser#pointer.
    def enterPointer(self, ctx:SmallCParser.PointerContext):
        pass

    # Exit a parse tree produced by SmallCParser#pointer.
    def exitPointer(self, ctx:SmallCParser.PointerContext):
        pass

     # Enter a parse tree produced by SmallCParser#pointerPart.
    def enterPointerPart(self, ctx:SmallCParser.PointerPartContext):
        if hasattr(self.currentNode, "indirections"):
            self.currentNode.indirections += 1

        if hasattr(self.currentNode, "const"):
            if ctx.getChildCount() == 2:
                self.currentNode.const.append(True)
            else:
                self.currentNode.const.append(False)
        pass

    # Exit a parse tree produced by SmallCParser#pointerPart.
    def exitPointerPart(self, ctx:SmallCParser.PointerPartContext):
        pass


    # Enter a parse tree produced by SmallCParser#oplevel15.
    def enterOplevel15(self, ctx:SmallCParser.Oplevel15Context):
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel15.
    def exitOplevel15(self, ctx:SmallCParser.Oplevel15Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel14.
    def enterOplevel14(self, ctx:SmallCParser.Oplevel14Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if symbol == "=":
                self.currentNode = self.currentNode.addChildNode(ASTSimpleAssignmentOperatorNode(ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel14.
    def exitOplevel14(self, ctx:SmallCParser.Oplevel14Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel13.
    def enterOplevel13(self, ctx:SmallCParser.Oplevel13Context):
        children = list(ctx.getChildren())
        if len(children) == 5:
            symbol1 = children[1].getText()
            symbol2 = children[3].getText()
            if symbol1 == "?" and symbol2 == ":":
                self.currentNode = self.currentNode.addChildNode(ASTTernaryConditionalOperatorNode(ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel13.
    def exitOplevel13(self, ctx:SmallCParser.Oplevel13Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel12.
    def enterOplevel12(self, ctx:SmallCParser.Oplevel12Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if symbol == "||":
                self.currentNode = self.currentNode.addChildNode(ASTLogicOperatorNode(ASTLogicOperatorNode.LogicOperatorType['disj'], ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel12.
    def exitOplevel12(self, ctx:SmallCParser.Oplevel12Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel11.
    def enterOplevel11(self, ctx:SmallCParser.Oplevel11Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if symbol == "&&":
                self.currentNode = self.currentNode.addChildNode(ASTLogicOperatorNode(ASTLogicOperatorNode.LogicOperatorType['conj'], ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel11.
    def exitOplevel11(self, ctx:SmallCParser.Oplevel11Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel10.
    def enterOplevel10(self, ctx:SmallCParser.Oplevel10Context):
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel10.
    def exitOplevel10(self, ctx:SmallCParser.Oplevel10Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel9.
    def enterOplevel9(self, ctx:SmallCParser.Oplevel9Context):
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel9.
    def exitOplevel9(self, ctx:SmallCParser.Oplevel9Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel8.
    def enterOplevel8(self, ctx:SmallCParser.Oplevel8Context):
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel8.
    def exitOplevel8(self, ctx:SmallCParser.Oplevel8Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel7.
    def enterOplevel7(self, ctx:SmallCParser.Oplevel7Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getSymbol().text
            self.currentNode = self.currentNode.addChildNode(ASTComparisonOperatorNode( \
                ASTComparisonOperatorNode.ComparisonType['inequal'] if symbol == "!=" else ASTComparisonOperatorNode.ComparisonType['equal'], ctx))
            self.createdNode.append(True)
        else:
            self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel7.
    def exitOplevel7(self, ctx:SmallCParser.Oplevel7Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel6.
    def enterOplevel6(self, ctx:SmallCParser.Oplevel6Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getSymbol().text
            if symbol in ["<", ">", "<=", ">="]:
                comparisonType = None
                if symbol == "<": comparisonType = ASTComparisonOperatorNode.ComparisonType['lt']
                elif symbol == ">": comparisonType = ASTComparisonOperatorNode.ComparisonType['gt']
                elif symbol == "<=": comparisonType = ASTComparisonOperatorNode.ComparisonType['le']
                elif symbol == ">=": comparisonType = ASTComparisonOperatorNode.ComparisonType['ge']
                self.currentNode = self.currentNode.addChildNode(ASTComparisonOperatorNode(comparisonType, ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel6.
    def exitOplevel6(self, ctx:SmallCParser.Oplevel6Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel5.
    def enterOplevel5(self, ctx:SmallCParser.Oplevel5Context):
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel5.
    def exitOplevel5(self, ctx:SmallCParser.Oplevel5Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel4.
    def enterOplevel4(self, ctx:SmallCParser.Oplevel4Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if self.addBinaryArithmeticOperator(symbol, ctx):
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel4.
    def exitOplevel4(self, ctx:SmallCParser.Oplevel4Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent

    def addBinaryArithmeticOperator(self, symbol, ctx):
        arithmeticType = None
        if symbol == "+": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType['add']
        elif symbol == "-": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType['sub']
        elif symbol == "*": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType['mul']
        elif symbol == "/": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType['div']
        elif symbol == "%": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType['remainder']
        else: return False
        self.currentNode = self.currentNode.addChildNode(ASTBinaryArithmeticOperatorNode(arithmeticType, ctx))
        return True

    # Enter a parse tree produced by SmallCParser#oplevel3.
    def enterOplevel3(self, ctx:SmallCParser.Oplevel3Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if self.addBinaryArithmeticOperator(symbol, ctx):
                self.createdNode.append(True)
                return
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel3.
    def exitOplevel3(self, ctx:SmallCParser.Oplevel3Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel2.
    def enterOplevel2(self, ctx:SmallCParser.Oplevel2Context):
        children = list(ctx.getChildren())
        if len(children) == 2:
            symbol = children[0].getText()
            if   symbol == "++": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType['increment'], ASTUnaryOperatorNode.Type['prefix'], ctx))
            elif symbol == "--": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement'], ASTUnaryOperatorNode.Type['prefix'], ctx))
            elif symbol == "+":  self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType['plus'], ASTUnaryOperatorNode.Type['prefix'], ctx))
            elif symbol == "-":  self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType['minus'], ASTUnaryOperatorNode.Type['prefix'], ctx))
            elif symbol == "&":  self.currentNode = self.currentNode.addChildNode(ASTAddressOfOperatorNode(ctx))
            elif symbol == "*":  self.currentNode = self.currentNode.addChildNode(ASTDereferenceOperatorNode(ctx))
            elif symbol == "!":  self.currentNode = self.currentNode.addChildNode(ASTLogicalNotOperatorNode(ctx))
            else:
                self.createdNode.append(False)
                return;
            self.createdNode.append(True)
            return
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel2.
    def exitOplevel2(self, ctx:SmallCParser.Oplevel2Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent


    # Enter a parse tree produced by SmallCParser#oplevel1.
    def enterOplevel1(self, ctx:SmallCParser.Oplevel1Context):
        children = list(ctx.getChildren())
        if len(children) == 2:
            symbol = children[1].getText()
            if symbol == "++": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType['increment'], ASTUnaryOperatorNode.Type['postfix'], ctx))
            elif symbol == "--": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement'], ASTUnaryOperatorNode.Type['postfix'], ctx))
            self.createdNode.append(True)
            return
        elif len(children) == 4:
            symbol1 = children[1].getText()
            symbol2 = children[3].getText()
            if symbol1 == "[" and symbol2 == "]":
                self.currentNode = self.currentNode.addChildNode(ASTArraySubscriptNode(ctx))
                self.createdNode.append(True)
                return
        self.createdNode.append(False)

    # Exit a parse tree produced by SmallCParser#oplevel1.
    def exitOplevel1(self, ctx:SmallCParser.Oplevel1Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent
