from enum import Enum

offset = "  | "

class ASTNode(object):

    def __init__(self, label="no label", parent=None):
        self.label = label
        self.children = [] # don't manipulate or read directly; use addChildNode and getChildren
        self.parent = parent

    def addChildNode(self, node):
        if not isinstance(node, ASTNode):
            raise Exception("trying to add child of non-ASTNode type: expected" + str(ASTNode) + ", got " + str(type(node)))
        self.children.append(node)
        node.parent = self
        return node

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
    def __init__(self):
        super(ASTProgramNode, self).__init__("program")

class ASTIncludeNode(ASTNode):
    def __init__(self, isStdInclude=False, name="include name"):
        super(ASTIncludeNode, self).__init__("include | " + name)
        self.isStdInclude = isStdInclude
        self.name = name

class ASTMainFunctionNode(ASTNode):
    def __init__(self):
        super(ASTMainFunctionNode, self).__init__("main")

class ASTFunctionDeclarationNode(ASTNode):
    def __init__(self, label="functionDeclaration"):
        super(ASTFunctionDeclarationNode, self).__init__(label)
        self.type = None
        self.identifier = None
        # parameters are child nodes

    def getParameters(self):
        for child in self.children:
            if isinstance(child, ASTParametersNode):
                return child
        return None

    def out(self, level):
        s = offset * level + self.label + "\n"
        s += offset * (level + 1) + "return type: " + self.type + "\n"
        s += offset * (level + 1) + "identifier:  " + self.identifier + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTFunctionDefinitionNode(ASTFunctionDeclarationNode):
    def __init__(self):
        super(ASTFunctionDefinitionNode, self).__init__("function definition")
        # parameters and statements are child nodes

class ASTParametersNode(ASTNode):
    def __init__(self):
        super(ASTParametersNode, self).__init__("parameters")

    def __eq__(self, other):
        if len(self.children) != len(other.children):
            return False

        for i, parameter in enumerate(self.children):
            if parameter != other.children[i]:
                return False
        return True

class ASTParameterNode(ASTNode):
    def __init__(self):
        super(ASTParameterNode, self).__init__("parameter")
        self.type = None
        self.identifier = None
        self.isArray = False
        self.arrayLength = None
        # TODO: arrayLength can be an expressionNode -> change
        self.isConstant = False
        self.indirections = 0

    def __eq__(self, other):
        return self.type == other.type \
            and self.isArray == other.isArray \
            and self.isConstant == other.isConstant \
            and self.indirections == other.indirections
        # and self.arrayLength == other.arrayLength # if checking arrayLength, need to check possible expression child equality

    def out(self, level):
        s = offset * level + "parameter" + " | " + self.type

        if (self.isConstant != False) :
            s += " | const"

        if (self.indirections != 0) :
            s += " | indirections: " + str(self.indirections)

        s += " | " + self.identifier

        if (self.isArray != False) :
            s += " | array:  " + str(self.isArray)

            if (self.arrayLength != None) :
                s += " | arrayLength: " + str(self.arrayLength)

        return s + "\n"

class ASTArgumentsNode(ASTNode):
    def __init__(self):
        super(ASTArgumentsNode, self).__init__("arguments")


'''
    STATEMENTS
'''


class ASTStatementsNode(ASTNode):
    def __init__(self):
        super(ASTStatementsNode, self).__init__("statements")

class ASTStatementNode(ASTNode):
    def __init__(self, label="statement"):
        super(ASTStatementNode, self).__init__(label)

class ASTIfNode(ASTStatementNode):
    def __init__(self):
        super(ASTIfNode, self).__init__("if")
        self.condition = None # expressionNode
        self.elseCondNode = None # elseNode

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
    def __init__(self):
        super(ASTElseNode, self).__init__("else")

class ASTWhileNode(ASTStatementNode):
    def __init__(self):
        super(ASTWhileNode, self).__init__("while")

class ASTDoWhileNode(ASTStatementNode):
    def __init__(self):
        super(ASTDoWhileNode, self).__init__("doWhile")

