from pprint import *
from enum import Enum

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

    def getChildren(self):
        return self.children

    def out(self, level=1):
        str =  self.label + "\n"

        for child in self.getChildren():
            str += "   " * level + child.out(level+1)

        if not self.children:
            str += "\n"

        return str

    def __str__(self):
        return self.label

class ASTNumberLiteralNode(ASTNode):
    class NumberType(Enum):
        integer = 1
        float = 2

        def __str__(self):
            if self == ASTNumberLiteralNode.NumberType['integer']: return "integer"
            if self == ASTNumberLiteralNode.NumberType['float']: return "float"
            return super(ASTNumberLiteralNode.NumberType, self).__str__()

    def __init__(self, value, parent=None):
        self.value = value
        super(ASTNumberLiteralNode, self).__init__(str(value) + "|" + str(self.type()))

    def value(self):
        return self.value

    def type(self):
        if type(self.value) == int: return ASTNumberLiteralNode.NumberType['integer']
        if type(self.value) == float: return ASTNumberLiteralNode.NumberType['float']
        return None

class ASTUnaryOperatorNode(ASTNode):
    class Type(Enum):
        prefix = 1
        postfix = 2

        def __str__(self):
            if self == ASTUnaryOperatorNode.Type['prefix']: return "prefix"
            if self == ASTUnaryOperatorNode.Type['postfix']: return "postfix"
            return super(ASTUnaryOperatorNode.Type, self).__str__()

    def __init__(self, operatorType, label, parent=None):
        super(ASTUnaryOperatorNode, self).__init__(label, parent)
        self.operand = None
        self.operatorType = operatorType

    def setOperand(self, op):
        self.operand = op

    def getOperand(self):
        return self.operand

    def addChildNode(self, node):
        if self.operand is None:
            self.operand = node
        else:
            raise Exception("I don't want a second child, I'm a unary operator node!")
        node.parent = self

        return node

    def addChild(self, label):
        raise Exception("Don't call me, I'm a unary operator node!")

    def getChildren(self):
        children = []
        if self.operand is not None: children.append(self.operand)
        return children

class ASTBinaryOperatorNode(ASTNode):
    def __init__(self, label, parent=None):
        super(ASTBinaryOperatorNode, self).__init__(label, parent)
        self.firstOperand = None
        self.secondOperand = None

    def setFirstOperand(self, op):
        self.firstOperand = op

    def setSecondOperand(self, op):
        self.secondOperand = op

    def getFirstOperand(self):
        return self.firstOperand

    def getSecondOperand(self):
        return self.secondOperand

    def addChildNode(self, node):
        if self.firstOperand is None:
            self.firstOperand = node
        elif self.secondOperand is None:
            self.secondOperand = node
        else:
            raise Exception("I don't want a third child, I'm a binary operator node!")
        node.parent = self

        return node

    def addChild(self, label):
        raise Exception("Don't call me, I'm a binary operator node!")

    def getChildren(self):
        children = []
        if self.firstOperand is not None: children.append(self.firstOperand)
        if self.secondOperand is not None: children.append(self.secondOperand)
        return children

class ASTTernaryOperatorNode(ASTNode):
    def __init__(self, label, parent=None):
        super(ASTTernaryOperatorNode, self).__init__(label, parent)
        self.firstOperand = None
        self.secondOperand = None
        self.thirdOperand = None

    def setFirstOperand(self, op):
        self.firstOperand = op

    def setSecondOperand(self, op):
        self.secondOperand = op

    def setThirdOperand(self, op):
        self.thirdOperand = op

    def getFirstOperand(self):
        return self.firstOperand

    def getSecondOperand(self):
        return self.secondOperand

    def getThirdOperand(self):
        return self.thirdOperand

    def addChildNode(self, node):
        if self.firstOperand is None:
            self.firstOperand = node
        elif self.secondOperand is None:
            self.secondOperand = node
        elif self.thirdOperand is None:
            self.thirdOperand = node
        else:
            raise Exception("I don't want a fourth child, I'm a ternary operator node!")
        node.parent = self

        return node

    def addChild(self, label):
        raise Exception("Don't call me, I'm a ternary operator node!")

    def getChildren(self):
        children = []
        if self.firstOperand is not None: children.append(self.firstOperand)
        if self.secondOperand is not None: children.append(self.secondOperand)
        if self.thirdOperand is not None: children.append(self.thirdOperand)
        return children

