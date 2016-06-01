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
            "boolean" : 0,
            "address" : 0
        }

        self.bin_arithm_op = {
            "+"  : "add",
            "-"  : "sub",
            "*"  : "mul",
            "/"  : "div",
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

    def pType(self, typeInfo):
        if typeInfo.indirections > 0:
            return self.p_types["address"]
        return self.p_types[typeInfo.basetype]

    def getLabel(self):
        self.current += 1
        return "l" + str(self.current)

    def __del__(self):
        self.outFile.close()


    def visitProgramNode(self, node):
        self.outFile.write("ldc i 0\n") # work/trash register
        self.outFile.write("ssp {0}\n".format(self.symbolTable.currentScope.getAddressCounter() + 1 + 5))

        # code for variables
        for variable in self.symbolTable.currentScope.addressedVariables:
            self.visitDeclaratorInitializerNode(variable.astnode)

        # sep k where k = max. depth local stack
        # self.outFile.write("sep 2147483646\n")

        self.outFile.write("mst 0\n")
        self.outFile.write("cup 0 function_main\n") #TODO: argc/argv
        self.outFile.write("hlt\n")

        # code for functions
        for child in node.children:
            if isinstance(child, ASTFunctionDefinitionNode):
                child.accept(self)


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

        # for variable in scope.addressedVariables:
            # TODO: distinguish arguments from local variables: arguments already placed on stack by caller
            # self.outFile.write("ldc {0} 0\n".format(self.p_types[variable.typeInfo.basetype]))

        # sep k where k = max. depth local stack
        # self.outFile.write("sep 1000\n")

        # label = self.getLabel()

        # TODO: extra: jump over optional sub procedures
        # TODO: extra: self.outFile.write("ujp {0}\n".format(label))
        # TODO: extra: code for optional sub procedures here

        # function body code
        # self.outFile.write("{0}:\n".format(label))
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
        self.visitFunctionDefinitionNode(node)


    # arguments are pushed on stack by the caller, type checking checks if everything is correct, so no code needed for function definition parameters
    def visitParametersNode(self, node):
        pass


    def visitParameterNode(self, node):
        # self.outFile.write("code\n")
        pass


    # TODO: check this with different codes (code_l, code_r and code_a)
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

    def visitStatementNode(self, node):
        self.visitChildren(node)
        self.outFile.write("ssp {0}\n".format(self.symbolTable.currentScope.getAddressCounter() + 1 + 5))


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


    # def visitElseNode(self, node):
    #     self.visitChildren(node)


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

        if hasInitializer:
            self.visitChildren(node)
        else:
            self.outFile.write("ldc {0} {1}\n".format(self.pType(node.getType()), self.initializers["address" if node.getType().indirections > 0 else node.getType().basetype]))

        self.outFile.write("str {0} 0 {1}\n".format(self.pType(node.getType()), node.symbolInfo.address + 5))


    def visitInitializerListNode(self, node):
        # children will cause data to be loaded onto the stack
        self.visitChildren(node)


    def visitIntegerLiteralNode(self, node):
        self.outFile.write("ldc i {0}\n".format(str(node.value)))


    def visitFloatLiteralNode(self, node):
        self.outFile.write("ldc f {0}\n".format(str(node.value)))


    def visitCharacterLiteralNode(self, node):
        self.outFile.write("ldc c {0}\n".format(str(node.value)))


    def visitStringLiteralNode(self, node):
        self.outFile.write("code string literal\n")


    def visitVariableNode(self, node):
        if self.lvalue and self.lvalue.pop():
            # put address on stack
            self.outFile.write("lda {0} {1}\n".format(self.symbolTable.functionDefinitionDepthDifference(node.symbolInfo), node.symbolInfo.address + 5))
        elif node.getType().indirections != 0:
            self.outFile.write("lod a 0 {0}\n".format(node.symbolInfo.address + 5))
        else:
            # put value on stack
            self.outFile.write("lod {0} 0 {1}\n".format(self.pType(node.getType()), node.symbolInfo.address + 5))

        self.visitChildren(node)


    def visitFunctionCallNode(self, node):
        # organizational block
        self.outFile.write("mst {0}\n".format(self.symbolTable.currentDepth))

        # evaluate arguments
        self.visitChildren(node)

        # call user procedure
        self.outFile.write("cup {0} function_{1}\n".format(len(node.children[0].children), node.definitionNode.identifier))


    def visitTernaryConditionalOperatorNode(self, node):
        self.visitIfNode(node)


    def visitSimpleAssignmentOperatorNode(self, node):
        # children of a = b: [ASTVariableNode, ExpressionNode]
        self.lvalue.append(True)
        node.children[0].accept(self)
        self.outFile.write("dpl a\n") # duplicate the address to load it after the assignment
        node.children[1].accept(self)

        self.outFile.write("sto {0}\n".format(self.pType(node.children[0].getType())))
        self.outFile.write("ind {0}\n".format(self.pType(node.children[0].getType())))


    def visitLogicOperatorNode(self, node):
        self.visitChildren(node)
        self.outFile.write(str(node.logicOperatorType) + "\n")


    def visitComparisonOperatorNode(self, node):
        self.visitChildren(node)
        self.outFile.write("{0} {1}\n".format(self.bin_comp_op[str(node.comparisonType)], self.p_types[node.children[0].getType().basetype]))


    def visitUnaryArithmeticOperatorNode(self, node):
        op = str(node.arithmeticType)
        ttype = self.pType(node.children[0].getType())

        if op == "++" or op == "--":
            self.lvalue.append(True)
        self.visitChildren(node)
        if op == "++" or op == "--":
            self.outFile.write("dpl a\ndpl a\n")
            maininstr = "inc"
            secinstr = "dec"
            if op == "--":
                maininstr, secinstr = secinstr, maininstr

            self.outFile.write("ind {0}\n".format(ttype))
            self.outFile.write("{0} {1} 1\n".format(maininstr, ttype))
            self.outFile.write("sto {0}\n".format(ttype))
            self.outFile.write("ind {0}\n".format(ttype))
            if node.operatorType == ASTUnaryOperatorNode.Type['postfix']:
                self.outFile.write("{0} {1} 1\n".format(secinstr, ttype))

        if op == "-":
            self.outFile.write("neg {0}\n".format(ttype))
        elif op == "+":
            pass


    def visitAddressOfoperatorNode(self, node):
        self.lvalue.append(True)
        if isinstance(node.children[0], ASTDereferenceOperatorNode):
            self.visitChildren(node.children[0])
        self.visitChildren(node)


    def visitDereferenceNode(self, node):
        # if isinstance(node.parent, ASTSimpleAssignmentOperatorNode) and self is node.parent.children[0]:
        #     self.lvalue.push(True)
        self.visitChildren(node)

        if isinstance(node.parent, ASTSimpleAssignmentOperatorNode) and node is node.parent.children[0]:
            self.outFile.write("ind a\n")
        else:
            self.outFile.write("ind {0}\n".format(self.pType(node.getType())))


    def visitLogicalNotOperatorNode(self, node):
        self.outFile.write("code logical not op\n")
        self.visitChildren(node)
        self.outFile.write("not {0}\n".format(self.p_types[node.children[0].getType().basetype]))


    def visitArraySubscriptNode(self, node):
        self.outFile.write("code array subscript op\n")
        self.visitChildren(node)


    def visitBinaryArithmeticNode(self, node):
        if node.arithmeticType == ASTBinaryArithmeticOperatorNode.ArithmeticType['modulo']:
            node.children[0].accept(self)
            self.outFile.write("dpl i\n")
            self.outFile.write("ldc a 0\n")
            node.children[1].accept(self)
            self.outFile.write("sto i\nldc a 0\nind i\ndiv i\nldc a 0\nind i\nmul i\nsub i\n")
        else:
            self.visitChildren(node)
            self.outFile.write("{0} {1}\n".format(self.bin_arithm_op[str(node.arithmeticType)], self.p_types[node.children[0].getType().basetype]))
