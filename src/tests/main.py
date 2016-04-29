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

    def exampleTestForCopyPasting(self):
        filename = "testfiles/binary-operator-types"

        with self.assertRaises(Exception) as context:
            self.parseFile(filename + ".c")

        self.assertTrue(self.errorHandler.errorCount() == 1)

        # if there is error output generated, compare with txt file
        with open(filename + ".txt", 'r') as myfile:
            correctOutput = myfile.read()

        # remove all whitespace
        errorMessageNoWhitespace = re.sub('[ \t\n\r]', '', self.errorHandler.errorToString(0))
        correctOutput = re.sub('[ \t\n\r]', '', correctOutput)

        self.assertTrue(errorMessageNoWhitespace.find(correctOutput) != -1)

class ComparisonOperatorTypeTests(ASTTest, unittest.TestCase):

    def testIntEqualsFloat(self):
        filename = "testfiles/binary-operator-types"

        with self.assertRaises(Exception) as context:
            self.parseFile(filename + ".c")

        self.assertTrue(self.errorHandler.errorCount() == 1)

        with open(filename + ".txt", 'r') as myfile:
            correctOutput = myfile.read()

        errorMessageNoWhitespace = str(re.sub('[ \t\n\r]', '', self.errorHandler.errorToString(0)))
        correctOutput = re.sub('[ \t\n\r]', '', correctOutput)

        #messageNoWhitespace = str(re.sub('[ \t\n\r]', '', str(context.exception)))
        #print (messageNoWhitespace.lower().find("errorhasoccur") != -1)
        #self.assertTrue(messageNoWhitespace.lower().find("errorhasoccur") != -1)

        #print(self.errorHandler.errorToString(0))
        #print (errorNoWhitespace.find("Errorat2:6:Comparisonoperatoroperandsneedtobeofsametype1==2.0;^") != -1)

        print("correctOutput: " + correctOutput)
        print("errorMessageNoWhitespace: " + errorMessageNoWhitespace)
        self.assertTrue(errorMessageNoWhitespace.find(correctOutput) != -1)

class FunctionCallTypeTests(ASTTest, unittest.TestCase):
    def testFunctionCallReturnType1(self):
        filename = "testfiles/function-call-parameter-type-1"

        with self.assertRaises(Exception) as context:
            self.parseFile(filename + ".c")

        self.assertTrue(self.errorHandler.errorCount() == 1)

        # if there is error output generated, compare with txt file
        with open(filename + ".txt", 'r') as myfile:
            correctOutput = myfile.read()

        # remove all whitespace
        errorMessageNoWhitespace = re.sub('[ \t\n\r]', '', self.errorHandler.errorToString(0))
        correctOutput = re.sub('[ \t\n\r]', '', correctOutput)
        self.assertTrue(errorMessageNoWhitespace.find(correctOutput) != -1)

def testAll():
    unittest.main()


if __name__=="__main__":
    testAll()
