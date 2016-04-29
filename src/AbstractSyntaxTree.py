import copy
from enum import Enum
from TypeInfo import TypeInfo
from CompilerErrorHandler import CompilerErrorHandler
from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNode

offset = "  | "

class ASTNode(object):

    def __init__(self, label="no label", ctx=None):
        self.tree = None
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

    def typeCheck(self):
        for child in self.children:
            child.typeCheck()

    @property
    def errorHandler(self):
        return self.tree.errorHandler if self.tree is not None else None

    def getRelevantToken(self):
        return self.getFirstToken()

    def getFirstToken(self, node=None): # node = context node, not AST node
        # TODO: rewrite please
        if node is None: node = self.ctx
        if node is None:
            raise Exception(str(type(self)) + "'s ctx was not set")
        if isinstance(node, TerminalNode):
            return node.getSymbol()
        for child in node.getChildren():
            if isinstance(child, TerminalNode):
                return child.getSymbol()
            else:
                result = self.getFirstToken(child)
                if result is not None:
                    return result

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

class ASTIncludeNode(ASTNode):
    def __init__(self, isStdInclude=False, name="include name", ctx=None):
        super(ASTIncludeNode, self).__init__("include - " + name, ctx)
        self.isStdInclude = isStdInclude
        self.name = name

class ASTMainFunctionNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTMainFunctionNode, self).__init__("main", ctx)

class ASTFunctionDeclarationNode(ASTNode):
    def __init__(self, label="function declaration", ctx=None):
        super(ASTFunctionDeclarationNode, self).__init__(label, ctx)
        self.type = None
        self.identifier = None
        # parameters are child nodes

    def getType(self):
        if self.type is None:
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("ASTFunctionDeclarationNode type not filled in", line, column)
        return TypeInfo(rvalue=None, basetype=self.type)

    def getParameters(self):
        for child in self.children:
            if isinstance(child, ASTParametersNode):
                return child
        return None

    def out(self, level):
        s = offset * level + self.label + "\n"
        s += offset * (level + 1) + "return type: " + str(self.type) + "\n"
        s += offset * (level + 1) + "identifier:  " + str(self.identifier) + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTFunctionDefinitionNode(ASTFunctionDeclarationNode):
    def __init__(self, ctx=None):
        super(ASTFunctionDefinitionNode, self).__init__("function definition", ctx)
        # parameters and statements are child nodes

class ASTParametersNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTParametersNode, self).__init__("parameters", ctx)

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
        self.type = None
        self.identifier = None
        self.isArray = False
        self.arrayLength = None
        # TODO: arrayLength can be an expressionNode -> change # done i think; check if member can be removed
        self.const = []
        self.indirections = 0

    def getType(self):
        if self.type is None:
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("ASTParameterNode type not filled in", line, column)
        return TypeInfo(rvalue=None, basetype=self.type, indirections=self.indirections, const=self.const)

    def __eq__(self, other):
        return self.type == other.type \
            and self.isArray == other.isArray \
            and self.const == other.const \
            and self.indirections == other.indirections
        # and self.arrayLength == other.arrayLength # if checking arrayLength, need to check possible expression child equality

    def getRelevantToken(self):
        for child in self.ctx.getChildren():
            if isinstance(child, CommonToken):
                return child
        return None

    def out(self, level):
        s = offset * level + "parameter" + " - " + str(self.type)

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
    def __init__(self, ctx=None):
        super(ASTArgumentsNode, self).__init__("arguments", ctx)


'''
    STATEMENTS
'''


class ASTStatementsNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTStatementsNode, self).__init__("statements", ctx)

class ASTStatementNode(ASTNode):
    def __init__(self, label="statement", ctx=None):
        super(ASTStatementNode, self).__init__(label, ctx)

class ASTReturnNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTReturnNode, self).__init__("return", ctx)

class ASTIfNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTIfNode, self).__init__("if", ctx)
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
    def __init__(self, ctx=None):
        super(ASTElseNode, self).__init__("else", ctx)

class ASTWhileNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTWhileNode, self).__init__("while", ctx)

class ASTDoWhileNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTDoWhileNode, self).__init__("doWhile", ctx)

class ASTVariableDeclarationNode(ASTStatementNode):
    def __init__(self, ctx=None):
        super(ASTVariableDeclarationNode, self).__init__("variable declaration", ctx)
        self.type = None
        self.isConstant = False
        # declaratorInitializers are children

    def getRelevantToken(self):
        # TODO: point to specific parts of declaration node
        super(ASTVariableDeclarationNode, self).getRelevantToken()

    def out(self, level):
        s  = offset * level + self.label + "\n"
        s += offset * (level + 1) + "type: " + str(self.type)
        s += ", const: " + str(self.isConstant) + "\n"

        return s if (not self.children) else self.outChildren(s, level)

