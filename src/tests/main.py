import unittest

# insert the tests directory into this path
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

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))

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
        abstractSyntaxTree = AbstractSyntaxTree(errorHandler=self.errorHandler);
        listener = MyListener(abstractSyntaxTree)
        walker.walk(listener, programContext)

        symbolTable = SymbolTable()
        tableFiller = ASTSymbolTableFiller(abstractSyntaxTree, symbolTable)
        tableFiller.fill()
        abstractSyntaxTree.typeCheck()

class ComparisonOperatorTypeTests(ASTTest, unittest.TestCase):

    def testIntEqualsFloat(self):
        self.parseFile("./testfiles/binary-operator-types.c")
        #TODO: compare output
        self.assertTrue(True)
        

def testAll():
    unittest.main()
    #test = ComparisonOperatorTypeTests()
    #test.testIntEqualsFloat()
    #print ("--- All tests passed ---")

if __name__=="__main__":
    testAll()
