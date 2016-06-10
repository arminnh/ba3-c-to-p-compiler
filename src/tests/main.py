import logging

# insert the parent directory into this path to get antlr files
import sys
import unittest
import os
sys.path.insert(0, "..")

from antlr4_generated.CLexer import CLexer
from antlr4_generated.CParser import CParser

from AbstractSyntaxTree import *
from Listener import *
from ErrorHandler import *
from SymbolTable import *
from VisitorDefinitionProcessor import *
from VisitorDeclarationProcessor import *
from VisitorTypeChecker import *
from VisitorCodeGenerator import *
from VisitorDecorator import *

import copy
# import re to remove all whitespace from strings
import re

# set this to True to generate test .txt files for failing
# generate-error-and-compare tests with output from c2p.py
setTxtFiles = False
setPCode = False

class ASTTest():
    def setUp(self):
        self.errorHandler = None

    def parseFile(self, filename):
        input_file = FileStream(filename)
        lexer = CLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = CParser(stream)
        programContext = parser.program()

        if parser._syntaxErrors > 0:
            raise Exception("error parsing file " + filename)

        walker = ParseTreeWalker()
        abstractSyntaxTree = AbstractSyntaxTree();
        self.errorHandler = ErrorHandler(filename)
        listener = Listener(abstractSyntaxTree)
        walker.walk(listener, programContext)

        decorator = VisitorDecorator()
        decorator.visitProgramNode(abstractSyntaxTree.root)

        symbolTable = SymbolTable()
        functionFiller = VisitorDefinitionProcessor(symbolTable, self.errorHandler)
        functionFiller.visitProgramNode(abstractSyntaxTree.root)

        tableFiller = VisitorDeclarationProcessor(symbolTable, self.errorHandler)
        tableFiller.visitProgramNode(abstractSyntaxTree.root)

        typeCheck = VisitorTypeChecker(self.errorHandler)
        typeCheck.visitProgramNode(abstractSyntaxTree.root)

        if self.errorHandler.errorCount() == 0:
            pFilename = os.path.splitext(filename)[0] + ".p"
            codeGenerator = VisitorCodeGenerator(symbolTable, pFilename)
            codeGenerator.visitProgramNode(abstractSyntaxTree.root)

    def generateErrorsAndCompare(self, filename):
        self.parseFile(filename + ".c")
        self.assertTrue(self.errorHandler.errorCount() or self.errorHandler.warningCount())

        # if there is error output generated, compare with txt file
        try:
            with open(filename + ".txt", "r") as myfile:
                correctOutputOriginal = myfile.read()
        except:
            with open(filename + ".txt", "w") as myfile:
                correctOutputOriginal = ""

        errorMessage = self.errorHandler.errorsToString()
        errorMessageWithWhitespace = copy.copy(errorMessage)

        # remove all whitespace
        errorMessage  = re.sub("[ \t\n\r]", "", errorMessage)
        correctOutput = re.sub("[ \t\n\r]", "", correctOutputOriginal)

        # expectedOutputFound = errorMessage.find(correctOutput) != -1
        expectedOutputFound = errorMessage == correctOutput

        if setTxtFiles and not expectedOutputFound:
            f = open(filename + ".txt", "w")
            f.write(errorMessageWithWhitespace)
            f.close()

        if not expectedOutputFound:
            print("\nEXPECTED:\n" + correctOutputOriginal + "\nGOT:\n" + errorMessageWithWhitespace + "\n\n\n\n")

        self.assertTrue(expectedOutputFound)

    def generateNoError(self, filename):
        self.parseFile(filename + ".c")
        self.assertTrue(self.errorHandler.errorCount() == 0)

        # open the newly generated p code file
        try:
            with open(filename + ".p", "r") as myfile:
                pCodeGeneratedOriginal = myfile.read()
        except:
            with open(filename + ".p", "w") as myfile:
                pCodeGeneratedOriginal = ""

        # open the file with the correct p code
        try:
            with open(filename + ".p_correct", "r") as myfile:
                pCodeCorrectOriginal = myfile.read()
        except:
            with open(filename + ".p_correct", "w") as myfile:
                pCodeCorrectOriginal = ""

        # remove all whitespace
        pCodeGenerated  = re.sub("[ \t\n\r]", "", pCodeGeneratedOriginal)
        pCodeCorrect    = re.sub("[ \t\n\r]", "", pCodeCorrectOriginal)

        # expectedOutputFound = errorMessage.find(correctOutput) != -1
        expectedCodeFound = pCodeGenerated == pCodeCorrect

        if setPCode and not expectedCodeFound:
            f = open(filename + ".p_correct", "w")
            f.write(pCodeGeneratedOriginal)
            f.close()

        if not expectedCodeFound:
            print("\nEXPECTED:\n" + pCodeGeneratedOriginal + "\nGOT:\n" + pCodeCorrectOriginal + "\n\n\n\n")

        os.system("gcc -std=c99 " + filename + ".c -w -o " + filename + ".testbin")

        self.assertTrue(expectedCodeFound)

class UnaryOperatorsTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateErrorsAndCompare("unary-operators/1")

    def test2(self):
        self.generateErrorsAndCompare("unary-operators/2")

    def test3(self):
        self.generateErrorsAndCompare("unary-operators/3")

    def test4(self):
        self.generateErrorsAndCompare("unary-operators/4")

    def test5(self):
        self.generateNoError("unary-operators/5")

    def test6(self):
        self.generateErrorsAndCompare("unary-operators/6")

    def test7(self):
        self.generateErrorsAndCompare("unary-operators/7")

    def test8(self):
        self.generateErrorsAndCompare("unary-operators/8")

    def test9(self):
        self.generateNoError("unary-operators/9")

    def test10(self):
        self.generateErrorsAndCompare("unary-operators/10")

    def test11(self):
        self.generateErrorsAndCompare("unary-operators/11")

    def test12(self):
        self.generateErrorsAndCompare("unary-operators/12")

    def test13(self):
        self.generateNoError("unary-operators/13")

    def test14(self):
        self.generateNoError("unary-operators/14")

    def test15(self):
        self.generateErrorsAndCompare("unary-operators/15")

    def test16(self):
        self.generateErrorsAndCompare("unary-operators/16")

    def test17(self):
        self.generateErrorsAndCompare("unary-operators/17")

    def test18(self):
        self.generateNoError("unary-operators/18")


