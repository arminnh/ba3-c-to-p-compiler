import copy
from enum import Enum
from TypeInfo import TypeInfo
from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNode

offset = "  | "

class ASTNode(object):

    def __init__(self, label="no label", ctx=None):
        self.tree = None
        if not hasattr(self, "parent"):
            self.parent = None
        self.error = False
        self.label = label
        self.ctx = ctx
        self.children = [] # don't manipulate or read directly; use addChildNode and getChildren

    def addChildNode(self, node):
        if not isinstance(node, ASTNode):
            raise Exception("trying to add child of non-ASTNode type: expected" + str(ASTNode) + ", got " + str(type(node)))
        self.children.append(node)
        node.parent = self
        node.tree = self.tree
        return node

    def accept(self, visitor):
        raise NotImplementedError

    def getRelevantToken(self):
        return self.getFirstToken()

    def getFirstToken(self, node=None): # node = context node, not AST node
        if node is None: node = self.ctx
        if node is None:
            raise Exception(str(type(self)) + "'s ctx was not set")
        if isinstance(node, TerminalNode):
            return node.getSymbol()
        for child in node.getChildren():
            token = self.getFirstToken(child)
            if token is not None:
                return token

        return None

    def getLineAndColumn(self):
        token = None

        token = self.getRelevantToken()
        if isinstance(token, CommonToken):
            return (token.line, token.column)
        return (None, None)

    def out(self, level=0):
        s = offset * level + self.label + "\n"

        #return (s + "\n") if (not self.children) else self.outChildren(s, level)
        return s if (not self.children) else self.outChildren(s, level)

    def outChildren(self, s, level):
        for child in self.children:
            s += child.out(level + 1)

        return s

    # def __str__(self):
    #     return self.label

class ASTProgramNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTProgramNode, self).__init__("program", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitProgramNode(self)

class ASTIncludeNode(ASTNode):
    def __init__(self, isStdInclude=False, name="include name", ctx=None):
        super(ASTIncludeNode, self).__init__("include - " + name, ctx)
        self.isStdInclude = isStdInclude
        self.name = name

    def accept(self, visitor):
        visitor.visitIncludeNode(self)

class ASTFunctionDeclarationNode(ASTNode):
    def __init__(self, label="function declaration", ctx=None):
        super(ASTFunctionDeclarationNode, self).__init__(label, ctx)
        self.basetype = None
        self.identifier = None
        self.indirections = [] # list of tuples of booleans: (array, const)
        self.isConstant = False
        # parameters are child nodes

    def accept(self, visitor):
        if not self.error:
            visitor.visitFunctionDeclarationNode(self)

    def getType(self):
        if self.basetype is None:
            raise Exception("ASTFunctionDeclarationNode basetype not filled in", line, column)
        return TypeInfo(rvalue=True, basetype=self.basetype, indirections=[(False, self.isConstant)] + self.indirections)

    def getParameters(self):
        for child in self.children:
            if isinstance(child, ASTParametersNode):
                return child
        return None

    def out(self, level):
        s = offset * level + self.label + "\n"
        s += offset * (level + 1) + "return type: " + str(self.basetype) + "\n"
        s += offset * (level + 1) + "identifier:  " + str(self.identifier) + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTFunctionDefinitionNode(ASTFunctionDeclarationNode):
    def __init__(self, label="function definition", ctx=None):
        super(ASTFunctionDefinitionNode, self).__init__(label, ctx)
        self.isStdioFunction = False
        # parameters and statements are child nodes

    def accept(self, visitor):
        if not self.error:
            visitor.visitFunctionDefinitionNode(self)

class ASTMainFunctionNode(ASTFunctionDefinitionNode):
    def __init__(self, ctx=None):
        super(ASTMainFunctionNode, self).__init__("main", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitMainFunctionNode(self)

class ASTParametersNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTParametersNode, self).__init__("parameters", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitParametersNode(self)

    def __eq__(self, other):
        if len(self.children) != len(other.children):
            return False

        for i, parameter in enumerate(self.children):
            if parameter != other.children[i]:
                return False
        return True

class ASTParameterNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTParameterNode, self).__init__("parameter", ctx)
        self.basetype = None
        self.identifier = None
        # self.arrayLength = None
        self.isConstant = False
        self.indirections = [] # list of tuples of booleans: (array, const)

    def accept(self, visitor):
        if not self.error:
            visitor.visitParameterNode(self)

    def getType(self):
        if self.basetype is None:
            raise Exception("ASTParameterNode basetype not filled in", line, column)
        return TypeInfo(rvalue=False, basetype=self.basetype, indirections = [(False, self.isConstant)] + self.indirections)

    def __eq__(self, other):
        # TODO: if checking arrayLength, need to check possible expression child equality. (somehow do self.arrayLength == other.arrayLength)
        return self.getType() == other.getType()

    def out(self, level):
        s = offset * level

        s += str(self.identifier) + ": " + str(self.getType())

        # if self.isConstant:
        #     s += "const "

        # s += str(self.basetype) + " "
        #
        # nrOfIndirections = self.indirections if not self.isArray else self.indirections - 1
        # for i in range(0, nrOfIndirections):
        #     if i != 0:
        #         s += " "
        #     s += "*"
        #     if i < len(self.const) and self.const[i]:
        #         s += " const"
        #     if i == (nrOfIndirections - 1):
        #         s += " "
        #
        # s += str(self.identifier)
        #
        # if (self.isArray != False) :
        #     s += " []"

        return s + "\n"

class ASTArgumentsNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTArgumentsNode, self).__init__("arguments", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitArgumentsNode(self)

class ASTInitializerListNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTInitializerListNode, self).__init__("initializer list", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitInitializerListNode(self)

'''
    STATEMENTS
'''


class ASTStatementsNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTStatementsNode, self).__init__("statements", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitStatementsNode(self)

class ASTStatementNode(ASTNode):
    def __init__(self, label="statement", ctx=None):
        super(ASTStatementNode, self).__init__(label, ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitStatementNode(self)

class ASTReturnNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTReturnNode, self).__init__("return", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitReturnNode(self)

class ASTIfNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTIfNode, self).__init__("if", ctx)
        self.condition = None # expressionNode
        self.elseCondNode = None # elseNode

    def accept(self, visitor):
        if not self.error:
            visitor.visitIfNode(self)

    def out(self, level):
        s = offset * level + self.label + "\n"

        for i in range(len(self.children)):
            if i == 0:
                s += offset * (level + 1) + "condition\n"
                s += self.children[i].out(level + 2)
            elif i == 1:
                s += offset * (level + 1) + "then\n"
                s += self.children[i].out(level + 2)
            else:
                s += self.children[i].out(level + 1)

        return s

class ASTElseNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTElseNode, self).__init__("else", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitElseNode(self)

class ASTWhileNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTWhileNode, self).__init__("while", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitWhileNode(self)

class ASTDoWhileNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTDoWhileNode, self).__init__("doWhile", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitDoWhileNode(self)

class ASTVariableDeclarationNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTVariableDeclarationNode, self).__init__("variable declaration", ctx)
        self.basetype = None
        self.isConstant = False
        # declaratorInitializers are children

    def accept(self, visitor):
        if not self.error:
            visitor.visitVariableDeclarationNode(self)

    def getRelevantToken(self):
        # TODO: point to specific parts of declaration node
        super(ASTVariableDeclarationNode, self).getRelevantToken()

    def out(self, level):
        s  = offset * level + self.label + "\n"
        s += offset * (level + 1) + "type: " + str(self.basetype)
        s += ", const: " + str(self.isConstant) + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTDeclaratorInitializerNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTDeclaratorInitializerNode, self).__init__("declarator initializer", ctx)
        self.identifier = None
        # arrayLength will be an expressionNode child
        self.indirections = [] # list of tuples of booleans: (array, const)

    def accept(self, visitor):
        if not self.error:
            visitor.visitDeclaratorInitializerNode(self)

    def getType(self):
        return TypeInfo(rvalue=False, basetype=self.parent.basetype, indirections = [(False, self.parent.isConstant)] + self.indirections)

    def out(self, level):
        s = offset * level + "declarator initializer" + "\n" + (offset * (level + 1))

        s += self.identifier + ": "
        s += str(self.getType()) + "\n"

        # nrOfIndirections = self.indirections if not self.isArray else self.indirections - 1
        # for i in range(0, nrOfIndirections):
        #     if i != 0:
        #         s += " "
        #     s += "*"
        #     if i < len(self.const) and self.const[i]:
        #         s += " const"
        #     if i == (nrOfIndirections - 1):
        #         s += " "
        #
        # s += self.identifier
        #
        # if (self.isArray != False) :
        #     s += " []"

        # s += "   ind: " + str(self.indirections) + " const: " + str(self.const)

        # s += "\n"

        for child in self.children:
            if isinstance(child, ASTExpressionNode):
                s += offset * (level + 1) + "arrayLength\n"
                s += child.out(level + 2)
            elif isinstance(child, ASTInitializerListNode):
                s += child.out(level + 1)

        return s


