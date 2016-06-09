from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *
from TypeInfo import TYPES
import copy

class VisitorCodeGenerator(Visitor):

    def __init__(self, symbolTable, outFile="out.p"):
        self.symbolTable = symbolTable
        self.current = 0
        self._lvalue = []
        self.backLabels = []
        self.forwardLabels = []
        self.outFile = open(outFile, "w")

        self.p_types = {
            "address" : "a",
            "int"     : "i",
            "float"   : "r",
            "char"    : "c",
            "numeric" : "N",
            "type"    : "T",
            "boolean" : "b",
            "void"    : "a" # TODO: check what to actually do here
        }

        self.initializers = {
            "int"     : 0,
            "float"   : 0.0,
            "char"    : 0,
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

    def lvalue(self):
        if len(self._lvalue):
            return self._lvalue[-1]
        return False

    def rvalue(self):
        return not self.lvalue()

    def pType(self, typeInfo):
        if typeInfo.nrIndirections() > 0:
            return self.p_types["address"]
        return self.p_types[typeInfo.baseType]

    def getLabel(self):
        self.current += 1
        return "l" + str(self.current)

    def __del__(self):
        self.outFile.close()


    def visitProgramNode(self, node):
        self.outFile.write("ldc i 0\n") # work/trash register
        self.outFile.write("ldc i 0\nldc i 0\n") # work registers
        self.outFile.write("ssp {0}\n".format(self.symbolTable.currentScope.getAddressCounter() + 5))

        # code for string literals
        for string, symbolInfo in sorted(self.symbolTable.stringLiterals.items()):
            for i, c in enumerate(string):
                self.outFile.write("lda 0 {0}\n".format(symbolInfo.address + i + 5))

                self.outFile.write("ldc c {0}\n".format(repr(c) if c != '\'' else "'\''"))
                self.outFile.write("sto c\n")

            if len(string) > 2:
                self.outFile.write("lda 0 {0}\n".format(symbolInfo.address + len(string) + 5))
                self.outFile.write("ldc c 27\n")
                self.outFile.write("sto c\n")

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
        self.outFile.write("ssp {0}\n".format(self.symbolTable.currentScope.getAddressCounter() + 5))

        # for variable in scope.addressedVariables:
            # TODO: distinguish arguments from local variables: arguments already placed on stack by caller
            # self.outFile.write("ldc {0} 0\n".format(self.p_types[variable.typeInfo.baseType]))

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
        if node.getType().baseType == "void" and node.getType().nrIndirections() == 0:
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
        pass


    # TODO: check this with different codes (code_l, code_r and code_a)
    def visitArgumentsNode(self, node):
        for child in node.children:
            if isinstance(child, ASTVariableNode):
                if child.getType().nrIndirections() > 0:
                    self._lvalue.append(True)
                    child.accept(self)
                    self._lvalue.pop()
                else:
                    child.accept(self)
            else:
                child.accept(self)


    def visitStatementsNode(self, node):
        # self.outFile.write("code\n")
        openedScope = False
        if not isinstance(node.parent, (ASTFunctionDefinitionNode, ASTForNode)):
            self.symbolTable.openScope()
            openedScope = True
        self.visitChildren(node)
        if openedScope:
            self.symbolTable.closeScope()
        # for ttype in self.symbolTable.getVariables(node):
        #     self.outFile.write("ldc {0} {1}".format(self.p_type[ttype], self.initializers[ttype]))

    def visitStatementNode(self, node):
        self.visitChildren(node)


    def visitReturnNode(self, node):
        if not node.children:
            self.outFile.write("retp\n")
            return

        self.visitChildren(node) # TODO: make sure this takes the r value
        self.outFile.write("str {0} 0 0\n".format(self.p_types[node.children[0].getType().baseType]))
        self.outFile.write("retf\n") # note: this was not in the compendium

    def visitBreakNode(self, node):
        self.outFile.write("ujp {0}\n".format(self.forwardLabels[-1]))


    def visitContinueNode(self, node):
        self.outFile.write("ujp {0}\n".format(self.backLabels[-1]))


    def visitIfNode(self, node):
        elseLabel = self.getLabel() + "_else"
        afterLabel = self.getLabel() + "_after_if"

        self._lvalue.append(False)
        if not isinstance(node.children[0], ASTExpressionNode):
            # only in case of ternary conditional operator, given that every statement is wrapped by a statement node (which is the case at the time of writing)
            # if proper if node, _lvalue should be empty as it needs to be
            self._lvalue.pop()
        node.children[0].accept(self)                            # condition
        self.outFile.write("conv {0} b\n".format(self.pType(node.children[0].getType())))
        self.outFile.write("fjp {0}\n".format(elseLabel))        # if top == false, jump over the 'then' code
        node.children[1].accept(self)                            # 'then'

        if len(node.children) == 3:                              # optional else
            self.outFile.write("ujp {0}\n".format(afterLabel))   # jump over the 'else' code if coming from 'then'
            self.outFile.write("{0}:\n".format(elseLabel))
            node.children[2].accept(self)                        # else
            self.outFile.write("{0}:\n".format(afterLabel))
        else:
            self.outFile.write("{0}:\n".format(elseLabel))

        if isinstance(node.children[0], ASTExpressionNode):
            # if ternary conditional, pop from _lvalue after visiting 'then' and 'else' (which are expressions in that case)
            self._lvalue.pop()



    # def visitElseNode(self, node):
    #     self.visitChildren(node)

    def visitForNode(self, node):
        iterationLabel = self.getLabel() + "_for_iteration"
        conditionLabel = self.getLabel() + "_for_condition"
        afterLabel = self.getLabel() + "_for_after"
        self.backLabels.append(iterationLabel)
        self.forwardLabels.append(afterLabel)

        self.symbolTable.openScope()
        if node.initializer: node.initializer.accept(self)
        self.outFile.write("{0}:\n".format(conditionLabel))
        if node.condition:
            node.condition.accept(self)
            self.outFile.write("conv {0} b\n".format(self.pType(node.condition.getType())))
        else: self.outFile.write("ldc b t\n")
        self.outFile.write("fjp {0}\n".format(afterLabel))
        self.visitChildren(node)
        self.outFile.write("{0}:\n".format(iterationLabel))
        if node.iteration: node.iteration.accept(self)
        self.outFile.write("ujp {0}\n".format(conditionLabel))
        self.outFile.write("{0}:\n".format(afterLabel))
        self.symbolTable.closeScope()

        self.backLabels.pop()
        self.forwardLabels.pop()


    def visitWhileNode(self, node):
        conditionLabel = self.getLabel() + "_while_condition"
        afterLabel = self.getLabel() + "_while_after"
        self.backLabels.append(conditionLabel)
        self.forwardLabels.append(afterLabel)

        self.outFile.write("{0}:\n".format(conditionLabel))
        node.children[0].accept(self)                            # condition
        self.outFile.write("conv {0} b\n".format(self.pType(node.children[0].getType())))
        self.outFile.write("fjp {0}\n".format(afterLabel))       # if top == false, jump over the loop code
        node.children[1].accept(self)                            # loop code
        self.outFile.write("ujp {0}\n".format(conditionLabel))   # jump back to the condition
        self.outFile.write("{0}:\n".format(afterLabel))

        self.backLabels.pop()
        self.forwardLabels.pop()


    def visitDoWhileNode(self, node): #TODO: test this
        conditionLabel = self.getLabel() + "_do_while_condition"
        afterLabel = self.getLabel() + "_do_while_after"

        node.children[1].accept(self)                            # loop code

        self.outFile.write("conv {0} b\n".format(self.pType(node.children[1].getType())))
        self.outFile.write("{0}:\n".format(conditionLabel))
        node.children[0].accept(self)                            # condition
        self.outFile.write("fjp {0}\n".format(afterLabel))       # if top == false, jump over the loop code
        node.children[1].accept(self)                            # loop code
        self.outFile.write("ujp {0}\n".format(conditionLabel))   # jump back to the condition
        self.outFile.write("{0}:\n".format(afterLabel))


    def visitVariableDeclarationNode(self, node):
        # nothing here, handled by declaratorInitializer
        self.visitChildren(node)


    def allocArray(self, ttype, address):
        if not ttype.isArray():
            raise Exception("trying to alloc array of non-array type")
        arrayElementType = copy.deepcopy(ttype)
        arrayElementType.indirections = ttype.indirections[:-1]
        if ttype.arrayNrDimensions() == 1:
            for i in range(ttype.array()[-1]):
                # self.outFile.write("lda 0 {0}\n".format(address + i))
                self.outFile.write("ldc {0} {1}\n".format(self.pType(arrayElementType), self.initializers["address" if arrayElementType.nrIndirections() > 0 else arrayElementType.baseType]))
                self.outFile.write("str {0} 0 {1}\n".format(self.pType(arrayElementType), address + i))
        else:
            for i in range(ttype.array()[-1]):
                self.allocArray(arrayElementType, address + i * arrayElementType.size())


    def storeString(self, decl, initializer):
        string = None
        if initializer:
            string = initializer.children[0].decodedValue
        ttype = decl.getType()

        for i in range(ttype.array()[-1]):
            self.outFile.write("lda 0 {0}\n".format(decl.symbolInfo.address + i + 5))
            self.outFile.write("ldc c {0}\n".format(repr(string[i]) if i < len(string) else 27))
            self.outFile.write("sto c\n")


    def visitDeclaratorInitializerNode(self, node):
        ttype = node.getType()
        needStore = True

        if node.initializerList:
            if ttype == TYPES["string"] and node.initializerList.children and isinstance(node.initializerList.children[0], ASTStringLiteralNode):
                self.storeString(node, node.initializerList)
                needStore = False
            elif not ttype.isArray():
                node.initializerList.accept(self)
        elif not ttype.isArray():
            initializer = self.initializers["address" if node.getType().nrIndirections() > 0 else node.getType().baseType]
            self.outFile.write("ldc {0} {1}\n".format(self.pType(node.getType()), initializer))
        elif ttype.isArray():
            self.allocArray(ttype, node.symbolInfo.address + 5)
            needStore = False

        if needStore:
            self.outFile.write("str {0} 0 {1}\n".format(self.pType(node.getType()), node.symbolInfo.address + 5))


    def visitInitializerListNode(self, node):
        # children will cause data to be loaded onto the stack
        self.visitChildren(node)


    def enterExpression(self, node):
        # print(type(node), "is stmt node", isinstance(node, ASTStatementNode))
        if expressionResultNeedsToBeCleanedUp(node):
            self.outFile.write("ldc a 0\n")

    def exitExpression(self, node):
        if expressionResultNeedsToBeCleanedUp(node):
            self.outFile.write("sto {0}\n".format(self.pType(node.getType())))


    def visitCommaOperatorNode(self, node):
        child = node.children[0]
        if not node.getType().equals(TYPES["void"]):
            self.outFile.write("ldc a 0\n")
            child.accept(self)
            self.outFile.write("sto {0}\n".format(self.pType(child.getType())))
        else:
            child.accept(self)
        node.children[1].accept(self)


    def visitIntegerLiteralNode(self, node):
        self.outFile.write("ldc i {0}\n".format(str(node.value)))


    def visitFloatLiteralNode(self, node):
        self.outFile.write("ldc r {0}\n".format(format(node.value, "f")))


    def visitCharacterLiteralNode(self, node):
        self.outFile.write("ldc c {0}\n".format(str(node.value)))


    def visitStringLiteralNode(self, node):
        if isinstance(node.parent, ASTInitializerListNode):
            return
        symbolInfo = self.symbolTable.stringLiterals.get(node.decodedValue)
        self.outFile.write("lda 1 {0}\n".format(symbolInfo.address))

        if self.rvalue():
            self.outFile.write("ind a\n")



    def visitVariableNode(self, node):
        depthDifference = self.symbolTable.functionDefinitionDepthDifference(node.symbolInfo)
        if self.lvalue() or node.getType().isArray():
            # put address on stack
            self.outFile.write("lda {0} {1}\n".format(depthDifference, node.symbolInfo.address + 5))
        elif node.getType().nrIndirections() > 0:
            # TODO: can't the elif and else be joined together?
            self.outFile.write("lod a {0} {1}\n".format(depthDifference, node.symbolInfo.address + 5))
        else:
            # put value on stack
            self.outFile.write("lod {0} {1} {2}\n".format(self.pType(node.getType()), depthDifference, node.symbolInfo.address + 5))

        self.visitChildren(node)


    def printf(self, node):
        for el in node.parsedFormat:
            if isinstance(el, str):
                for c in bytes(el, "utf-8").decode("unicode-escape"):
                    self.outFile.write("ldc c {0}\n".format(repr(c) if c != '\'' else "'\''"))
                    self.outFile.write("out c\n")
            else:
                width, node = el
                if node.getType().equals(TYPES["int"]) and width > 0:
                    loop1Label = self.getLabel() + "_loop1"
                    afterLoop1Label = self.getLabel() + "_after_loop1"
                    loop2Label = self.getLabel() + "_loop2"
                    afterLoop2Label = self.getLabel() + "_after_loop2"
                    noPaddingLabel = self.getLabel() + "_no_padding"

                    self.outFile.write("ldc a 2\n")
                    self._lvalue.append(False)
                    node.accept(self)
                    self._lvalue.pop()
                    c = "sto i\n" # store number in 2
                    c += "ldc a 1\nldc a 2\nind i\nsto i\n" # initialize quotient
                    c += "ldc a 0\nldc i 1\nsto i\n" # initialize number length to -1 in 0
                    c += "ldc a 1\nind i\n"
                    c += "ldc i 0\n"
                    c += "les i\n" # if number < 0
                    c += "fjp {0}\n".format(loop1Label)
                    c += "ldc a 0\nldc a 0\nind i\ninc i 1\nsto i\n" # increment number length if number is negative
                    c += "ldc a 1\nldc a 1\nind i\nneg i\nsto i\n" # negate the quotient if it is negative
                    c += "{0}:\n".format(loop1Label) # loop
                    c += "ldc a 1\nind i\nldc i 9\ngrt i\nfjp {0}\n".format(afterLoop1Label) # if quotient > 9, iterate
                    c += "ldc a 0\nldc a 0\nind i\ninc i 1\nsto i\n" # increment number length in iteration
                    c += "ldc a 1\nldc a 1\nind i\n"
                    c += "ldc i 10\n"
                    c += "div i\n" # divide number by 10
                    c += "sto i\n"
                    c += "ujp {0}\n".format(loop1Label)
                    c += "{0}:\n".format(afterLoop1Label)
                    c += "ldc a 0\nldc i {0}\n".format(width)
                    c += "ldc a 0\nind i\n"
                    c += "sub i\nsto i\n" # calculate amount of padding, store in 0
                    # c += "ldc a 0\nind i\nldc i 0\ngeq i\nfjp {0}\n".format(noPaddingLabel)
                    c += "ldc a 1\nldc i 0\nsto i\n" # initialize loop iterator in 1
                    c += "{0}:\n".format(loop2Label)
                    c += "ldc a 1\nind i\nldc a 0\nind i\n" # iterator >= padding: end of loop
                    c += "les i\nfjp {0}\n".format(noPaddingLabel)
                    c += "ldc c ' '\nout c\n" # print padding
                    c += "ldc a 1\nldc a 1\nind i\ninc i 1\nsto i\n" # increment iterator
                    c += "ujp {0}\n".format(loop2Label)
                    c += "{0}:\n".format(noPaddingLabel)
                    c += "ldc a 2\nind i\nout i\n"
                    self.outFile.write(c)
                elif node.getType().equals(TYPES["char"]):
                    i = 0
                    while i < width - 1:
                        self.outFile.write("ldc c ' '\nout c\n")
                        i += 1
                    node.accept(self)
                    self.outFile.write("out c\n")
                elif node.getType().equals(TYPES["string"]):
                    b = c = ""

                    # code before evaluating char*
                    b += "ldc a 1\n"
                    
                    # code after evaluating char*
                    c += "sto a\n" # store the address of the string
                    c += "ldc a 0\nldc i 0\nsto i\n" # initialize counter
                    
                    if width > 0:
                        loopLabel = self.getLabel() + "_count_loop"
                        afterLoopLabel = self.getLabel() + "_after_count_loop"
                        paddingLoopLabel = self.getLabel() + "_padding_loop"
                        afterPaddingLoopLabel = self.getLabel() + "_after_padding_loop"

                        c += "ldc a 2\n" # load address to be able to pop the string's address later
                        c += "ldc a 1\nind a\n" # load the address of the string to 1
                        c += "dpl a\nind c\n"
                        c += "{0}:\n".format(loopLabel)
                        c += "ldc c 27\nneq c\nfjp {0}\n".format(afterLoopLabel)
                        c += "ldc a 0\nldc a 0\nind i\ninc i 1\nsto i\n" # increment counter
                        c += "inc a 1\ndpl a\nind c\n"
                        c += "ujp {0}\n".format(loopLabel)
                        c += "{0}:\n".format(afterLoopLabel)
                        c += "sto a\n" # pop address from stack
                        c += "ldc a 0\nldc i {0}\n".format(width)
                        c += "ldc a 0\nind i\n"
                        c += "sub i\nsto i\n" # determine number of padding spaces required
                        # c += "ldc a 0\nind i\nout i\nhlt\n"
                        c += "{0}:\n".format(paddingLoopLabel)
                        c += "ldc a 0\nind i\nldc i 0\ngrt i\nfjp {0}\n".format(afterPaddingLoopLabel) # padding <= 0
                        c += "ldc c ' '\nout c\n" # print padding
                        c += "ldc a 0\nldc a 0\nind i\ndec i 1\nsto i\n"
                        c += "ujp {0}\n".format(paddingLoopLabel)
                        c += "{0}:\n".format(afterPaddingLoopLabel)

                    loopLabel = self.getLabel() + "_out_loop"
                    afterLoopLabel = self.getLabel() + "_after_out_loop"

                    c += "ldc a 1\nind a\n"
                    c += "{0}:\n".format(loopLabel)
                    c += "\ndpl a\nind c\n"
                    c += "ldc c 27\nneq c\nfjp {0}\n".format(afterLoopLabel)
                    c += "dpl a\nind c\nout c\n" # print character
                    c += "inc a 1\n"
                    c += "ujp {0}\n".format(loopLabel)
                    c += "{0}:\n".format(afterLoopLabel)

                    self.outFile.write(b)
                    self._lvalue.append(False)
                    node.accept(self)
                    self._lvalue.pop()
                    self.outFile.write(c)


                elif isinstance(node, ASTNode) and not node.getType().equals(TYPES["void"]):
                    self._lvalue.append(False)
                    node.accept(self)
                    self._lvalue.pop()
                    self.outFile.write("out {0}\n".format(self.pType(node.getType())))

    def scanf(self, node):
        for el in node.parsedFormat:
            if isinstance(el, tuple):
                width, node = el
                if isinstance(node, ASTNode):
                    self._lvalue.append(False)
                    node.accept(self)
                    self._lvalue.pop()
                    self.outFile.write("in {0}\n".format(self.pType(node.getType().dereference())))
                    self.outFile.write("sto {0}\n".format(self.pType(node.getType().dereference())))

    def visitFunctionCallNode(self, node):
        if node.definitionNode.isStdioFunction:
            if node.identifier == "printf":
                self.printf(node)
            elif node.identifier == "scanf":
                self.scanf(node)
        else:
            functionSymbol = self.symbolTable.retrieveSymbol(node.identifier)
            # organizational block
            self.outFile.write("mst {0}\n".format(functionSymbol.depth))

            # evaluate arguments
            self.visitChildren(node)

            # call user procedure
            self.outFile.write("cup {0} function_{1}\n".format(len(node.children[0].children), node.definitionNode.identifier))


    def visitTypeCastNode(self, node):
        self.visitChildren(node)

        if self.rvalue() and self.pType(node.children[0].getType()) != self.pType(node.getType()):
            self.outFile.write("conv {0} {1}\n".format(self.pType(node.children[0].getType()), self.pType(node.getType())))


    def visitTernaryConditionalOperatorNode(self, node):
        self.visitIfNode(node)


    def visitSimpleAssignmentOperatorNode(self, node):
        # children of a = b: [ASTVariableNode, ExpressionNode]
        self._lvalue.append(True)
        node.children[0].accept(self)
        self.outFile.write("dpl a\n") # duplicate the address to load it after the assignment

        self._lvalue[-1] = False
        node.children[1].accept(self)
        self._lvalue.pop()

        self.outFile.write("sto {0}\n".format(self.pType(node.children[0].getType())))
        self.outFile.write("ind {0}\n".format(self.pType(node.children[0].getType())))


    def visitLogicOperatorNode(self, node):
        self._lvalue.append(False)
        node.children[0].accept(self)
        self.outFile.write("conv i b\n")
        node.children[1].accept(self)
        self.outFile.write("conv i b\n")
        self.outFile.write(str(node.logicOperatorType) + "\n")
        self.outFile.write("conv b i\n")
        self._lvalue.pop()


    def visitComparisonOperatorNode(self, node):
        self._lvalue.append(False)
        self.visitChildren(node)
        self.outFile.write("{0} {1}\n".format(self.bin_comp_op[str(node.comparisonType)], self.p_types[node.children[0].getType().baseType]))
        self.outFile.write("conv b i\n")
        self._lvalue.pop()


    def visitUnaryArithmeticOperatorNode(self, node):
        op = str(node.arithmeticType)
        ttype = node.children[0].getType()

        self._lvalue.append(op == "++" or op == "--")
        self.visitChildren(node)
        self._lvalue.pop()
        if op == "++" or op == "--":
            self.outFile.write("dpl a\ndpl a\n")
            maininstr = "inc"
            secinstr = "dec"
            if op == "--":
                maininstr, secinstr = secinstr, maininstr

            # a++;      aPtr++;

            self.outFile.write("ind {0}\n".format(self.pType(ttype)))
            if ttype.isPointer():
                self.outFile.write("conv a i\n")
            self.outFile.write("{0} {1} {2}\n".format(maininstr, *((self.pType(ttype), 1) if not ttype.isPointer() else ("i", str(ttype.dereference().size())))))
            if ttype.isPointer():
                self.outFile.write("conv i a\n")
            self.outFile.write("sto {0}\n".format(self.pType(ttype)))
            self.outFile.write("ind {0}\n".format(self.pType(ttype)))
            if node.operatorType == ASTUnaryOperatorNode.Type["postfix"]:
                if ttype.isPointer():
                    self.outFile.write("conv a i\n")
                self.outFile.write("{0} {1} {2}\n".format(secinstr, *((self.pType(ttype), 1) if not ttype.isPointer() else ("i", str(ttype.dereference().size())))))
                if ttype.isPointer():
                    self.outFile.write("conv i a\n")

        if op == "-":
            self.outFile.write("neg {0}\n".format(self.pType(ttype)))
        elif op == "+":
            pass


    def visitAddressOfoperatorNode(self, node):
        self._lvalue.append(True)
        if isinstance(node.children[0], ASTDereferenceOperatorNode):
            self.visitChildren(node.children[0])
        else:
            self.visitChildren(node)
        self._lvalue.pop()


    def visitDereferenceNode(self, node):
        self._lvalue.append(False)
        self.visitChildren(node)
        self._lvalue.pop()

        if self.rvalue():
            self.outFile.write("ind {0}\n".format(self.pType(node.getType())))


    def visitLogicalNotOperatorNode(self, node):
        self._lvalue.append(False)
        self.visitChildren(node)
        self._lvalue.pop()
        self.outFile.write("conv i b\n")
        self.outFile.write("not\n")
        self.outFile.write("conv b i\n")


    def visitArraySubscriptNode(self, node):
        arrayType = node.children[0].getType()
        arrayElementType = node.getType()

        self._lvalue.append(True)
        node.children[0].accept(self)
        if arrayType.isPointer():
            self.outFile.write("ind a\n")
        self._lvalue[-1] = False
        node.children[1].accept(self)
        self._lvalue.pop()

        if not arrayType.isPointer():
            self.outFile.write("chk 0 {0}\n".format(arrayType.size() - 1))
        
        self.outFile.write("ixa {0}\n".format(arrayElementType.size()))

        if self.rvalue():
            self.outFile.write("ind {0}\n".format(self.pType(node.getType())))


    def visitBinaryArithmeticNode(self, node):
        t1 = node.children[0].getType()
        t2 = node.children[1].getType()
        self._lvalue.append(False)
        if node.arithmeticType == ASTBinaryArithmeticOperatorNode.ArithmeticType["modulo"]:
            node.children[0].accept(self)
            self.outFile.write("dpl i\n")
            self.outFile.write("ldc a 0\n")
            node.children[1].accept(self)
            self.outFile.write("sto i\n" +\
                               "ldc a 0\n"+\
                               "ind i\n" +\
                               "div i\n" +\
                               "ldc a 0\n" +\
                               "ind i\n" +\
                               "mul i\n" +\
                               "sub i\n")
        elif t1.isPointer() or t2.isPointer():
            # pointer arithmetic
            pointerType, integerType = (t1, t2) if t1.isPointer() else (t2, t1)

            pointerCode = "conv a i\n"
            integerCode = "ldc i {0}\n".format(pointerType.dereference().size())
            integerCode += "mul i\n"

            node.children[0].accept(self)
            self.outFile.write(pointerCode if t1 is pointerType else integerCode)
            node.children[1].accept(self)
            self.outFile.write(pointerCode if t2 is pointerType else integerCode)

            self.outFile.write("{0} i\n".format(self.bin_arithm_op[str(node.arithmeticType)]))
            self.outFile.write("conv i a\n")

        else:
            self.visitChildren(node)
            self.outFile.write("{0} {1}\n".format(self.bin_arithm_op[str(node.arithmeticType)], self.p_types[node.children[0].getType().baseType]))
        self._lvalue.pop()

def expressionResultNeedsToBeCleanedUp(node):
    # print(type(node.parent))
    if not node.isBaseExpression():
        return False
    if node.getType().equals(TYPES["void"]):
        return False
    if type(node.parent) is ASTInitializerListNode:
        return False
    if isinstance(node.parent, ASTForNode):
        if node is node.parent.iteration:
            return True
        else:
            return False
    if isinstance(node.parent, (ASTIfNode, ASTWhileNode, ASTDoWhileNode, ASTReturnNode, ASTArgumentsNode, ASTDeclaratorInitializerNode)):
        return False
    if type(node.parent) is ASTStatementNode:
        return True
    raise Exception("don't know if expression result should be cleaned up for expression type " + str(type(node)) + ", parent type " + str(type(node.parent)))