class ASTDeclaratorInitializerNode(ASTNode):
    def __init__(self, ctx=None):
        super(ASTDeclaratorInitializerNode, self).__init__("declarator initializer", ctx)
        self.identifier = None
        self.isArray = False
        self.indirections = 0
        self.const = []
        # if arrayParameter hasArrayLength -> first child is array length, else it is initializationValue
        self.hasArrayLength = False
        # arrayLength will be an expressionNode child
        # TODO: dont't allow const variable declaration without initial value

    def typeCheck(self):
        childIndex = None
        if len(self.children) == 1 and not self.hasArrayLength:
            childIndex = 0
        elif len(self.children) == 2:
            childIndex = 1

        ownType = copy.deepcopy(self.getType())
        if ownType.isArray:
            ownType.isArray = False
            ownType.indirections -= 1

        if childIndex is not None:

            if isinstance(self.children[childIndex], ASTArgumentsNode): # type check array elements
                for argument in self.children[childIndex].children:
                    if not ownType.isCompatible(argument.getType(), ignoreRvalue=True, ignoreConst=True):
                        line, column = self.getLineAndColumn()
                        self.errorHandler.addError("Variable initialization must have the same type (have " + str(ownType) + " and " + str(argument.getType()) + ")", line, column)
            else: # type check non-array elements
                if not ownType.isCompatible(self.children[childIndex].getType(), ignoreRvalue=True, ignoreConst=True):
                    line, column = self.getLineAndColumn()
                    self.errorHandler.addError("Variable initialization must have the same type (have " + str(ownType) + " and " + str(self.children[childIndex].getType()) + ")", line, column)
        else:
            return

    def getType(self):
        return TypeInfo(rvalue=None, basetype=self.parent.type, indirections=self.indirections, const=[self.parent.isConstant] + self.const, isArray=self.isArray)

    def out(self, level):
        s = offset * level + "declarator initializer" + "\n"

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
    def __init__(self, label="expression", ctx=None):
        super(ASTExpressionNode, self).__init__(label, ctx)

    def typeCheck(self):
        return NotImplementedError

    def getType(self):
        raise NotImplementedError

class ASTIntegerLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTIntegerLiteralNode, self).__init__("int", ctx)
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTFloatLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTFloatLiteralNode, self).__init__("float", ctx)
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="float")

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTCharacterLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTCharacterLiteralNode, self).__init__("char", ctx)
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="char")

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTStringLiteralNode(ASTExpressionNode):
    def __init__(self, value, ctx=None):
        super(ASTStringLiteralNode, self).__init__("string", ctx)
        self.value = value

    def typeCheck(self):
        return True

    def getType(self):
        return TypeInfo(rvalue=True, basetype="char", indirections=1, const=[False], isArray=True)

    def out(self, level):
        return offset * level + self.label + " - " + str(self.value) + "\n"

class ASTVariableNode(ASTExpressionNode):
    def __init__(self, identifier, ctx=None):
        super(ASTVariableNode, self).__init__("variable", ctx)
        self.identifier = identifier
        self.type = None

    def typeCheck(self):
        return True

    def getType(self):
        if self.type is None:
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Type has not been set yet for variable " + self.identifier, line, column)
        return self.type

    def out(self, level):
        return offset * level + self.label + " - " + self.identifier + "\n"

class ASTFunctionCallNode(ASTExpressionNode):
    def __init__(self, ctx=None):
        super(ASTFunctionCallNode, self).__init__("function call", ctx)
        self.identifier = None
        self.definitionNode = None
        self.errorParameter = None

    def typeCheck(self):
        parameterNodes = self.definitionNode.getParameters().children
        arguments = None
        for child in self.children:
            if isinstance(child, ASTArgumentsNode):
                arguments = child
                break
        if arguments is not None:
            if len(arguments.children) != len(parameterNodes):
                line, column = self.getLineAndColumn()
                self.errorHandler.addError("Number of arguments to function {0} does not match definition (have {1}, need {2})" \
                    .format(self.identifier, len(arguments.children), len(parameterNodes)), line, column)
            for i, argument in enumerate(arguments.children):
                if not argument.getType().isCompatible(parameterNodes[i].getType(), ignoreRvalue=True, ignoreConst=True):
                    self.errorParameter = i
                    line, column = self.getLineAndColumn()
                    self.errorHandler.addError("Arguments to function '{0}' don't match: {1} vs {2}".format(self.identifier, str(argument.getType()), str(parameterNodes[i].getType())), line, column)
        else:
            raise Exception("Did not find arguments node in ASTFunctionCallNode")
        #TODO check constness of arguments/parameters

    def getType(self):
        if self.definitionNode is None:
            raise Exception("definitionNode has not been set yet for function " + self.identifier)
        return self.definitionNode.getType()

    def getRelevantToken(self):
        if self.errorParameter is not None:
            return self.getFirstToken(list(list(self.ctx.getChildren())[2].getChildren())[2 * self.errorParameter])
        return super(ASTFunctionCallNode, self).getRelevantToken()

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

    def __init__(self, label, operatorType, ctx):
        super(ASTUnaryOperatorNode, self).__init__(label, ctx)
        self.operatorType = operatorType

    def addChildNode(self, node):
        if len(self.children) >= 1: # this should never happen
            raise Exception("ASTUnaryOperatorNode cannot have more than one child")
        return super(ASTUnaryOperatorNode, self).addChildNode(node)

    def typeCheck(self):
        return self.children[0].typeCheck()

    def getType(self):
        return self.children[0].getType()

