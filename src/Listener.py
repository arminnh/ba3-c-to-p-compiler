from antlr4_generated.CListener import CListener
from antlr4_generated.CParser import CParser
from AbstractSyntaxTree import *
from antlr4 import tree
from antlr4 import ParserRuleContext
import sys


class Listener(CListener):
    def __init__(self, tree):
        super(Listener, self).__init__()
        self.ast = tree
        self.currentNode = self.ast.root
        self.createdNode = []


    def enterProgram(self, ctx:CParser.ProgramContext):
        self.ast.root = ASTProgramNode()
        self.currentNode = self.ast.root

    def exitProgram(self, ctx:CParser.ProgramContext):
        pass



    def enterStdInclude(self, ctx:CParser.StdIncludeContext):
        self.currentNode = self.currentNode.addChildNode(ASTIncludeNode(True, ctx.getText()))

    def exitStdInclude(self, ctx:CParser.StdIncludeContext):
        self.currentNode = self.currentNode.parent



    def enterCustomInclude(self, ctx:CParser.CustomIncludeContext):
        self.currentNode = self.currentNode.addChildNode(ASTIncludeNode(False, ctx.getText()[1:-1]))

    def exitCustomInclude(self, ctx:CParser.CustomIncludeContext):
        self.currentNode.children = []
        self.currentNode = self.currentNode.parent



    def enterStatements(self, ctx:CParser.StatementsContext):
        self.currentNode = self.currentNode.addChildNode(ASTStatementsNode())

    def exitStatements(self, ctx:CParser.StatementsContext):
        self.currentNode = self.currentNode.parent



    def enterStatement(self, ctx:CParser.StatementContext):
        self.currentNode = self.currentNode.addChildNode(ASTStatementNode(ctx=ctx))

    def exitStatement(self, ctx:CParser.StatementContext):
        self.currentNode = self.currentNode.parent



    def enterReturnStmt(self, ctx:CParser.ReturnStmtContext):
        self.currentNode = self.currentNode.addChildNode(ASTReturnNode(ctx))

    def exitReturnStmt(self, ctx:CParser.ReturnStmtContext):
        self.currentNode = self.currentNode.parent



    def enterBreakStmt(self, ctx:CParser.BreakStmtContext):
        self.currentNode = self.currentNode.addChildNode(ASTBreakNode(ctx))

    def exitBreakStmt(self, ctx:CParser.BreakStmtContext):
        self.currentNode = self.currentNode.parent



    def enterContinueStmt(self, ctx:CParser.ContinueStmtContext):
        self.currentNode = self.currentNode.addChildNode(ASTContinueNode(ctx))

    def exitContinueStmt(self, ctx:CParser.ContinueStmtContext):
        self.currentNode = self.currentNode.parent



    def enterVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        self.currentNode = self.currentNode.addChildNode(ASTVariableDeclarationNode())


    def exitVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        self.currentNode = self.currentNode.parent



    def enterDeclarationSpecifier(self, ctx:CParser.DeclarationSpecifierContext):
        pass

    def exitDeclarationSpecifier(self, ctx:CParser.DeclarationSpecifierContext):
        pass



    def enterCvQualifier(self, ctx:CParser.CvQualifierContext):
        self.currentNode.isConstant = True

    def exitCvQualifier(self, ctx:CParser.CvQualifierContext):
        pass



    def enterDeclarator1(self, ctx:CParser.Declarator1Context):
        children = list(ctx.getChildren())
        for child in children:
            if isinstance(child, CParser.PointerPartContext):
                self.currentNode.indirections.append((False, child.getChildCount() == 2)) # if child count == 2, there is a const node
        for i in range(len(children) - 1, -1, -1):
            if isinstance(children[i], CParser.ArrayPartContext):
                self.currentNode.indirections.append((True, False))



    def exitDeclarator1(self, ctx:CParser.Declarator1Context):
        children = list(ctx.getChildren())



    def enterDeclaratorInitializer(self, ctx:CParser.DeclaratorInitializerContext):
        self.currentNode = self.currentNode.addChildNode(ASTDeclaratorInitializerNode(ctx))

    def exitDeclaratorInitializer(self, ctx:CParser.DeclaratorInitializerContext):
        self.currentNode = self.currentNode.parent



    def enterVariable(self, ctx:CParser.VariableContext):
        self.currentNode = self.currentNode.addChildNode(ASTVariableNode(ctx.getText(), ctx))

    def exitVariable(self, ctx:CParser.VariableContext):
        self.currentNode = self.currentNode.parent



    def enterFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        self.currentNode = self.currentNode.addChildNode(ASTFunctionDeclarationNode(ctx=ctx))

    def exitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        self.currentNode = self.currentNode.parent



    def enterFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        child = ctx.getChild(0, CParser.IdentifierContext)
        if child is not None and child.getText() == "main":
            self.currentNode = self.currentNode.addChildNode(ASTMainFunctionNode(ctx=ctx))
        else:
            self.currentNode = self.currentNode.addChildNode(ASTFunctionDefinitionNode(ctx=ctx))

    def exitFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        self.currentNode = self.currentNode.parent



    def enterParameters(self, ctx:CParser.ParametersContext):
        self.currentNode = self.currentNode.addChildNode(ASTParametersNode())

    def exitParameters(self, ctx:CParser.ParametersContext):
        self.currentNode = self.currentNode.parent



    def enterParameter(self, ctx:CParser.ParameterContext):
        self.currentNode = self.currentNode.addChildNode(ASTParameterNode(ctx=ctx))

    def exitParameter(self, ctx:CParser.ParameterContext):
        self.currentNode.children = []
        self.currentNode = self.currentNode.parent



    def enterParamDeclarator1(self, ctx:CParser.ParamDeclaratorContext):
        self.enterDeclarator1(ctx)

    def exitParamDeclarator1(self, ctx:CParser.ParamDeclaratorContext):
        self.exitDeclarator1(ctx)



    def enterArrayPart(self, ctx:CParser.ArrayPartContext):
        newNode = ASTArrayPartNode(ctx=ctx)
        self.currentNode.arrayLengths.append(newNode)
        self.currentNode = self.currentNode.addChildNode(newNode)

    def exitArrayPart(self, ctx:CParser.ArrayPartContext):
        self.currentNode = self.currentNode.parent



    def enterTypeDeclaration(self, ctx:CParser.TypeDeclarationContext):
        self.currentNode.baseType = ctx.getText()
        self.currentNode.typeSpecifierPresent = True

    def exitTypeDeclaration(self, ctx:CParser.TypeDeclarationContext):
        pass



    def enterFunctionCall(self, ctx:CParser.FunctionCallContext):
        self.currentNode = self.currentNode.addChildNode(ASTFunctionCallNode(ctx))

    def exitFunctionCall(self, ctx:CParser.FunctionCallContext):
        self.currentNode = self.currentNode.parent



    def enterArguments(self, ctx:CParser.ArgumentsContext):
        self.currentNode = self.currentNode.addChildNode(ASTArgumentsNode(ctx))

    def exitArguments(self, ctx:CParser.ArgumentsContext):
        self.currentNode = self.currentNode.parent



    def enterArrayInitializer(self, ctx:CParser.ArrayInitializerContext):
        self.currentNode = self.currentNode.addChildNode(ASTInitializerListNode(ctx))
        self.currentNode.isArray = True

    def exitArrayInitializer(self, ctx:CParser.ArrayInitializerContext):
        self.currentNode = self.currentNode.parent



    def enterExpressionInitializer(self, ctx:CParser.ExpressionInitializerContext):
        self.currentNode = self.currentNode.addChildNode(ASTInitializerListNode(ctx))

    def exitExpressionInitializer(self, ctx:CParser.ExpressionInitializerContext):
        self.currentNode = self.currentNode.parent



    def enterIfCond(self, ctx:CParser.IfCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTIfNode(ctx))

    def exitIfCond(self, ctx:CParser.IfCondContext):
        self.currentNode = self.currentNode.parent



    def enterElseCond(self, ctx:CParser.ElseCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTElseNode(ctx))

    def exitElseCond(self, ctx:CParser.ElseCondContext):
        self.currentNode = self.currentNode.parent



    def enterForLoop(self, ctx:CParser.ForLoopContext):
        self.currentNode = self.currentNode.addChildNode(ASTForNode(ctx))

    def exitForLoop(self, ctx:CParser.ForLoopContext):
        self.currentNode = self.currentNode.parent



    def enterForLoopInitStatement(self, ctx:CParser.ForLoopInitStatementContext):
        self.currentNode = self.currentNode.dummies[0]

    def exitForLoopInitStatement(self, ctx:CParser.ForLoopInitStatementContext):
        if self.currentNode.children:
            self.currentNode.parent.initializer = self.currentNode.children[0]
            self.currentNode.parent.initializer.parent = self.currentNode.parent
        self.currentNode = self.currentNode.parent



    def enterForLoopCondition(self, ctx:CParser.ForLoopConditionContext):
        self.currentNode = self.currentNode.dummies[1]

    def exitForLoopCondition(self, ctx:CParser.ForLoopConditionContext):
        if self.currentNode.children:
            self.currentNode.parent.condition = self.currentNode.children[0]
            self.currentNode.parent.condition.parent = self.currentNode.parent
        self.currentNode = self.currentNode.parent



    def enterForLoopIterationExpression(self, ctx:CParser.ForLoopIterationExpressionContext):
        self.currentNode = self.currentNode.dummies[2]

    def exitForLoopIterationExpression(self, ctx:CParser.ForLoopIterationExpressionContext):
        if self.currentNode.children:
            self.currentNode.parent.iteration = self.currentNode.children[0]
            self.currentNode.parent.iteration.parent = self.currentNode.parent
        self.currentNode = self.currentNode.parent



    def enterWhileCond(self, ctx:CParser.WhileCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTWhileNode(ctx))

    def exitWhileCond(self, ctx:CParser.WhileCondContext):
        self.currentNode = self.currentNode.parent



    def enterDoWhileCond(self, ctx:CParser.DoWhileCondContext):
        self.currentNode = self.currentNode.addChildNode(ASTDoWhileNode(ctx))

    def exitDoWhileCond(self, ctx:CParser.DoWhileCondContext):
        self.currentNode = self.currentNode.parent



    def enterFloatLiteral(self, ctx:CParser.FloatLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTFloatLiteralNode(float(ctx.getText()), ctx))

    def exitFloatLiteral(self, ctx:CParser.FloatLiteralContext):
        self.currentNode = self.currentNode.parent



    def enterIntegerLiteral(self, ctx:CParser.IntegerLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTIntegerLiteralNode(int(ctx.getText()), ctx))

    def exitIntegerLiteral(self, ctx:CParser.IntegerLiteralContext):
        self.currentNode = self.currentNode.parent



    def enterCharacterLiteral(self, ctx:CParser.CharacterLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTCharacterLiteralNode(ctx.getText(), ctx))

    def exitCharacterLiteral(self, ctx:CParser.CharacterLiteralContext):
        self.currentNode = self.currentNode.parent



    def enterStringLiteral(self, ctx:CParser.StringLiteralContext):
        self.currentNode = self.currentNode.addChildNode(ASTStringLiteralNode(ctx.getText()[1:-1], ctx))

    def exitStringLiteral(self, ctx:CParser.StringLiteralContext):
        self.currentNode = self.currentNode.parent



    def enterIdentifier(self, ctx:CParser.IdentifierContext):
        if hasattr(self.currentNode, "identifier"):
            self.currentNode.identifier = ctx.getText()

    def exitIdentifier(self, ctx:CParser.IdentifierContext):
        pass



    def enterPointerPart(self, ctx:CParser.PointerPartContext):
        if isinstance(self.currentNode, (ASTFunctionDeclarationNode, ASTTypeCastNode)):
            self.currentNode.indirections.append((False, ctx.getChildCount() == 2)) # if child count == 2, there is a const node

    def exitPointerPart(self, ctx:CParser.PointerPartContext):
        pass



    def enterOplevel15(self, ctx:CParser.Oplevel15Context):
        children = list(ctx.getChildren())
        if len(children) > 1:
            self.currentNode = self.currentNode.addChildNode(ASTCommaOperatorNode(ctx))
            self.createdNode.append(True)
        else:
            self.createdNode.append(False)

    def exitOplevel15(self, ctx:CParser.Oplevel15Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel14(self, ctx:CParser.Oplevel14Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if symbol == "=":
                self.currentNode = self.currentNode.addChildNode(ASTSimpleAssignmentOperatorNode(ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    def exitOplevel14(self, ctx:CParser.Oplevel14Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel13(self, ctx:CParser.Oplevel13Context):
        children = list(ctx.getChildren())
        if len(children) == 5:
            symbol1 = children[1].getText()
            symbol2 = children[3].getText()
            if symbol1 == "?" and symbol2 == ":":
                self.currentNode = self.currentNode.addChildNode(ASTTernaryConditionalOperatorNode(ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    def exitOplevel13(self, ctx:CParser.Oplevel13Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel12(self, ctx:CParser.Oplevel12Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if symbol == "||":
                self.currentNode = self.currentNode.addChildNode(ASTLogicOperatorNode(ASTLogicOperatorNode.LogicOperatorType["disj"], ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    def exitOplevel12(self, ctx:CParser.Oplevel12Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel11(self, ctx:CParser.Oplevel11Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if symbol == "&&":
                self.currentNode = self.currentNode.addChildNode(ASTLogicOperatorNode(ASTLogicOperatorNode.LogicOperatorType["conj"], ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    def exitOplevel11(self, ctx:CParser.Oplevel11Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel10(self, ctx:CParser.Oplevel10Context):
        self.createdNode.append(False)

    def exitOplevel10(self, ctx:CParser.Oplevel10Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel9(self, ctx:CParser.Oplevel9Context):
        self.createdNode.append(False)

    def exitOplevel9(self, ctx:CParser.Oplevel9Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel8(self, ctx:CParser.Oplevel8Context):
        self.createdNode.append(False)

    def exitOplevel8(self, ctx:CParser.Oplevel8Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel7(self, ctx:CParser.Oplevel7Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getSymbol().text
            self.currentNode = self.currentNode.addChildNode(ASTComparisonOperatorNode( \
                ASTComparisonOperatorNode.ComparisonType["inequal"] if symbol == "!=" else ASTComparisonOperatorNode.ComparisonType["equal"], ctx))
            self.createdNode.append(True)
        else:
            self.createdNode.append(False)

    def exitOplevel7(self, ctx:CParser.Oplevel7Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel6(self, ctx:CParser.Oplevel6Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getSymbol().text
            if symbol in ["<", ">", "<=", ">="]:
                comparisonType = None
                if symbol == "<": comparisonType = ASTComparisonOperatorNode.ComparisonType["lt"]
                elif symbol == ">": comparisonType = ASTComparisonOperatorNode.ComparisonType["gt"]
                elif symbol == "<=": comparisonType = ASTComparisonOperatorNode.ComparisonType["le"]
                elif symbol == ">=": comparisonType = ASTComparisonOperatorNode.ComparisonType["ge"]
                self.currentNode = self.currentNode.addChildNode(ASTComparisonOperatorNode(comparisonType, ctx))
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    def exitOplevel6(self, ctx:CParser.Oplevel6Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel5(self, ctx:CParser.Oplevel5Context):
        self.createdNode.append(False)

    def exitOplevel5(self, ctx:CParser.Oplevel5Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel4(self, ctx:CParser.Oplevel4Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if self.addBinaryArithmeticOperator(symbol, ctx):
                self.createdNode.append(True)
                return

        self.createdNode.append(False)

    def exitOplevel4(self, ctx:CParser.Oplevel4Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def addBinaryArithmeticOperator(self, symbol, ctx):
        arithmeticType = None
        if symbol == "+": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType["add"]
        elif symbol == "-": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType["sub"]
        elif symbol == "*": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType["mul"]
        elif symbol == "/": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType["div"]
        elif symbol == "%": arithmeticType = ASTBinaryArithmeticOperatorNode.ArithmeticType["modulo"]
        else: return False
        self.currentNode = self.currentNode.addChildNode(ASTBinaryArithmeticOperatorNode(arithmeticType, ctx))
        return True



    def enterOplevel3(self, ctx:CParser.Oplevel3Context):
        children = list(ctx.getChildren())
        if len(children) == 3:
            symbol = children[1].getText()
            if self.addBinaryArithmeticOperator(symbol, ctx):
                self.createdNode.append(True)
                return
        self.createdNode.append(False)

    def exitOplevel3(self, ctx:CParser.Oplevel3Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel2(self, ctx:CParser.Oplevel2Context):
        children = list(ctx.getChildren())
        if len(children) == 2:
            symbol = children[0].getText()
            if   symbol == "++": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType["increment"], ASTUnaryOperatorNode.Type["prefix"], ctx))
            elif symbol == "--": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType["decrement"], ASTUnaryOperatorNode.Type["prefix"], ctx))
            elif symbol == "+":  self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType["plus"], ASTUnaryOperatorNode.Type["prefix"], ctx))
            elif symbol == "-":  self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType["minus"], ASTUnaryOperatorNode.Type["prefix"], ctx))
            elif symbol == "&":  self.currentNode = self.currentNode.addChildNode(ASTAddressOfOperatorNode(ctx))
            elif symbol == "*":  self.currentNode = self.currentNode.addChildNode(ASTDereferenceOperatorNode(ctx))
            elif symbol == "!":  self.currentNode = self.currentNode.addChildNode(ASTLogicalNotOperatorNode(ctx))
            else:
                self.createdNode.append(False)
                return;
            self.createdNode.append(True)
            return
        self.createdNode.append(False)

    def exitOplevel2(self, ctx:CParser.Oplevel2Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterOplevel1(self, ctx:CParser.Oplevel1Context):
        children = list(ctx.getChildren())

        if len(children) == 2:
            symbol = children[1].getText()
            if symbol == "++": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType["increment"], ASTUnaryOperatorNode.Type["postfix"], ctx))
            elif symbol == "--": self.currentNode = self.currentNode.addChildNode(ASTUnaryArithmeticOperatorNode(ASTUnaryArithmeticOperatorNode.ArithmeticType["decrement"], ASTUnaryOperatorNode.Type["postfix"], ctx))
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

    def exitOplevel1(self, ctx:CParser.Oplevel1Context):
        if self.createdNode.pop(): self.currentNode = self.currentNode.parent



    def enterTypeCast(self, ctx=CParser.TypeCastContext):
        self.currentNode = self.currentNode.addChildNode(ASTTypeCastNode(ctx))

    def exitTypeCast(self, ctx=CParser.TypeCastContext):
        self.currentNode = self.currentNode.parent
