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

class UnaryOperatorsTypeTests(ASTTest, unittest.TestCase):
    # unary operators: ++, --, *, &, !, [], can be prefix or postfix
    # unary logic operator: ! only works with type int
    def testUnaryOperatorTypes1(self):
        self.generateOneErrorAndCompare("testfiles/unary-operators/types-1")

    def testUnaryOperatorTypes2(self):
        self.generateOneErrorAndCompare("testfiles/unary-operators/types-2")

    def testUnaryOperatorTypes3(self):
        self.generateOneErrorAndCompare("testfiles/unary-operators/types-3")

    def testUnaryOperatorTypes4(self):
        self.generateOneErrorAndCompare("testfiles/unary-operators/types-4")
    
    def testUnaryOperatorTypes5(self):
        self.generateNoError("testfiles/unary-operators/types-5.c")

    def testUnaryOperatorTypes6(self):
        self.generateOneErrorAndCompare("testfiles/unary-operators/types-6")

    def testUnaryOperatorTypes7(self):
        self.generateOneErrorAndCompare("testfiles/unary-operators/types-7")

class BinaryOperatorsTypeTests(ASTTest, unittest.TestCase):
    # binary operators tests: <, >, <=, >=, ==, +, +, -, *, /, %
    # binary logic operators tests: &&, || must be same type and compatible with int

    def testAllBinaryOperatorTypesLiteralsCorrect(self):
        self.generateNoError("testfiles/binary-operators/types-correct-literals.c")

    def testBinaryOperatorTypes1(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-1")

    def testBinaryOperatorTypes2(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-2")

    def testBinaryOperatorTypes3(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-3")

    def testBinaryOperatorTypes4(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-4")

    def testBinaryOperatorTypes5(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-5")

    def testBinaryOperatorTypes6(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-6")

    def testBinaryOperatorTypes7(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-7")

    def testBinaryOperatorTypes8(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-8")

    def testBinaryOperatorTypes9(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-9")

    def testBinaryOperatorTypes10(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-10")

    def testBinaryOperatorTypes11(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-11")

    def testBinaryOperatorTypes12(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-12")

    def testBinaryOperatorTypes13(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-13")

    def testBinaryOperatorTypes14(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-14")

    def testBinaryOperatorTypes15(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-15")

    def testBinaryOperatorTypes16(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-16")

    def testBinaryOperatorTypes17(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-17")

    def testBinaryOperatorTypes18(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-18")

    def testBinaryOperatorTypes19(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-19")

    def testBinaryOperatorTypes20(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-20")

    def testBinaryOperatorTypes21(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-21")

    def testBinaryOperatorTypes22(self):
        self.generateOneErrorAndCompare("testfiles/binary-operators/types-22")

class TernaryOperatorTypeTests(ASTTest, unittest.TestCase):
    # ternary operator test: needs int as first operator and alternatives should be of same type
    # (expression with type int) ? (expression with type T) : (expression with same type T);
    def ternaryOperatorTypes1(self):
        pass

class FunctionCallTypeTests(ASTTest, unittest.TestCase):
    def testFunctionCallParameterType1(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-1")

    def testFunctionCallParameterType2(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-2")

    def testFunctionCallParameterType3(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-3")

    def testFunctionCallParameterType4(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-4")

    def testFunctionCallParameterType5(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-5")

    def testFunctionCallParameterType6(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-6")

    def testFunctionCallParameterType7(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-7")

    def testFunctionCallParameterType8(self):
        self.generateOneErrorAndCompare("testfiles/function-calls/parameter-type-8")

    def testFunctionCallParameterTypeCorrect(self):
        self.generateNoError("testfiles/function-calls/parameter-type-correct.c")

class VariableDeclarationTests(ASTTest, unittest.TestCase):
    def testVariableDeclaration1(self):
        self.generateOneErrorAndCompare("testfiles/variable-declarations/1")

    def testVariableDeclaration2(self):
        self.generateOneErrorAndCompare("testfiles/variable-declarations/2")

    def testVariableDeclaration3(self):
        self.generateOneErrorAndCompare("testfiles/variable-declarations/3")

    def testVariableDeclaration4(self):
        self.generateOneErrorAndCompare("testfiles/variable-declarations/4")

    def testVariableDeclaration5(self):
        self.generateOneErrorAndCompare("testfiles/variable-declarations/5")

    def testVariableDeclaration6(self):
        self.generateOneErrorAndCompare("testfiles/variable-declarations/6")

class FunctionDeclarationTests(ASTTest, unittest.TestCase):
    def testFunctionDeclaration1(self):
        self.generateOneErrorAndCompare("testfiles/function-declarations/1")

    def testFunctionDeclaration2(self):
        self.generateOneErrorAndCompare("testfiles/function-declarations/2")

def testAll():
    unittest.main()

if __name__=="__main__":
    testAll()