class BinaryOperatorsTests(ASTTest, unittest.TestCase):

    def testLiteralsCorrect(self):
        self.generateNoError("binary-operators/correct-literals")

    def testStringsAndArrays(self):
        self.generateNoError("binary-operators/strings-and-arrays")

    def testPointerArithmetic(self):
        self.generateNoError("binary-operators/pointer-arithmetic")

    def test1(self):
        self.generateErrorsAndCompare("binary-operators/1")

    def test2(self):
        self.generateErrorsAndCompare("binary-operators/2")

    def test3(self):
        self.generateErrorsAndCompare("binary-operators/3")

    def test4(self):
        self.generateErrorsAndCompare("binary-operators/4")

    def test5(self):
        self.generateErrorsAndCompare("binary-operators/5")

    def test6(self):
        self.generateErrorsAndCompare("binary-operators/6")

    def test7(self):
        self.generateErrorsAndCompare("binary-operators/7")

    def test8(self):
        self.generateErrorsAndCompare("binary-operators/8")

    def test9(self):
        self.generateErrorsAndCompare("binary-operators/9")

    def test10(self):
        self.generateErrorsAndCompare("binary-operators/10")

    def test11(self):
        self.generateErrorsAndCompare("binary-operators/11")

    def test12(self):
        self.generateErrorsAndCompare("binary-operators/12")

    def test13(self):
        self.generateErrorsAndCompare("binary-operators/13")

    def test14(self):
        self.generateErrorsAndCompare("binary-operators/14")

    def test15(self):
        self.generateErrorsAndCompare("binary-operators/15")

    def test16(self):
        self.generateErrorsAndCompare("binary-operators/16")

    def test17(self):
        self.generateErrorsAndCompare("binary-operators/17")

    def test18(self):
        self.generateErrorsAndCompare("binary-operators/18")

    def test19(self):
        self.generateErrorsAndCompare("binary-operators/19")

    def test20(self):
        self.generateErrorsAndCompare("binary-operators/20")

    def test21(self):
        self.generateErrorsAndCompare("binary-operators/21")

    def test22(self):
        self.generateErrorsAndCompare("binary-operators/22")

    def test23(self):
        self.generateErrorsAndCompare("binary-operators/23")

    def test24(self):
        self.generateErrorsAndCompare("binary-operators/24")

    def test25(self):
        self.generateErrorsAndCompare("binary-operators/25")

    def test26(self):
        self.generateErrorsAndCompare("binary-operators/26")

    def test27(self):
        self.generateErrorsAndCompare("binary-operators/27")

    def test28(self):
        self.generateErrorsAndCompare("binary-operators/28")

    def test29(self):
        self.generateErrorsAndCompare("binary-operators/29")

    def test30(self):
        self.generateErrorsAndCompare("binary-operators/30")

    def test31(self):
        self.generateErrorsAndCompare("binary-operators/31")

    def test32(self):
        self.generateErrorsAndCompare("binary-operators/32")

    def test33(self):
        self.generateNoError("binary-operators/33")

    def test34(self):
        self.generateErrorsAndCompare("binary-operators/34")

    def test35(self):
        self.generateNoError("binary-operators/35")

    def test36(self):
        self.generateErrorsAndCompare("binary-operators/36")

    def test37(self):
        self.generateErrorsAndCompare("binary-operators/37")

    def test38(self):
        self.generateErrorsAndCompare("binary-operators/38")

    def test39(self):
        self.generateErrorsAndCompare("binary-operators/39")

    def test39(self):
        self.generateErrorsAndCompare("binary-operators/40")


class TernaryOperatorsTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateErrorsAndCompare("ternary-operator/1")

    def test2(self):
        self.generateErrorsAndCompare("ternary-operator/2")

    def test3(self):
        self.generateNoError("ternary-operator/3")

    def test4(self):
        self.generateNoError("ternary-operator/4")

    def test5(self):
        self.generateErrorsAndCompare("ternary-operator/5")

    def test6(self):
        self.generateErrorsAndCompare("ternary-operator/6")


class FunctionCallsTests(ASTTest, unittest.TestCase):

    def testCorrect(self):
        self.generateNoError("function-calls/correct")

    def testBasicScanf(self):
        self.generateNoError("function-calls/basic-scanf")

    def test1(self):
        self.generateErrorsAndCompare("function-calls/1")

    def test2(self):
        self.generateErrorsAndCompare("function-calls/2")

    def test3(self):
        self.generateErrorsAndCompare("function-calls/3")

    def test4(self):
        self.generateErrorsAndCompare("function-calls/4")

    def test5(self):
        self.generateErrorsAndCompare("function-calls/5")

    def test6(self):
        self.generateErrorsAndCompare("function-calls/6")

    def test7(self):
        self.generateErrorsAndCompare("function-calls/7")

    def test8(self):
        self.generateErrorsAndCompare("function-calls/8")

    def test9(self):
        self.generateErrorsAndCompare("function-calls/9")

    def test10(self):
        self.generateNoError("function-calls/10")

    def test11(self):
        self.generateErrorsAndCompare("function-calls/11")

    def test12(self):
        self.generateNoError("function-calls/12")

    def test13(self):
        self.generateErrorsAndCompare("function-calls/13")

    def test14(self):
        self.generateErrorsAndCompare("function-calls/14")

    def test15(self):
        self.generateErrorsAndCompare("function-calls/15")

    def test16(self):
        self.generateErrorsAndCompare("function-calls/16")

    def test17(self):
        self.generateErrorsAndCompare("function-calls/17")

    def test18(self):
        self.generateErrorsAndCompare("function-calls/18")

    # this test takes very long to finish (15 seconds)
    # def test19(self):
    #     self.generateErrorsAndCompare("function-calls/19")

    def test20(self):
        self.generateNoError("function-calls/20")

    def test21(self):
        self.generateErrorsAndCompare("function-calls/21")

    def test22(self):
        self.generateErrorsAndCompare("function-calls/22")

    def test23(self):
        self.generateErrorsAndCompare("function-calls/23")

    def test24(self):
        self.generateErrorsAndCompare("function-calls/24")

    def test25(self):
        self.generateErrorsAndCompare("function-calls/25")

    def test26(self):
        self.generateNoError("function-calls/26")

    def test27(self):
        self.generateNoError("function-calls/27")

    def test28(self):
        self.generateErrorsAndCompare("function-calls/28")


