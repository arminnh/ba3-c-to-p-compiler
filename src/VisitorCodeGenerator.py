from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorCodeGenerator(Visitor):

    def __init__(self, outFile="out.p"):
        self.lvalue = []
        self.outFile = open(outFile, 'w')

        self.p_types = {
            "address" : "a",
            "int"     : "i",
            "float"   : "r",
            "char"    : "c",
            "numeric" : "N",
            "type"    : "T",
            "boolean" : "b"
        }

        self.initializers = {
            "int"     : 0,
            "float"   : 0.0,
            "char"    : 'c',
            "boolean" : 0
        }

        self.bin_arithm_op = {
            "+"  : "add",
            "-"  : "sub",
            "*"  : "mul",
            "/"  : "div",
            "%"  : "MODULO"
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

    def __del__(self):
        self.outFile.close()


    def visitProgramNode(self, node):
        # self.outFile.write("code \n")
        # self.outFile.write("ujp  lmain\n")
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
        # self.outFile.write("\nlmain: \n")
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


    def visitStatementsNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitReturnNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitIfNode(self, node):
        node.children[0].accept(self)        # condition
        self.outFile.write("fjp l1 \n")      # if top == false, jump over the 'then' code
        node.children[1].accept(self)        # 'then'

        if len(node.children) == 3:          # optional else
            self.outFile.write("ujp l2 \n")  # jump over the 'else' code if coming from 'then'
            self.outFile.write("l1: \n")
            node.children[2].accept(self)    # else
            self.outFile.write("l2: \n")
        else:
            self.outFile.write("l1: \n")


    def visitElseNode(self, node):
        self.visitChildren(node)


    def visitWhileNode(self, node):
        self.outFile.write("l1: \n")
        node.children[0].accept(self)   # condition
        self.outFile.write("fjp l2 \n") # if top == false, jump over the loop code
        node.children[1].accept(self)   # loop code
        self.outFile.write("ujp l1 \n") # jump back to the condition
        self.outFile.write("l2: \n")


    def visitDoWhileNode(self, node): #TODO: test this
        node.children[1].accept(self)   # loop code

        self.outFile.write("l1: \n")
        node.children[0].accept(self)   # condition
        self.outFile.write("fjp l2 \n") # if top == false, jump over the loop code
        node.children[1].accept(self)   # loop code
        self.outFile.write("ujp l1 \n") # jump back to the condition
        self.outFile.write("l2: \n")


    def visitVariableDeclarationNode(self, node):
        # nothing here, handled by declaratorInitializer
        self.visitChildren(node)


    def visitDeclaratorInitializerNode(self, node):
        hasInitializer = False
        for child in node.children:
            if isinstance(child, ASTInitializerListNode):
                hasInitializer = True

        if hasInitializer:
            self.visitChildren(node)
        else:
            self.outFile.write("ldc {0} {1}\n".format(self.p_types[node.getType().basetype], self.initializers[node.getType().basetype]))


    def visitInitializerListNode(self, node):
        # children will cause data to be loaded onto the stack
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
        if self.lvalue and self.lvalue.pop():
            self.outFile.write("ldc a 0\n") # TODO
        else:
            self.outFile.write("ldc a 0\n") # TODO
            self.outFile.write("ind {0}\n".format(self.p_types[node.getType().basetype])) # TODO
            # self.outFile.write("ind {0}\n".format(self.p_types[node.getType().basetype])) # TODO

        self.visitChildren(node)


    def visitFunctionCallNode(self, node):
        # self.outFile.write("code \n")
        self.visitChildren(node)


    def visitTernaryConditionalOperatorNode(self, node):
        self.outFile.write("code ternary cond \n")
        self.visitChildren(node)


    def visitSimpleAssignmentOperatorNode(self, node):
        self.lvalue.append(True)
        # node.children[0].accept(self)
        self.visitChildren(node)
        self.outFile.write("sto " + self.p_types[node.children[0].getType().basetype] + "\n")


    def visitLogicOperatorNode(self, node):
        self.visitChildren(node)
        self.outFile.write(str(node.logicOperatorType) + "\n")


    def visitComparisonOperatorNode(self, node):
        self.visitChildren(node)
        self.outFile.write(self.bin_comp_op[str(node.comparisonType)] + " " + self.p_types[node.children[0].getType().basetype] + "\n")


    def visitUnaryArithmeticOperatorNode(self, node):
        op = str(node.arithmeticType)
        self.visitChildren(node)
        if op == "-":
            self.outFile.write("neg " + self.p_types[node.children[0].getType().basetype] +"\n")
        elif op == "+":
            pass
        elif op == "++":

            # self.outFile.write("ldc i 1 \n")
            # self.outFile.write("add i\n")
            pass
        elif op == "--":
            self.outFile.write("UNARY ARITHMETIC" + op + "\n")

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