class ASTVariableDeclarationNode(ASTStatementNode):
    def __init__(self):
        super(ASTVariableDeclarationNode, self).__init__("variable declaration")
        self.type = None
        self.isConstant = False
        # declaratorInitializers are children

    def out(self, level):
        s  = offset * level + self.label + "\n"
        s += offset * (level + 1) + "return type: " + self.type
        s += ", const: " + str(self.isConstant) + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTVariableDefinitionNode(ASTVariableDeclarationNode):
    def __init__(self):
        super(ASTVariableDefinitionNode, self).__init__("variable definition")
        # parameters and statements are child nodes

class ASTDeclaratorInitializerNode(ASTNode):
    def __init__(self):
        super(ASTDeclaratorInitializerNode, self).__init__("declarator initializer")
        self.identifier = None
        self.isArray = False
        self.indirections = 0
        # arrayLength will be an expressionNode child

    @property
    def type(self):
        return self.parent.type

    def out(self, level):
        s = offset * level + "declaratorInitializer" + "\n"

        if (self.indirections != 0) :
            s += offset * (level + 1) + "indirections: " + str(self.indirections) + "\n"

        s += offset * (level + 1) + "identifier: " + self.identifier

        if (self.isArray != False) :
            s += " | array: " + str(self.isArray)

        s += "\n"

        for child in self.children:
            if isinstance(child, ASTExpressionNode):
                if self.isArray:
                    s += offset * (level + 1) + "arrayLength\n"
                    s += child.out(level + 2)
                else:
                    s += offset * (level + 1) + "initialization value\n"
                    s += child.out(level + 2)

            else:
                s += child.out(level + 1)

        return s if (not self.children) else s


'''
    EXPRESSIONS
'''


class ASTExpressionNode(ASTNode):
    def __init__(self, label="expression"):
        super(ASTExpressionNode, self).__init__(label)

class ASTReturnExpressionNode(ASTExpressionNode):
    def __init__(self):
        super(ASTReturnExpressionNode, self).__init__("return")

class ASTIntegerLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTIntegerLiteralNode, self).__init__("int")
        self.value = value

    def out(self, level):
        return offset * level + self.label + " | " + str(self.value) + "\n"

class ASTFloatLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTFloatLiteralNode, self).__init__("float")
        self.value = value

    def out(self, level):
        return offset * level + self.label + " | " + str(self.value) + "\n"

class ASTCharacterLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTCharacterLiteralNode, self).__init__("char")
        self.value = value

    def out(self, level):
        return offset * level + self.label + " | " + str(self.value) + "\n"

class ASTStringLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTStringLiteralNode, self).__init__("char*")
        self.value = value

    def out(self, level):
        return offset * level + self.label + " | " + str(self.value) + "\n"

class ASTVariableNode(ASTExpressionNode):
    def __init__(self, identifier):
        super(ASTVariableNode, self).__init__("variable")
        self.identifier = identifier

    def out(self, level):
        return offset * level + self.label + " | " + self.identifier + "\n"

class ASTFunctionCallNode(ASTExpressionNode):
    def __init__(self):
        super(ASTFunctionCallNode, self).__init__("function call")
        self.identifier = None

'''
    EXPRESISSION OPERATIONS
'''

# TODO: [] operator
class ASTUnaryOperatorNode(ASTExpressionNode):
    class Type(Enum):
        prefix = 1
        postfix = 2

        def __str__(self):
            if self == ASTUnaryOperatorNode.Type['prefix']: return "prefix"
            if self == ASTUnaryOperatorNode.Type['postfix']: return "postfix"
            return super(ASTUnaryOperatorNode.Type, self).__str__()

    def __init__(self, label, operatorType):
        super(ASTUnaryOperatorNode, self).__init__(label)
        self.operatorType = operatorType

    def addChildNode(self, node):
        if len(self.children) >= 1: # this should never happen
            raise Exception("ASTUnaryOperatorNode cannot have more than one child")
        print(str(type(node)))
        return super(ASTUnaryOperatorNode, self).addChildNode(node)

