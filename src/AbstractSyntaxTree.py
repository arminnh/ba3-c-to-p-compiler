import copy
from enum import Enum
from TypeInfo import TypeInfo

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

    def typeCheck(self):
        for child in self.children:
            child.typeCheck()

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
        super(ASTIncludeNode, self).__init__("include - " + name)
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

    def getType(self):
        if self.type is None:
            raise Exception("ASTFunctionDeclarationNode type not filled in")
        return TypeInfo(rvalue=None, basetype=self.type)

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
        self.const = []
        self.indirections = 0
    
    def getType(self):
        if self.type is None:
            raise Exception("ASTParameterNode type not filled in")
        return TypeInfo(rvalue=None, basetype=self.type, indirections=self.indirections, const=self.const)

    def __eq__(self, other):
        return self.type == other.type \
            and self.isArray == other.isArray \
            and self.const == other.const \
            and self.indirections == other.indirections
        # and self.arrayLength == other.arrayLength # if checking arrayLength, need to check possible expression child equality

    def out(self, level):
        s = offset * level + "parameter" + " - " + self.type

        if (len(self.const) != 0) :
            s += " - const: " + str(self.const)

        if (self.indirections != 0) :
            s += " - indirections: " + str(self.indirections)

        s += " - " + str(self.identifier)

        if (self.isArray != False) :
            s += " - array:  " + str(self.isArray)

            if (self.arrayLength != None) :
                s += " - arrayLength: " + str(self.arrayLength)

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

class ASTReturnNode(ASTStatementNode):
    def __init__(self):
        super(ASTReturnNode, self).__init__("return")

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
        s += offset * (level + 1) + "type: " + self.type
        s += ", const: " + str(self.isConstant) + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTDeclaratorInitializerNode(ASTNode):
    def __init__(self):
        super(ASTDeclaratorInitializerNode, self).__init__("declarator initializer")
        self.identifier = None
        self.isArray = False
        self.indirections = 0
        self.const = []
        # if arrayParameter hasArrayLength -> first child is array length, else it is initializationValue
        self.hasArrayLength = False
        # arrayLength will be an expressionNode child

    def getType(self):
        return TypeInfo(rvalue=None, basetype=self.parent.type, indirections=self.indirections, const=[self.parent.isConstant] + self.const, isArray=self.isArray)

    def out(self, level):
        s = offset * level + "declaratorInitializer" + "\n"

        if (len(self.const) != 0) :
            s += offset * (level + 1) +  "const: " + str(self.const) + "\n"

        if (self.indirections != 0) :
            s += offset * (level + 1) + "indirections: " + str(self.indirections) + "\n"

        s += offset * (level + 1) + "identifier: " + self.identifier

        if (self.isArray != False) :
            s += " - array: " + str(self.isArray)

        s += "\n"

        if len(self.children) == 1:
            if self.hasArrayLength:
                s += offset * (level + 1) + "arrayLength\n"
                s += self.children[0].out(level + 2)
            else:
                s += offset * (level + 1) + "initialization value\n"
                s += self.children[0].out(level + 2)
        elif len(self.children) == 2:
            s += offset * (level + 1) + "arrayLength\n"
            s += self.children[0].out(level + 2)
            s += offset * (level + 1) + "initialization value\n"
            s += self.children[1].out(level + 2)

        return s if (not self.children) else s


'''
    EXPRESSIONS
'''


class ASTExpressionNode(ASTNode):
    def __init__(self, label="expression"):
        super(ASTExpressionNode, self).__init__(label)

    def typeCheck(self):
        return NotImplementedError

    def getType(self):
        raise NotImplementedError

class ASTIntegerLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTIntegerLiteralNode, self).__init__("int")
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")
    
    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTFloatLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTFloatLiteralNode, self).__init__("float")
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="float")
    
    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTCharacterLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTCharacterLiteralNode, self).__init__("char")
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="char")
    
    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTStringLiteralNode(ASTExpressionNode):
    def __init__(self, value):
        super(ASTStringLiteralNode, self).__init__("string")
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="char", indirections=1, const=[False], isArray=True)

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTVariableNode(ASTExpressionNode):
    def __init__(self, identifier):
        super(ASTVariableNode, self).__init__("variable")
        self.identifier = identifier
        self.type = None

    def typeCheck(self):
        return True

    def getType(self):
        if self.type is None:
            raise Exception("Type has not been set yet for variable " + self.identifier)
        return self.type

    def out(self, level):
        return offset * level + self.label + " - " + self.identifier + "\n"

class ASTFunctionCallNode(ASTExpressionNode):
    def __init__(self):
        super(ASTFunctionCallNode, self).__init__("function call")
        self.identifier = None
        self.type = None

    def typeCheck(self):
        return True

    def getType(self):
        if self.type is None:
            raise Exception("Type has not been set yet for function " + self.identifier)
        return self.type

    def out(self, level):
        s = offset * level + self.label + " - " + self.identifier + "\n"

        return s if (not self.children) else self.outChildren(s, level)


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

    def typeCheck(self):
        return True

    def getType(self):
        return self.children[0].getType()

class ASTBinaryOperatorNode(ASTExpressionNode):
    def __init__(self, label):
        super(ASTBinaryOperatorNode, self).__init__(label)

    def typeCheck(self):
        if not self.children[0].getType().isCompatible(self.children[1].getType()):
            raise Exception("Binary operator operands must have the same type (have " + str(self.children[0].getType()) + " and " + str(self.children[1].getType()) + ")")

    def getType(self):
        return self.children[0].getType()

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

    def typeCheck(self):
        if not self.children[0].getType().isCompatible(TypeInfo(basetype="int")):
            raise Exception("Ternary conditional operator needs int as first operand")
        if self.children[1].getType() != self.children[2].getType():
            raise Exception("Ternary conditional operator alternatives should be of equal type")
        return True

    def getType():
        return self.children[1].getType()

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

    def typeCheck(self):
        if self.children[0].getType() != self.children[1].getType():
            raise Exception("Logic operator operands must have the same type")
        if self.children[0].getType().isCompatible(TypeInfo(basetype="int")):
            raise Exception("Logic operator operands not compatible with int")

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

    def __init__(self, comparisonType):
        label = str(comparisonType)
        super(ASTComparisonOperatorNode, self).__init__(label)
        self.comparisonType = comparisonType

    def typeCheck(self):
        if self.children[0].getType() != self.children[1].getType():
            raise Exception("Comparison operator operands need to be of same type")
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")

class ASTUnaryArithmeticOperatorNode(ASTUnaryOperatorNode):
    class ArithmeticType(Enum):
        increment = 1
        decrement = 2

        def __str__(self):
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['increment']: return "++"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']: return "--"
            return super(ASTUnaryArithmeticOperatorNode, self).__str__()

    def __init__(self, arithmeticType, operatorType):
        super(ASTUnaryArithmeticOperatorNode, self).__init__(str(arithmeticType) + " - " + str(operatorType), str(operatorType))

class ASTAddressOfOperatorNode(ASTUnaryOperatorNode):
    def __init__(self):
        super(ASTAddressOfOperatorNode, self).__init__("&", ASTUnaryOperatorNode.Type['prefix'])

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections += 1
        return ttype

class ASTDereferenceOperatorNode(ASTUnaryOperatorNode):
    def __init__(self):
        super(ASTDereferenceOperatorNode, self).__init__("*", ASTUnaryOperatorNode.Type['prefix'])

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections -= 1
        if ttype.indirections == 0:
            ttype.isArray = False
        return ttype

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

    def typeCheck(self):
        self.root.typeCheck()