'''
    EXPRESSIONS
'''


class ASTExpressionNode(ASTNode):
    def __init__(self, label="expression", ctx=None):
        super(ASTExpressionNode, self).__init__(label, ctx)

    def baseExpression(self):
        if isinstance(self.parent, ASTExpressionNode):
            return self.parent.baseExpression()
        return self

    def getType(self):
        raise NotImplementedError

class ASTIntegerLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTIntegerLiteralNode, self).__init__("int", ctx)
        self.value = value

    def accept(self, visitor):
        if not self.error:
            visitor.visitIntegerLiteralNode(self)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTFloatLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTFloatLiteralNode, self).__init__("float", ctx)
        self.value = value

    def accept(self, visitor):
        if not self.error:
            visitor.visitFloatLiteralNode(self)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="float")

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTCharacterLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTCharacterLiteralNode, self).__init__("char", ctx)
        self.value = value

    def accept(self, visitor):
        if not self.error:
            visitor.visitCharacterLiteralNode(self)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="char")

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTStringLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTStringLiteralNode, self).__init__("string", ctx)
        self.value = value

    def accept(self, visitor):
        if not self.error:
            visitor.visitStringLiteralNode(self)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="char", indirections=[(False, False), (True, False)])

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTVariableNode(ASTExpressionNode):
    def __init__(self, identifier, ctx=None):
        super(ASTVariableNode, self).__init__("variable", ctx)
        self.identifier = identifier
        self.typeInfo = None

    def accept(self, visitor):
        if not self.error:
            visitor.visitVariableNode(self)

    def getType(self):
        return self.typeInfo

    def out(self, level):
        return offset * level + self.label + " - " + self.identifier + "\n"

class ASTFunctionCallNode(ASTExpressionNode):
    def __init__(self, ctx=None):
        super(ASTFunctionCallNode, self).__init__("function call", ctx)
        self.identifier = None
        self.definitionNode = None
        self.errorParameter = None

    def accept(self, visitor):
        if not self.error:
            visitor.visitFunctionCallNode(self)

    def getType(self):
        if self.definitionNode is None:
            raise Exception("definitionNode has not been set yet for function " + self.identifier)
        return self.definitionNode.getType().toRvalue()

    def getRelevantToken(self):
        if self.errorParameter is not None:
            return self.getFirstToken(list(list(self.ctx.getChildren())[2].getChildren())[2 * self.errorParameter])
        return super(ASTFunctionCallNode, self).getRelevantToken()

    def out(self, level):
        s = offset * level + self.label + " - " + self.identifier + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTTypeCastNode(ASTExpressionNode):
    def __init__(self, ctx=None):
        super(ASTTypeCastNode, self).__init__("type cast", ctx)
        self.basetype = None
        self.indirections = []
        self.isConstant = False

    def accept(self, visitor):
        if not self.error:
            visitor.visitTypeCastNode(self)

    def getType(self):
        if self.basetype is None:
            raise Exception("ASTTypeCastNode basetype not filled in", line, column)
        return TypeInfo(rvalue=True, basetype=self.basetype, indirections = [(False, self.isConstant)] + self.indirections)


