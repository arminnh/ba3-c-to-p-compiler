import unittest

# insert the parent directory into this path to get antlr files
import sys
sys.path.insert(0, '..')

from antlr4 import *
from SmallCLexer import SmallCLexer
from SmallCListener import SmallCListener
from SmallCParser import SmallCParser
from AbstractSyntaxTree import *
from MyListener import *
from ASTWalker import *
from ASTSymbolTableFiller import *

# import re to remove all whitespace from strings
import re


class ASTTest():
    def setUp(self):
        self.errorHandler = None

    def parseFile(self, filename):
        input_file = FileStream(filename)
        lexer = SmallCLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = SmallCParser(stream)
        programContext = parser.program()

        walker = ParseTreeWalker()
        self.errorHandler = CompilerErrorHandler(filename)
        abstractSyntaxTree = AbstractSyntaxTree(self.errorHandler);
        listener = MyListener(abstractSyntaxTree)
        walker.walk(listener, programContext)

        symbolTable = SymbolTable()
        tableFiller = ASTSymbolTableFiller(abstractSyntaxTree, symbolTable, self.errorHandler)
        tableFiller.fill()
        abstractSyntaxTree.typeCheck()

    def generateOneErrorAndCompare(self, filename):
        with self.assertRaises(Exception) as context:
            self.parseFile(filename + ".c")

        self.assertTrue(self.errorHandler.errorCount() == 1)
        #messageNoWhitespace = str(re.sub('[ \t\n\r]', '', str(context.exception)))
        #print (messageNoWhitespace.lower().find("errorhasoccurred") != -1)
        #self.assertTrue(messageNoWhitespace.lower().find("errorhasoccurred") != -1)

        # if there is error output generated, compare with txt file
        with open(filename + ".txt", 'r') as myfile:
            correctOutput = myfile.read()

        # remove all whitespace
        errorMessageNoWhitespace = str(re.sub('[ \t\n\r]', '', self.errorHandler.errorToString(0)))
        correctOutput = re.sub('[ \t\n\r]', '', correctOutput)

        self.assertTrue(errorMessageNoWhitespace.find(correctOutput) != -1)

    def generateNoError(self, filename):
        self.parseFile(filename)

        self.assertTrue(self.errorHandler.errorCount() == 0)


class ComparisonOperatorTypeTests(ASTTest, unittest.TestCase):

    # binary operators tests: <, >, <=, >=, ==, +, +, -, *, /, %
    # logic operators tests: &&, ||, !, must be same type and compatible with int
    # ternary operator test: needs int as first operator and alternatives should be of same type


    def testAllBinaryOperatorTypesLiteralsCorrect(self):
        self.generateNoError("testfiles/binary-operator-types-correct-literals.c")

    def testBinaryOperatorTypes1(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-1")

    def testBinaryOperatorTypes2(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-2")

    def testBinaryOperatorTypes3(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-3")

    def testBinaryOperatorTypes4(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-4")

    def testBinaryOperatorTypes5(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-5")

    def testBinaryOperatorTypes6(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-6")

    def testBinaryOperatorTypes7(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-7")

    def testBinaryOperatorTypes8(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-8")

    def testBinaryOperatorTypes9(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-9")

    def testBinaryOperatorTypes10(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-10")

    def testBinaryOperatorTypes11(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-11")

    def testBinaryOperatorTypes12(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-12")

    def testBinaryOperatorTypes13(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-13")

    def testBinaryOperatorTypes14(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-14")

    def testBinaryOperatorTypes15(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-15")

    def testBinaryOperatorTypes16(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-16")

    def testBinaryOperatorTypes17(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-17")

    def testBinaryOperatorTypes18(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-18")

    def testBinaryOperatorTypes19(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-19")

    def testBinaryOperatorTypes20(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-20")

    def testBinaryOperatorTypes21(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-21")

    def testBinaryOperatorTypes22(self):
        self.generateOneErrorAndCompare("testfiles/binary-operator-types-22")



def testAll():
    unittest.main()

if __name__=="__main__":
    testAll()
