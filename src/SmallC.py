from antlr4 import *
from SmallCLexer import SmallCLexer
from SmallCListener import SmallCListener
from SmallCVisitor import SmallCVisitor
from SmallCParser import SmallCParser
from AbstractSyntaxTree import *
from MyListener import *
from ASTWalker import *
from ASTSymbolTableFiller import *

import sys

def main(filename):
    input_file = FileStream(filename)

    # get lexer
    lexer = SmallCLexer(input_file)

    # get list of matched tokens
    stream = CommonTokenStream(lexer)

    # pass tokens to the parser
    parser = SmallCParser(stream)

    # specify the entry point
    programContext = parser.program() # tree with program as root

    # walk it and attach our listener
    walker = ParseTreeWalker()
    abstractSyntaxTree = AbstractSyntaxTree();
    listener = MyListener(abstractSyntaxTree)
    walker.walk(listener, programContext)

    print (abstractSyntaxTree)

    symbolTable = SymbolTable()

    tableFiller = ASTSymbolTableFiller(abstractSyntaxTree, symbolTable)
    #tableFiller.fill()
    #print(symbolTable)




if __name__=="__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 SmallC.py filename\n")
        sys.exit()


    main(sys.argv[1])