'''
    EXPRESISSION OPERATIONS
'''

class ASTUnaryOperatorNode(ASTExpressionNode):
    class Type(Enum):
        prefix = 1
        postfix = 2

        def __str__(self):
            if self == ASTUnaryOperatorNode.Type['prefix']: return "prefix"
            if self == ASTUnaryOperatorNode.Type['postfix']: return "postfix"
            return super(ASTUnaryOperatorNode.Type, self).__str__()

    def __init__(self, label, operatorType, ctx):
        super(ASTUnaryOperatorNode, self).__init__(label, ctx)
        self.operatorType = operatorType

    def addChildNode(self, node):
        if len(self.children) >= 1: # this should never happen
            raise Exception("ASTUnaryOperatorNode cannot have more than one child")
        return super(ASTUnaryOperatorNode, self).addChildNode(node)

    def getType(self):
        return NotImplementedError

class ASTBinaryOperatorNode(ASTExpressionNode):
    def __init__(self, label, ctx=None):
        super(ASTBinaryOperatorNode, self).__init__(label, ctx)

    def getType(self):
        return self.children[0].getType().toRvalue()

    def addChildNode(self, node):
        if len(self.children) >= 2: # this should never happen
            raise Exception("ASTBinaryOperatorNode cannot have more than two children")
        return super(ASTBinaryOperatorNode, self).addChildNode(node)

class ASTTernaryOperatorNode(ASTExpressionNode):
    def __init__(self, label, ctx=None):
        super(ASTTernaryOperatorNode, self).__init__(label, ctx)

    def addChildNode(self, node):
        if len(self.children) >= 3:
            raise Exception("ASTTernaryOperatorNode cannot have more than three children")
        return super(ASTTernaryOperatorNode, self).addChildNode(node)

class ASTTernaryConditionalOperatorNode(ASTTernaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTTernaryConditionalOperatorNode, self).__init__("?:", ctx)
        self.errorOperand = None

    def accept(self, visitor):
        if not self.error:
            visitor.visitTernaryConditionalOperatorNode(self)

    def getRelevantToken(self):
            return self.getFirstToken(list(self.ctx.getChildren())[self.errorOperand * 2])

    def getType(self):
        return self.children[1].getType().toRvalue()

