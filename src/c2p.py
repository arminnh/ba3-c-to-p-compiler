from antlr4 import *
from SmallCLexer import SmallCLexer
from SmallCListener import SmallCListener
from SmallCParser import SmallCParser
from AbstractSyntaxTree import *
from MyListener import *
from VisitorTypeCheck import *
from VisitorFillSymbolTable import *
import traceback

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

    errorHandler = CompilerErrorHandler(filename)
    # create an AST an attach it to a listener so the listener can fill in the tree
    abstractSyntaxTree = AbstractSyntaxTree(errorHandler);

    listener = MyListener(abstractSyntaxTree)

    try:
        # walk the parse tree and fill in the AST, this can throw exceptions (e.g. double main() definition)
        walker.walk(listener, programContext)

        # print the resulting AST after the walk
        print (abstractSyntaxTree)

        # create a symbol table and symbol table filler, fill in the table and check if everything is declared before it is used in the c file
        symbolTable = SymbolTable()
        tableFiller = VisitorFillSymbolTable(symbolTable, errorHandler)
        tableFiller.visitProgramNode(abstractSyntaxTree.root)
        print(symbolTable)

        #do the type checking of the c file
        # try:
        # abstractSyntaxTree.typeCheck()
        # except Exception as e:
        #     print(e)

        # VisitorSymbolTable()
        typeCheck = VisitorTypeCheck(errorHandler)
        typeCheck.visitProgramNode(abstractSyntaxTree.root)

        # VisitorCodeGeneration()

    except Exception as e:
        print (errorHandler.errorCount(), "error" + ("s" if errorHandler.errorCount() != 1 else ""))
        if errorHandler.errorCount():
            errorHandler.printError(0)
        else:
            ex_type, ex, tb = sys.exc_info()
            traceback.print_exception(ex_type, ex, tb)

if __name__=="__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 c2p.py filename\n")
        sys.exit()

    main(sys.argv[1])