class ASTTernaryConditionalOperatorNode(ASTTernaryOperatorNode):
    def __init__(self, parent=None):
        super(ASTTernaryConditionalOperatorNode, self).__init__("?:", parent)

class ASTSimpleAssignmentOperatorNode(ASTBinaryOperatorNode):
    def __init__(self, parent=None):
        super(ASTSimpleAssignmentOperatorNode, self).__init__("=", parent)

class ASTLogicOperatorNode(ASTBinaryOperatorNode):
    class LogicOperatorType(Enum):
        conj = 1
        disj = 2

        def __str__(self):
            if self == ASTLogicOperatorNode.LogicOperatorType['conj']: return "and"
            if self == ASTLogicOperatorNode.LogicOperatorType['disj']: return "or"
            return super(ASTLogicOperatorNode.LogicOperatorType, self).__str__()

    def __init__(self, logicOperatorType, parent=None):
        super(ASTLogicOperatorNode, self).__init__(str(logicOperatorType), parent)
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

    def __init__(self, comparisonType, parent=None):
        label = str(comparisonType)
        super(ASTComparisonOperatorNode, self).__init__(label, parent)
        self.comparisonType = comparisonType

class ASTUnaryArithmeticOperatorNode(ASTUnaryOperatorNode):
    class ArithmeticType(Enum):
        increment = 1
        decrement = 2

        def __str__(self):
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['increment']: return "++"
            if self == ASTUnaryArithmeticOperatorNode.ArithmeticType['decrement']: return "--"
            return super(ASTUnaryArithmeticOperatorNode, self).__str__()

    def __init__(self, arithmeticType, operatorType, parent=None):
        super(ASTUnaryArithmeticOperatorNode, self).__init__(operatorType, str(arithmeticType) + "|" + str(operatorType))

class ASTAddressOfOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, parent=None):
        super(ASTAddressOfOperatorNode, self).__init__("&", ASTUnaryOperatorNode.Type['prefix'], parent)

class ASTDereferenceOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, parent=None):
        super(ASTDereferenceOperatorNode, self).__init__("*", ASTUnaryOperatorNode.Type['prefix'], parent)

class ASTLogicalNotOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, parent=None):
        super(ASTLogicOperatorNode, self).__init__("!", ASTUnaryOperatorNode.Type['prefix'], parent)

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

    def __init__(self, arithmeticType, parent=None):
        label = str(arithmeticType)
        ASTBinaryOperatorNode.__init__(self, label, parent)
        self.arithmeticType = arithmeticType




class AbstractSyntaxTree:

    def __init__(self, root=ASTNode("root")):
        self.root = root

    def __str__(self):
        return "AST:\n" + self.root.out()





# tests
if __name__=="__main__":
    root = ASTNode("root")

    one = root.addChild("child1")
    two = root.addChild("child2")

    three = one.addChild("three")

    four = two.addChild("four")
    five = two.addChild("five")

    three.addChild("six")

    ast = AbstractSyntaxTree(root)
    print (root.out())

    currentNode = root
    print (currentNode)
    print (currentNode.parent)
    currentNode = currentNode.addChild("bla")
    print (currentNode)
    print (currentNode.parent)
    currentNode = currentNode.addChild("blabla")
    print (currentNode)
    print (currentNode.parent)
    currentNode = currentNode.parent
    print (currentNode)
    print (currentNode.parent)