class ASTBinaryOperatorNode(ASTExpressionNode):
    def __init__(self, label, ctx=None):
        super(ASTBinaryOperatorNode, self).__init__(label, ctx)

    def typeCheck(self):
        for child in self.children:
            child.typeCheck()

        if not self.children[0].getType().isCompatible(self.children[1].getType()):
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Binary operator operands must have the same type (have " + str(self.children[0].getType()) + " and " + str(self.children[1].getType()) + ")", line, column)

    def getType(self):
        return self.children[0].getType()

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

    def typeCheck(self):
        for child in self.children:
            child.typeCheck()

        if not self.children[0].getType().isCompatible(TypeInfo(rvalue=None, basetype="int"), ignoreRvalue=True):
            self.errorOperand = 0
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Ternary conditional operator needs int as first operand", line, column)
        if self.children[1].getType() != self.children[2].getType():
            self.errorOperand = 1
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Ternary conditional operator alternatives should be of equal type", line, column)
        return True

    def getRelevantToken(self):
            return self.getFirstToken(list(self.ctx.getChildren())[self.errorOperand * 2])

    def getType():
        return self.children[1].getType()

class ASTSimpleAssignmentOperatorNode(ASTBinaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTSimpleAssignmentOperatorNode, self).__init__("=", ctx)

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

    def typeCheck(self):
        for child in self.children:
            child.typeCheck()

        if self.children[0].getType() != self.children[1].getType():
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Logic operator operands must have the same type (have " + str(self.children[0].getType()) + " and " + str(self.children[1].getType()) + ")", line, column)
        if not self.children[0].getType().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Logic operator operands not compatible with int", line, column)

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

    def typeCheck(self):
        for child in self.children:
            child.typeCheck()

        if not self.children[0].getType().equals(self.children[1].getType(), ignoreConst=True):
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Comparison operator operands need to be of same type (have " + str(self.children[0].getType()) + " and " + str(self.children[1].getType()) + ")", line, column)
        return True

    def getRelevantToken(self):
        return list(self.ctx.getChildren())[1].getSymbol()

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

    def __init__(self, arithmeticType, operatorType, ctx=None):
        super(ASTUnaryArithmeticOperatorNode, self).__init__(str(arithmeticType) + " - " + str(operatorType), str(operatorType), ctx)

class ASTAddressOfOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTAddressOfOperatorNode, self).__init__("&", ASTUnaryOperatorNode.Type['prefix'], ctx)

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections += 1
        return ttype

class ASTDereferenceOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTDereferenceOperatorNode, self).__init__("*", ASTUnaryOperatorNode.Type['prefix'], ctx)

    def typeCheck(self):
        self.getType()

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections -= 1
        if ttype.indirections < 0:
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("invalid type argument of unary '*' (have '" + str(ttype) + "')", line, column)
        elif ttype.indirections == 0:
            ttype.isArray = False
        return ttype

    def getRelevantToken(self):
        return self.getFirstToken(list(self.ctx.getChildren())[1])

class ASTLogicalNotOperatorNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTLogicalNotOperatorNode, self).__init__("!", ASTUnaryOperatorNode.Type['prefix'], ctx)

    def typeCheck(self):
        self.children[0].typeCheck()

        if not self.children[0].getType().isCompatible(TypeInfo(rvalue=True, basetype="int"), ignoreRvalue=True):
            line, column = self.getLineAndColumn()
            self.errorHandler.addError("Logical not operator operand not compatible with int", line, column)

    def getType(self):
        return TypeInfo(rvalue=True, basetype="int")

class ASTArraySubscriptNode(ASTUnaryOperatorNode):
    def __init__(self, ctx=None):
        super(ASTArraySubscriptNode, self).__init__("[]", ASTUnaryOperatorNode.Type['postfix'], ctx)

    def getType(self):
        ttype = copy.deepcopy(self.children[0].getType())
        ttype.indirections -= 1
        if ttype.indirections == 0:
            ttype.isArray = False
        return ttype

    def addChildNode(self, node):
        if len(self.children) <= 2:
            return ASTNode.addChildNode(self, node)

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

    def __init__(self, arithmeticType, ctx=None):
        label = str(arithmeticType)
        ASTBinaryOperatorNode.__init__(self, label, ctx)
        self.arithmeticType = arithmeticType


'''
    AST
'''

class AbstractSyntaxTree:

    def __init__(self, errorHandler=None):
        self.errorHandler = errorHandler
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

    def typeCheck(self):
        self.root.typeCheck()