class ASTBinaryOperatorNode(ASTExpressionNode):
    def __init__(self, label):
        super(ASTBinaryOperatorNode, self).__init__(label)

    def addChildNode(self, node):
        if len(self.children) >= 2: # this should never happen
            raise Exception("ASTBinaryOperatorNode cannot have more than two children")
        return super(ASTBinaryOperatorNode, self).addChildNode(node)

class ASTTernaryOperatorNode(ASTExpressionNode):
    def __init__(self, label):
        super(ASTTernaryOperatorNode, self).__init__(label)

    def addChildNode(self, node):
        if len(self.children) >= 3:
            raise Exception("ASTTernaryOperatorNode cannot have more than three children")
        return super(ASTTernaryOperatorNode, self).addChildNode(node)

class ASTTernaryConditionalOperatorNode(ASTTernaryOperatorNode):
    def __init__(self):
        super(ASTTernaryConditionalOperatorNode, self).__init__("?:")

class ASTSimpleAssignmentOperatorNode(ASTBinaryOperatorNode):
    def __init__(self):
        super(ASTSimpleAssignmentOperatorNode, self).__init__("=")

class ASTLogicOperatorNode(ASTBinaryOperatorNode):
    class LogicOperatorType(Enum):
        conj = 1
        disj = 2

        def __str__(self):
            if self == ASTLogicOperatorNode.LogicOperatorType['conj']: return "and"
            if self == ASTLogicOperatorNode.LogicOperatorType['disj']: return "or"
            return super(ASTLogicOperatorNode.LogicOperatorType, self).__str__()

    def __init__(self, logicOperatorType):
        super(ASTLogicOperatorNode, self).__init__(str(logicOperatorType))
        self.logicOperatorType = logicOperatorType

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

    def __init__(self, comparisonType):
        label = str(comparisonType)
        super(ASTComparisonOperatorNode, self).__init__(label)
        self.comparisonType = comparisonType

class ASTUnaryArithmeticOperatorNode(ASTUnaryOperatorNode):
    class ArithmeticType(Enum):
        increment = 1
        decrement = 2

        def __str__(self):
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['increment']: return "++"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']: return "--"
            return super(ASTUnaryArithmeticOperatorNode, self).__str__()

    def __init__(self, arithmeticType, operatorType):
        super(ASTUnaryArithmeticOperatorNode, self).__init__(str(arithmeticType) + " | " + str(operatorType), str(operatorType))

class ASTAddressOfOperatorNode(ASTUnaryOperatorNode):
    def __init__(self):
        super(ASTAddressOfOperatorNode, self).__init__("&", ASTUnaryOperatorNode.Type['prefix'])

class ASTDereferenceOperatorNode(ASTUnaryOperatorNode):
    def __init__(self):
        super(ASTDereferenceOperatorNode, self).__init__("*", ASTUnaryOperatorNode.Type['prefix'])

class ASTLogicalNotOperatorNode(ASTUnaryOperatorNode):
    def __init__(self):
        super(ASTLogicalNotOperatorNode, self).__init__("!", ASTUnaryOperatorNode.Type['prefix'])

class ASTArraySubscriptNode(ASTUnaryOperatorNode):
    def __init__(self, subscript):
        super(ASTArraySubscriptNode, self).__init__("[]", ASTUnaryOperatorNode.Type['postfix'])

class ASTBinaryArithmeticOperatorNode(ASTBinaryOperatorNode):
    class ArithmeticType(Enum):
        add = 1
        sub = 2
        mul = 3
        div = 4
        remainder = 5

        def __str__(self):
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['add']: return "+"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['sub']: return "-"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['mul']: return "*"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['div']: return "/"
            if self == ASTBinaryArithmeticOperatorNode.ArithmeticType['remainder']: return "%"
            return super(ASTBinaryArithmeticOperatorNode.ArithmeticType, self).__str__()

    def __init__(self, arithmeticType):
        label = str(arithmeticType)
        ASTBinaryOperatorNode.__init__(self, label)
        self.arithmeticType = arithmeticType


'''
    AST
'''

class AbstractSyntaxTree:

    def __init__(self, root=ASTNode("root")):
        self.root = root

    def __str__(self):
        return "AST:\n" + self.root.out()
