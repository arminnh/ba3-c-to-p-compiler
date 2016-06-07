import unittest
import logging

# insert the parent directory into this path to get antlr files
import sys
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
set = False

class ASTTest():
    def setUp(self):
        self.errorHandler = None

    def parseFile(self, filename):
        input_file = FileStream(filename)
        lexer = CLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = CParser(stream)
        programContext = parser.program()

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

        if set and not expectedOutputFound:
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

        if set and not expectedCodeFound:
            f = open(filename + ".p_correct", "w")
            f.write(pCodeGeneratedOriginal)
            f.close()

        if not expectedCodeFound:
            print("\nEXPECTED:\n" + pCodeGeneratedOriginal + "\nGOT:\n" + pCodeCorrectOriginal + "\n\n\n\n")

        self.assertTrue(expectedCodeFound)

class UnaryOperatorsTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/2")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/3")

    def test4(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/4")

    def test5(self):
        self.generateNoError("testfiles/unary-operators/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/6")

    def test7(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/7")

    def test8(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/8")

    def test9(self):
        self.generateNoError("testfiles/unary-operators/9")

    def test10(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/10")

    def test11(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/11")

    def test12(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/12")

    def test13(self):
        self.generateNoError("testfiles/unary-operators/13")

    def test14(self):
        self.generateNoError("testfiles/unary-operators/14")

    def test15(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/15")

    def test16(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/16")


class BinaryOperatorsTests(ASTTest, unittest.TestCase):

    def testLiteralsCorrect(self):
        self.generateNoError("testfiles/binary-operators/correct-literals")

    def testStringsAndArrays(self):
        self.generateNoError("testfiles/binary-operators/strings-and-arrays")

    def test1(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/2")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/3")

    def test4(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/4")

    def test5(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/6")

    def test7(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/7")

    def test8(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/8")

    def test9(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/9")

    def test10(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/10")

    def test11(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/11")

    def test12(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/12")

    def test13(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/13")

    def test14(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/14")

    def test15(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/15")

    def test16(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/16")

    def test17(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/17")

    def test18(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/18")

    def test19(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/19")

    def test20(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/20")

    def test21(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/21")

    def test22(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/22")

    def test23(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/23")

    def test24(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/24")

    def test25(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/25")

    def test26(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/26")

    def test27(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/27")

    def test28(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/28")

    def test29(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/29")

    def test30(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/30")

    def test31(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/31")

    def test32(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/32")

    def test33(self):
        self.generateNoError("testfiles/binary-operators/33")

    def test34(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/34")

    def test35(self):
        self.generateNoError("testfiles/binary-operators/35")

    def test36(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/36")

    def test37(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/37")

    def test38(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/38")


class TernaryOperatorsTests(ASTTest, unittest.TestCase):
    # ternary operator test: needs int as first operator and alternatives should be of same type
    # (expression with type int) ? (expression with type T) : (expression with same type T);
    def test1(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/2")

    def test3(self):
        self.generateNoError("testfiles/ternary-operator/3")

    def test4(self):
        self.generateNoError("testfiles/ternary-operator/4")

    def test5(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/6")


class FunctionCallsTests(ASTTest, unittest.TestCase):

    def testCorrect(self):
        self.generateNoError("testfiles/function-calls/correct")

    def test1(self):
        self.generateErrorsAndCompare("testfiles/function-calls/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/function-calls/2")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/function-calls/3")

    def test4(self):
        self.generateErrorsAndCompare("testfiles/function-calls/4")

    def test5(self):
        self.generateErrorsAndCompare("testfiles/function-calls/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/function-calls/6")

    def test7(self):
        self.generateErrorsAndCompare("testfiles/function-calls/7")

    def test8(self):
        self.generateErrorsAndCompare("testfiles/function-calls/8")

    def test9(self):
        self.generateErrorsAndCompare("testfiles/function-calls/9")

    def test10(self):
        self.generateNoError("testfiles/function-calls/10")

    def test11(self):
        self.generateErrorsAndCompare("testfiles/function-calls/11")

    def test12(self):
        self.generateNoError("testfiles/function-calls/12")

    def test13(self):
        self.generateErrorsAndCompare("testfiles/function-calls/13")

    def test14(self):
        self.generateErrorsAndCompare("testfiles/function-calls/14")

    def test15(self):
        self.generateErrorsAndCompare("testfiles/function-calls/15")

    def test16(self):
        self.generateErrorsAndCompare("testfiles/function-calls/16")

    def test17(self):
        self.generateErrorsAndCompare("testfiles/function-calls/17")

    def test18(self):
        self.generateErrorsAndCompare("testfiles/function-calls/18")

    # test 19 takes very long (15 seconds)
    # def test19(self):
    #     self.generateErrorsAndCompare("testfiles/function-calls/19")

    def test20(self):
        self.generateNoError("testfiles/function-calls/20")

    def test21(self):
        self.generateErrorsAndCompare("testfiles/function-calls/21")

    def test22(self):
        self.generateErrorsAndCompare("testfiles/function-calls/22")

    def test23(self):
        self.generateErrorsAndCompare("testfiles/function-calls/23")

    def test24(self):
        self.generateErrorsAndCompare("testfiles/function-calls/24")

    def test25(self):
        self.generateErrorsAndCompare("testfiles/function-calls/25")


class VariableDeclarationsTests(ASTTest, unittest.TestCase):

    def testStrangeBrackets(self):
        self.generateNoError("testfiles/variable-declarations/strange-brackets")

    def testCharArraysPointers(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/char-arrays-pointers")

    def testMultiArraysPointers(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/multi-arrays-pointers")

    def test1(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/2")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/3")

    def test4(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/4")

    def test5(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/6")

    def test7(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/7")

    def test8(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/8")

    def test9(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/9")

    def test10(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/10")

    def test11(self):
        self.generateNoError("testfiles/variable-declarations/11")

    def test12(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/12")

    def test13(self):
        self.generateNoError("testfiles/variable-declarations/13")

    def test14(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/14")

    def test15(self):
        self.generateNoError("testfiles/variable-declarations/15")

    def test16(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/16")

    def test17(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/17")

    def test18(self):
        self.generateNoError("testfiles/variable-declarations/18")

    def test19(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/19")

    def test20(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/20")

    def test21(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/21")

    def test22(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/22")

    def test23(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/23")

    def test24(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/24")

    def test25(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/25")

    def test26(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/26")

    def test27(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/27")

    def test28(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/28")

    def test29(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/29")

    def test30(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/30")

    def test31(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/31")


class FunctionDeclarationsTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/2")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/3")

    def test4(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/4")

    def test5(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/6")

    def test7(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/7")

    def test8(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/8")

    def test9(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/9")

    def test10(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/10")

    def test11(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/11")

    def test12(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/12")

    def test13(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/13")

    def test14(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/14")

    def test15(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/15")

    def test16(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/16")

    def test17(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/17")

    def test18(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/18")

    def test19(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/19")

    def test20(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/20")

    def test21(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/21")

    def test22(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/22")

    def test23(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/23")


class ConstTests(ASTTest, unittest.TestCase):

    def test1(self):
        self.generateNoError("testfiles/const/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/const/2")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/const/3")

    def test4(self):
        self.generateErrorsAndCompare("testfiles/const/4")

    def test5(self):
        self.generateErrorsAndCompare("testfiles/const/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/const/6")

    def test7(self):
        self.generateErrorsAndCompare("testfiles/const/7")

    def test8(self):
        self.generateErrorsAndCompare("testfiles/const/8")

    def test9(self):
        self.generateErrorsAndCompare("testfiles/const/9")

    def test10(self):
        self.generateErrorsAndCompare("testfiles/const/10")


class MiscellaneousTests(ASTTest, unittest.TestCase):

    # expressions.c has many combinations of binary operators
    def testExpressions(self):
        self.generateNoError("testfiles/expressions")

    # tests different usages of if, else, while, do while, if without else
    def testFlowControl(self):
        self.generateNoError("testfiles/flow_control")

    # many scopes and many variables and some more complex initializers
    def testVariables(self):
        self.generateNoError("testfiles/variables")

    # functions, forward declarations, weird parameters to functions and printf
    def testFunctions(self):
        self.generateNoError("testfiles/functions")

    # a file with some includes, functions, expressions and flow control
    def testHelloWorld(self):
        self.generateNoError("testfiles/hello_world")

    # builds and prints a Hankel matrix
    def testPrintMatrix(self):
        self.generateNoError("testfiles/print_matrix")


class EvalutationTests(ASTTest, unittest.TestCase):

    def testTypes(self):
        self.generateNoError("testfiles/assistant-tests/1types2")

    def testIO(self):
        self.generateNoError("testfiles/assistant-tests/2io1")

    def testExpressions(self):
        self.generateNoError("testfiles/assistant-tests/3expressions3")

    def testFunction(self):
        self.generateNoError("testfiles/assistant-tests/7function2")

    def testArrays(self):
        self.generateNoError("testfiles/assistant-tests/8arrays2")


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