class ASTSimpleAssignmentOperatorNode(ASTBinaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTSimpleAssignmentOperatorNode, self).__init__("=", ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitSimpleAssignmentOperatorNode(self)

class ASTLogicOperatorNode(ASTBinaryOperatorNode):
    class LogicOperatorType(Enum):
        conj = 1
        disj = 2

        def __str__(self):
            if self == ASTLogicOperatorNode.LogicOperatorType['conj']: return "and"
            if self == ASTLogicOperatorNode.LogicOperatorType['disj']: return "or"
            return super(ASTLogicOperatorNode.LogicOperatorType, self).__str__()

    def __init__(self, logicOperatorType, ctx=None):
        super(ASTLogicOperatorNode, self).__init__(str(logicOperatorType), ctx)
        self.logicOperatorType = logicOperatorType

    def accept(self, visitor):
        if not self.error:
            visitor.visitLogicOperatorNode(self)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")

class ASTComparisonOperatorNode(ASTBinaryOperatorNode):
    class ComparisonType(Enum):
        lt = 1
        gt = 2
        le = 3
        ge = 4
        equal = 5
        inequal = 6

        def __str__(self):
            if self == ASTComparisonOperatorNode.ComparisonType['lt']: return "<"
            if self == ASTComparisonOperatorNode.ComparisonType['gt']: return ">"
            if self == ASTComparisonOperatorNode.ComparisonType['le']: return "<="
            if self == ASTComparisonOperatorNode.ComparisonType['ge']: return ">="
            if self == ASTComparisonOperatorNode.ComparisonType['equal']: return "=="
            if self == ASTComparisonOperatorNode.ComparisonType['inequal']: return "!="
            return super(ASTComparisonOperatorNode.ComparisonType, self).__str__()

    def __init__(self, comparisonType, ctx=None):
        label = str(comparisonType)
        super(ASTComparisonOperatorNode, self).__init__(label, ctx)
        self.comparisonType = comparisonType

    def accept(self, visitor):
        if not self.error:
            visitor.visitComparisonOperatorNode(self)

    def getRelevantToken(self):
        return list(self.ctx.getChildren())[1].getSymbol()

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int").toRvalue()

class ASTUnaryArithmeticOperatorNode(ASTUnaryOperatorNode):
    class ArithmeticType(Enum):
        increment = 1
        decrement = 2
        plus = 3
        minus = 4

        def __str__(self):
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['increment']: return "++"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']: return "--"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['plus']: return "+"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['minus']: return "-"
            return super(ASTUnaryArithmeticOperatorNode, self).__str__()

        def wordStr(self):
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['increment']: return "increment"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']: return "decrement"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['plus']: return "unary plus"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['minus']: return "unary minus"
            return str(self)

    def __init__(self, arithmeticType, operatorType, ctx=None):
        super(ASTUnaryArithmeticOperatorNode, self).__init__(str(arithmeticType) + " - " + str(operatorType), operatorType, ctx)
        self.arithmeticType = arithmeticType

    def accept(self, visitor):
        if not self.error:
            visitor.visitUnaryArithmeticOperatorNode(self)

    def getType(self):
        return self.children[0].getType()

class ASTAddressOfOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTAddressOfOperatorNode, self).__init__("&", ASTUnaryOperatorNode.Type['prefix'], ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitAddressOfoperatorNode(self)

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections.append((False, False))
        ttype.rvalue = True
        return ttype


class ASTDereferenceOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTDereferenceOperatorNode, self).__init__("*", ASTUnaryOperatorNode.Type['prefix'], ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitDereferenceNode(self)

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections.pop()
        ttype.rvalue = False

        return ttype

    def getRelevantToken(self):
        return self.getFirstToken(list(self.ctx.getChildren())[1])

class ASTLogicalNotOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTLogicalNotOperatorNode, self).__init__("!", ASTUnaryOperatorNode.Type['prefix'], ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitLogicalNotOperatorNode(self)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")

class ASTArraySubscriptNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTArraySubscriptNode, self).__init__("[]", ASTUnaryOperatorNode.Type['postfix'], ctx)

    def accept(self, visitor):
        if not self.error:
            visitor.visitArraySubscriptNode(self)

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections.pop()
        ttype.rvalue = False

        return ttype

    def addChildNode(self, node):
        if len(self.children) >= 2:
            raise Exception("ASTArraySubscriptNode cannot have more than two children")
        return ASTNode.addChildNode(self, node)

class ASTBinaryArithmeticOperatorNode(ASTBinaryOperatorNode):
    class ArithmeticType(Enum):
        add = 1
        sub = 2
        mul = 3
        div = 4
        modulo = 5

        def __str__(self):
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['add']: return "+"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['sub']: return "-"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['mul']: return "*"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['div']: return "/"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['modulo']: return "%"
            return super(ASTBinaryArithmeticOperatorNode.ArithmeticType, self).__str__()

    def __init__(self, arithmeticType, ctx=None):
        label = str(arithmeticType)
        ASTBinaryOperatorNode.__init__(self, label, ctx)
        self.arithmeticType = arithmeticType

    def accept(self, visitor):
        if not self.error:
            visitor.visitBinaryArithmeticNode(self)


'''
    AST
'''

class AbstractSyntaxTree:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root
        self._root.tree = self

    def __str__(self):
        return "AST:\n" + self.root.out()
