from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorCodeGenerator(Visitor):

    def __init__(self, outfile="out.p"):
        self.outFile = open(outfile, 'w')

        self.p_types = {
            "int"     : "i",
            "float"   : "r",
            "char"    : "c",
            "numeric" : "N",
            "type"    : "T",
            "boolean" : "b"
        }

        self.bin_arithm_op = {
            "+"  : "add",
            "-"  : "sub",
            "*"  : "mul",
            "/"  : "div",
            "%"  : "MODULO",
        }

        self.bin_comp_op = {
            "<" : "les",
            ">" : "grt",
            "<=" : "leq",
            ">=" : "geq",
            "==" : "equ",
            "!=" : "neq",
        }

        # - => neg
        # =
        # and -> and
        # or -> or
        # ! -> not


    def visitProgramNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)
        self.outFile.write("hlt\n")


    def visitIncludeNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitFunctionDeclarationNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitFunctionDefinitionNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitMainFunctionNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitParametersNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitParameterNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitArgumentsNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitInitializerListNode(self, node):
        self.outFile.write("code initializer list \n")
        self.visitChildren(node)


    def visitStatementsNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitReturnNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitIfNode(self, node):
        self.outFile.write("code if \n")
        self.visitChildren(node)


    def visitElseNode(self, node):
        self.outFile.write("code else \n")
        self.visitChildren(node)


    def visitWhileNode(self, node):
        self.outFile.write("code while \n")
        self.visitChildren(node)


    def visitDoWhileNode(self, node):
        self.outFile.write("code do while \n")
        self.visitChildren(node)


    def visitVariableDeclarationNode(self, node):
        self.outFile.write("code variable decl \n")
        self.visitChildren(node)


    def visitDeclaratorInitializerNode(self, node):
        self.outFile.write("code decl initializer \n")
        self.visitChildren(node)


    def visitIntegerLiteralNode(self, node):
        self.outFile.write("ldc i " + str(node.value) + "\n")


    def visitFloatLiteralNode(self, node):
        self.outFile.write("ldc f " + str(node.value) + "\n")


    def visitCharacterLiteralNode(self, node):
        self.outFile.write("ldc c " + str(node.value) + "\n")


    def visitStringLiteralNode(self, node):
        self.outFile.write("code string literal \n")


    def visitVariableNode(self, node):
        self.outFile.write("code variable \n")
        self.visitChildren(node)


    def visitFunctionCallNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitTernaryConditionalOperatorNode(self, node):
        self.outFile.write("code ternary cond \n")
        self.visitChildren(node)


    def visitSimpleAssignmentOperatorNode(self, node):
        self.outFile.write("code simple assignment \n")
        self.visitChildren(node)


    def visitLogicOperatorNode(self, node):
        self.outFile.write("code logic op \n")
        self.visitChildren(node)
        self.outFile.write(str(node.logicOperatorType) + " " + self.p_types[node.children[0].getType().basetype] + "\n")


    def visitComparisonOperatorNode(self, node):
        self.outFile.write("code comp op \n")
        self.visitChildren(node)
        self.outFile.write(self.bin_comp_op[str(node.comparisonType)] + " " + self.p_types[node.children[0].getType().basetype] + "\n")


    def visitUnaryArithmeticOperatorNode(self, node):
        self.visitChildren(node)
        if str(node.arithmeticType) == "-":
            self.outFile.write("neg")
        else:
            self.outFile.write("UNARY ARITHMETIC")

    def visitAddressOfoperatorNode(self, node):
        self.outFile.write("code address of op \n")
        self.visitChildren(node)


    def visitDereferenceNode(self, node):
        self.outFile.write("code dereference op \n")
        self.visitChildren(node)


    def visitLogicalNotOperatorNode(self, node):
        self.outFile.write("code logical not op \n")
        self.visitChildren(node)
        self.outFile.write("not " + self.p_types[node.children[0].getType().basetype] + "\n")


    def visitArraySubscriptNode(self, node):
        self.outFile.write("code array subscript op \n")
        self.visitChildren(node)


    def visitBinaryArithmeticNode(self, node):
        self.visitChildren(node)
        self.outFile.write(self.bin_arithm_op[str(node.arithmeticType)] + " " + self.p_types[node.children[0].getType().basetype] + "\n")