class VariableDeclarationsTests(ASTTest, unittest.TestCase):

    def testStrangeBrackets(self):
        self.generateNoError("variable-declarations/strange-brackets")

    def testCharArraysPointers(self):
        self.generateErrorsAndCompare("variable-declarations/char-arrays-pointers")

    def testMultiArraysPointers(self):
        self.generateErrorsAndCompare("variable-declarations/multi-arrays-pointers")

    def testFunctionVariableSameName(self):
        self.generateErrorsAndCompare("variable-declarations/function-variable-same-name")

    def testTypeCasts(self):
        self.generateNoError("variable-declarations/typecasts")

    def test1(self):
        self.generateErrorsAndCompare("variable-declarations/1")

    def test2(self):
        self.generateErrorsAndCompare("variable-declarations/2")

    def test3(self):
        self.generateErrorsAndCompare("variable-declarations/3")

    def test4(self):
        self.generateErrorsAndCompare("variable-declarations/4")

    def test5(self):
        self.generateErrorsAndCompare("variable-declarations/5")

    def test6(self):
        self.generateErrorsAndCompare("variable-declarations/6")

    def test7(self):
        self.generateErrorsAndCompare("variable-declarations/7")

    def test8(self):
        self.generateErrorsAndCompare("variable-declarations/8")

    def test9(self):
        self.generateErrorsAndCompare("variable-declarations/9")

    def test10(self):
        self.generateErrorsAndCompare("variable-declarations/10")

    def test11(self):
        self.generateNoError("variable-declarations/11")

    def test12(self):
        self.generateErrorsAndCompare("variable-declarations/12")

    def test13(self):
        self.generateNoError("variable-declarations/13")

    def test14(self):
        self.generateErrorsAndCompare("variable-declarations/14")

    def test15(self):
        self.generateNoError("variable-declarations/15")

    def test16(self):
        self.generateErrorsAndCompare("variable-declarations/16")

    def test17(self):
        self.generateErrorsAndCompare("variable-declarations/17")

    def test18(self):
        self.generateNoError("variable-declarations/18")

    def test19(self):
        self.generateErrorsAndCompare("variable-declarations/19")

    def test20(self):
        self.generateErrorsAndCompare("variable-declarations/20")

    def test21(self):
        self.generateErrorsAndCompare("variable-declarations/21")

    def test22(self):
        self.generateErrorsAndCompare("variable-declarations/22")

    def test23(self):
        self.generateErrorsAndCompare("variable-declarations/23")

    def test24(self):
        self.generateErrorsAndCompare("variable-declarations/24")

    def test25(self):
        self.generateErrorsAndCompare("variable-declarations/25")

    def test26(self):
        self.generateErrorsAndCompare("variable-declarations/26")

    def test27(self):
        self.generateErrorsAndCompare("variable-declarations/27")

    def test28(self):
        self.generateErrorsAndCompare("variable-declarations/28")

    def test29(self):
        self.generateErrorsAndCompare("variable-declarations/29")

    def test30(self):
        self.generateErrorsAndCompare("variable-declarations/30")

    def test31(self):
        self.generateErrorsAndCompare("variable-declarations/31")

    def test32(self):
        self.generateErrorsAndCompare("variable-declarations/32")

    def test33(self):
        self.generateErrorsAndCompare("variable-declarations/33")


class FunctionDeclarationsTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateErrorsAndCompare("function-declarations/1")

    def test2(self):
        self.generateErrorsAndCompare("function-declarations/2")

    def test3(self):
        self.generateErrorsAndCompare("function-declarations/3")

    def test4(self):
        self.generateErrorsAndCompare("function-declarations/4")

    def test5(self):
        self.generateErrorsAndCompare("function-declarations/5")

    def test6(self):
        self.generateErrorsAndCompare("function-declarations/6")

    def test7(self):
        self.generateErrorsAndCompare("function-declarations/7")

    def test8(self):
        self.generateErrorsAndCompare("function-declarations/8")

    def test9(self):
        self.generateErrorsAndCompare("function-declarations/9")

    def test10(self):
        self.generateErrorsAndCompare("function-declarations/10")

    def test11(self):
        self.generateErrorsAndCompare("function-declarations/11")

    def test12(self):
        self.generateErrorsAndCompare("function-declarations/12")

    def test13(self):
        self.generateErrorsAndCompare("function-declarations/13")

    def test14(self):
        self.generateErrorsAndCompare("function-declarations/14")

    def test15(self):
        self.generateErrorsAndCompare("function-declarations/15")

    def test16(self):
        self.generateErrorsAndCompare("function-declarations/16")

    def test17(self):
        self.generateErrorsAndCompare("function-declarations/17")

    def test18(self):
        self.generateErrorsAndCompare("function-declarations/18")

    def test19(self):
        self.generateErrorsAndCompare("function-declarations/19")

    def test20(self):
        self.generateErrorsAndCompare("function-declarations/20")

    def test21(self):
        self.generateErrorsAndCompare("function-declarations/21")

    def test22(self):
        self.generateErrorsAndCompare("function-declarations/22")

    def test23(self):
        self.generateErrorsAndCompare("function-declarations/23")

    def test24(self):
        self.generateErrorsAndCompare("function-declarations/24")


class ConstTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateNoError("const/1")

    def test2(self):
        self.generateErrorsAndCompare("const/2")

    def test3(self):
        self.generateErrorsAndCompare("const/3")

    def test4(self):
        self.generateErrorsAndCompare("const/4")

    def test5(self):
        self.generateErrorsAndCompare("const/5")

    def test6(self):
        self.generateErrorsAndCompare("const/6")

    def test7(self):
        self.generateErrorsAndCompare("const/7")

    def test8(self):
        self.generateErrorsAndCompare("const/8")

    def test9(self):
        self.generateErrorsAndCompare("const/9")

    def test10(self):
        self.generateErrorsAndCompare("const/10")


class MiscellaneousTests(ASTTest, unittest.TestCase):

    # will store an int on a manually chosen address
    def testStoreInAddress(self):
        self.generateNoError("misc/store-in-address")

    # some uses of multi dimensional arrays
    def testMultidimensionalArrays(self):
        self.generateErrorsAndCompare("misc/multidimensional-arrays")

    # expressions.c has many combinations of binary operators
    def testExpressions(self):
        self.generateNoError("misc/expressions")

    # tests different usages of if, else, while, do while, if without else
    def testFlowControl(self):
        self.generateNoError("misc/flow-control")

    # many scopes and many variables and some more complex initializers
    def testVariables(self):
        self.generateNoError("misc/variables")

    # functions, forward declarations, weird parameters to functions and printf
    def testFunctions(self):
        self.generateNoError("misc/functions")

    # a file with some includes, functions, expressions and flow control
    def testHelloWorld(self):
        self.generateNoError("misc/hello-world")

    # basic for and while loops
    def testForAndWhile(self):
        self.generateNoError("misc/for-and-while")

    # usage of some global variables
    def testGlobalVar(self):
        self.generateNoError("misc/global-var")


class ProgramsTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateNoError("programs/areaCircle")

    def test2(self):
        self.generateNoError("programs/areaCirclePointer")

    def test3(self):
        self.generateNoError("programs/areaRectangle")

    def test4(self):
        self.generateNoError("programs/areaTriangle")

    def test5(self):
        self.generateNoError("programs/arrayCopy")

    def test6(self):
        self.generateNoError("programs/arraySum")

    def test7(self):
        self.generateNoError("programs/centigradeToFarenheit")

    def test8(self):
        self.generateNoError("programs/factorialNoFunction")

    def test9(self):
        self.generateNoError("programs/factorialRecursive")

    def test9_1(self):
        self.generateNoError("programs/fibonacci")

    def test10(self):
        self.generateNoError("programs/hanoiTowers")

    def test11(self):
        self.generateNoError("programs/knapsackProblem")

    def test12_0(self):
        self.generateNoError("programs/matrixInitializerPrint")

    def test12(self):
        self.generateNoError("programs/matrixInverse")

    def test13(self):
        self.generateNoError("programs/matrixIsMagicSquare")

    def test14(self):
        self.generateNoError("programs/matrixMultiplication")

    def test15(self):
        self.generateNoError("programs/matrixMultiplicationRecursive")

    def test15_1(self):
        self.generateNoError("programs/matrixPrint")

    def test16(self):
        self.generateNoError("programs/pointerAddition")

    def test16_1(self):
        self.generateNoError("programs/pointerAdditionSegmentationFault")

    def test17(self):
        self.generateNoError("programs/pointerReverseArray")

    def test18(self):
        self.generateNoError("programs/pointerStringLength")

    def test19(self):
        self.generateNoError("programs/pointerSumArray")

    def test20(self):
        self.generateNoError("programs/primsAlgorithm")

    def test21(self):
        self.generateNoError("programs/printAllASCIIValues")

    def test22(self):
        self.generateNoError("programs/snek")

    def test23(self):
        self.generateNoError("programs/tableOfSquares")


class EvalutationTests(ASTTest, unittest.TestCase):

    def testTypes(self):
        self.generateNoError("assistant-tests/1types2")

    def testIO(self):
        self.generateNoError("assistant-tests/2io1")

    def testExpressions(self):
        self.generateNoError("assistant-tests/3expressions3")

    def testFunction(self):
        self.generateNoError("assistant-tests/7function2")

    def testArrays(self):
        self.generateNoError("assistant-tests/8arrays2")


class SymbolTableTests(unittest.TestCase):
    def testInsertionAndRetrieval(self):
        table = SymbolTable()
        inttype = TypeInfo(rvalue=False, baseType="int")
        floattype = TypeInfo(rvalue=False, baseType="float")
        chartype = TypeInfo(rvalue=False, baseType="char")
        a = ASTVariableNode("a")
        a.typeInfo = inttype

        b = ASTVariableNode("b")
        b.typeInfo = floattype

        c = ASTVariableNode("c")
        c.typeInfo = chartype

        d = ASTVariableNode("d")
        d.typeInfo = floattype

        b_bis = ASTVariableNode("b")
        b_bis.typeInfo = inttype

        # d_bis = ASTVariableNode("d")
        # d_bis.type = floattype

        table.insertVariableSymbol(a)
        table.insertVariableSymbol(b)
        table.openScope()
        table.insertVariableSymbol(c)
        self.assertTrue(table.retrieveSymbol("a", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("c", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("d", requireSeen=False) is None)
        table.closeScope()
        table.openScope()
        table.insertVariableSymbol(d)
        table.insertVariableSymbol(b_bis)
        self.assertTrue(table.retrieveSymbol("a", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("c", requireSeen=False) is None)
        self.assertTrue(table.retrieveSymbol("d", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False).typeInfo.baseType == "int")

        table.closeScope()

        self.assertTrue(table.retrieveSymbol("b", requireSeen=False).typeInfo.baseType == "float")
        self.assertTrue(table.retrieveSymbol("a", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("c", requireSeen=False) is None)
        self.assertTrue(table.retrieveSymbol("d", requireSeen=False) is None)

def testAll():
    unittest.main()

if __name__=="__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("ASTTest").setLevel(logging.DEBUG)
    testAll()
