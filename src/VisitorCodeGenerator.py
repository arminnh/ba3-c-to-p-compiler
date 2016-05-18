from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *

class VisitorCodeGenerator(Visitor):

    def __init__(self, symbolTable, outFile="out.p"):
        self.symbolTable = symbolTable
        self.current = 0
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

    def getLabel(self):
        self.current += 1
        return "l" + str(self.current)

    def __del__(self):
        self.outFile.close()


    def visitProgramNode(self, node):
        # self.outFile.write("code\n")
        # self.outFile.write("ujp  lmain\n")
        self.outFile.write("ujp main\n")
        self.visitChildren(node)


    def visitIncludeNode(self, node):
        # self.outFile.write("code\n")
        self.visitChildren(node)


    def visitFunctionDeclarationNode(self, node):
        # self.outFile.write("code\n")
        self.visitChildren(node)


    def visitFunctionDefinitionNode(self, node):
        self.symbolTable.openScope(isFunctionScope=True, name=node.identifier)
        scope = self.symbolTable.currentScope

        # function label
        self.outFile.write("\nfunction_{0}:\n".format(node.identifier))

        # set SP to
        self.outFile.write("ssp {0}\n".format(self.symbolTable.currentScope.getAddressCounter() + 1 + 5))

        for variable in scope.addressedVariables:
            # distinguish arguments from local variables: arguments already placed on stack by caller
            self.outFile.write("ldc {0} 0\n".format(self.p_types[variable.typeInfo.basetype]))

        # sep k where k = max. depth local stack
        self.outFile.write("sep 1000\n")

        label = self.getLabel()

        # jump over optional sub procedures
        self.outFile.write("ujp {0}\n".format(label))
        # TODO: extra: code for optional sub procedures here

        # function body code
        self.outFile.write("{0}:\n".format(label))
        for child in node.children:
            if not isinstance(child, ASTParametersNode):
                child.accept(self)

        # return from function
        if node.getType().basetype == "void" and node.getType().indirections == 0:
            self.outFile.write("retp\n")
        else:
            self.outFile.write("retf\n")

        self.symbolTable.closeScope()


    def visitMainFunctionNode(self, node):
        # self.outFile.write("\nlmain:\n")
        self.symbolTable.openScope(isFunctionScope=True, name=node.identifier)
        self.outFile.write("\nmain:\n")
        for i in range(len(self.symbolTable.currentScope.addressedVariables)):
            self.outFile.write("ldc {0} 0\n".format(self.p_types[self.symbolTable.currentScope.addressedVariables[i].typeInfo.basetype]))
        self.visitChildren(node)
        self.outFile.write("hlt\n")
        self.symbolTable.closeScope()


    def visitParametersNode(self, node):
        self.visitChildren(node)


    def visitParameterNode(self, node):
        # self.outFile.write("code\n")
        self.visitChildren(node)


    def visitArgumentsNode(self, node):
        for child in node.children:
            if isinstance(child, ASTVariableNode):
                if child.getType().indirections > 0:
                    self.lvalue.append(True)
                    child.accept(self)
                else:
                    child.accept(self)
            else:
                child.accept(self)


    def visitStatementsNode(self, node):
        # self.outFile.write("code\n")
        openedScope = False
        if not isinstance(node.parent, ASTFunctionDefinitionNode):
            self.symbolTable.openScope()
            openedScope = True
        self.visitChildren(node)
        if openedScope:
            self.symbolTable.closeScope()
        # for ttype in self.symbolTable.getVariables(node):
        #     self.outFile.write("ldc {0} {1}".format(self.p_type[ttype], self.initializers[ttype]))

    def visitReturnNode(self, node):
        if not node.children:
            self.outFile.write("retp\n")
            return

        self.visitChildren(node) # TODO: make sure this takes the r value
        self.outFile.write("str {0} 0 0\n".format(self.p_types[node.children[0].getType().basetype]))
        self.outFile.write("retf\n") # note: this was not in the compendium


    def visitIfNode(self, node):
        elseLabel = self.getLabel()
        afterLabel = self.getLabel()

        node.children[0].accept(self)                            # condition
        self.outFile.write("fjp {0}\n".format(elseLabel))        # if top == false, jump over the 'then' code
        node.children[1].accept(self)                            # 'then'

        if len(node.children) == 3:                              # optional else
            self.outFile.write("ujp {0}\n".format(afterLabel))   # jump over the 'else' code if coming from 'then'
            self.outFile.write("{0}:\n".format(elseLabel))
            node.children[2].accept(self)                        # else
            self.outFile.write("{0}:\n".format(afterLabel))
        else:
            self.outFile.write("{0}:\n".format(elseLabel))


    def visitElseNode(self, node):
        self.visitChildren(node)


    def visitWhileNode(self, node):
        conditionLabel = self.getLabel()
        afterLabel = self.getLabel()
        self.outFile.write("{0}:\n".format(conditionLabel))
        node.children[0].accept(self)                            # condition
        self.outFile.write("fjp {0}\n".format(afterLabel))       # if top == false, jump over the loop code
        node.children[1].accept(self)                            # loop code
        self.outFile.write("ujp {0}\n".format(conditionLabel))   # jump back to the condition
        self.outFile.write("{0}:\n".format(afterLabel))


    def visitDoWhileNode(self, node): #TODO: test this
        conditionLabel = self.getLabel()
        afterLabel = self.getLabel()

        node.children[1].accept(self)                            # loop code

        self.outFile.write("{0}:\n".format(conditionLabel))
        node.children[0].accept(self)                            # condition
        self.outFile.write("fjp {0}\n".format(afterLabel))       # if top == false, jump over the loop code
        node.children[1].accept(self)                            # loop code
        self.outFile.write("ujp {0}\n".format(conditionLabel))   # jump back to the condition
        self.outFile.write("{0}:\n".format(afterLabel))


    def visitVariableDeclarationNode(self, node):
        # nothing here, handled by declaratorInitializer
        self.visitChildren(node)


    def visitDeclaratorInitializerNode(self, node):
        hasInitializer = False
        for child in node.children:
            if isinstance(child, ASTInitializerListNode):
                hasInitializer = True

        self.outFile.write("ldc a {0}\n".format(node.symbolInfo.address))

        if hasInitializer:
            self.visitChildren(node)
        else:
            self.outFile.write("ldc {0} {1}\n".format(self.p_types[node.getType().basetype], self.initializers[node.getType().basetype]))

        self.outFile.write("sto {0}\n".format(self.p_types[node.getType().basetype]))


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
        self.outFile.write("code string literal\n")


    def visitVariableNode(self, node):
        if self.lvalue and self.lvalue.pop():
            self.outFile.write("ldc a {0}\n".format(node.symbolInfo.address))
        else:
            self.outFile.write("ldc a {0}\n".format(node.symbolInfo.address))
            self.outFile.write("ind {0}\n".format(self.p_types[node.getType().basetype]))

        self.visitChildren(node)


    def visitFunctionCallNode(self, node):
        # organizational block
        self.outFile.write("mst 0\n")

        # evaluate arguments
        self.visitChildren(node)

        # call user procedure
        self.outFile.write("cup {0} function_{1}\n".format(len(node.children[0].children), node.definitionNode.identifier))


    def visitTernaryConditionalOperatorNode(self, node):
        self.outFile.write("code ternary cond\n")
        self.visitChildren(node)


    def visitSimpleAssignmentOperatorNode(self, node):
        # children of a = b: [ASTVariableNode, ExpressionNode]
        self.lvalue.append(True)
        node.children[0].accept(self)
        self.outFile.write("dpl a\n") # duplicate the address to load it after the assignment
        node.children[1].accept(self)
        self.outFile.write("sto {0}\n".format(self.p_types[node.children[0].getType().basetype]))
        self.outFile.write("ind {0}\n".format(self.p_types[node.children[0].getType().basetype]))


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

            # self.outFile.write("ldc i 1\n")
            # self.outFile.write("add i\n")
            pass
        elif op == "--":
            self.outFile.write("UNARY ARITHMETIC" + op + "\n")

    def visitAddressOfoperatorNode(self, node):
        self.outFile.write("code address of op\n")
        self.visitChildren(node)


    def visitDereferenceNode(self, node):
        self.outFile.write("code dereference op\n")
        self.visitChildren(node)


    def visitLogicalNotOperatorNode(self, node):
        self.outFile.write("code logical not op\n")
        self.visitChildren(node)
        self.outFile.write("not " + self.p_types[node.children[0].getType().basetype] + "\n")


    def visitArraySubscriptNode(self, node):
        self.outFile.write("code array subscript op\n")
        self.visitChildren(node)


    def visitBinaryArithmeticNode(self, node):
        self.visitChildren(node)
        self.outFile.write(self.bin_arithm_op[str(node.arithmeticType)] + " " + self.p_types[node.children[0].getType().basetype] + "\n")
