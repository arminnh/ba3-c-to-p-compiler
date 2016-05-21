from antlr4_generated.SmallCLexer import SmallCLexer
from antlr4_generated.SmallCParser import SmallCParser

from AbstractSyntaxTree import *
from Listener import *
from CompilerErrorHandler import *
from SymbolTable import *
from VisitorDefinitionProcessor import *
from VisitorDeclarationProcessor import *
from VisitorTypeChecker import *
from VisitorCodeGenerator import *

import traceback
import sys
import time

def main(filename):
    timeNow = time.time()
    input_file = FileStream(filename)
    print ("file read: ", time.time() - timeNow)

    # get lexer
    timeNow = time.time()
    lexer = SmallCLexer(input_file)
    print ("file lexed: ", time.time() - timeNow)

    # get list of matched tokens
    timeNow = time.time()
    stream = CommonTokenStream(lexer)
    print ("file tokenized: ", time.time() - timeNow)

    # pass tokens to the parser
    parser = SmallCParser(stream)

    # specify the entry point
    timeNow = time.time()
    programContext = parser.program() # tree with program as root
    print ("file parsed: ", time.time() - timeNow)

    # quit if there are any syntax errors
    if parser._syntaxErrors > 0:
        sys.exit(0)

    # walk it and attach our listener
    walker = ParseTreeWalker()

    # create an AST an attach it to a listener so the listener can fill in the tree
    abstractSyntaxTree = AbstractSyntaxTree();

    # the errorHandler which will group all of the errors
    errorHandler = CompilerErrorHandler(filename)

    try:
        listener = Listener(abstractSyntaxTree)
        # walk the parse tree and fill in the AST
        timeNow = time.time()
        walker.walk(listener, programContext)
        print ("AST built: ", time.time() - timeNow)

        # print the resulting AST after the walk
        print (abstractSyntaxTree)

        # create a symbol table and symbol table filler, fill in the table and check if everything is declared before it is used in the c file
        symbolTable = SymbolTable()
        timeNow = time.time()
        functionFiller = VisitorDefinitionProcessor(symbolTable, errorHandler)
        functionFiller.visitProgramNode(abstractSyntaxTree.root)
        print ("symbol table filled: ", time.time() - timeNow)
        symbolTable.traverseOn()
        symbolTable.resetToRoot()
        timeNow = time.time()
        tableFiller = VisitorDeclarationProcessor(symbolTable, errorHandler)
        tableFiller.visitProgramNode(abstractSyntaxTree.root)
        print ("symbol table checked: ", time.time() - timeNow)
        print(symbolTable)

        # do the type checking
        timeNow = time.time()
        typeCheck = VisitorTypeChecker(errorHandler)
        typeCheck.visitProgramNode(abstractSyntaxTree.root)
        print ("program type checked: ", time.time() - timeNow)

        # generate code
        if not errorHandler.errorCount():
            symbolTable.resetToRoot()
            timeNow = time.time()
            codeGenerator = VisitorCodeGenerator(symbolTable)
            codeGenerator.visitProgramNode(abstractSyntaxTree.root)
            print ("code generated: ", time.time() - timeNow)

    except Exception as e:
        ex_type, ex, tb = sys.exc_info()
        traceback.print_exception(ex_type, ex, tb)

    if errorHandler.errorCount():
        print (errorHandler.errorCount(), "error" + ("s" if errorHandler.errorCount() != 1 else ""))
        errorHandler.printErrors()


if __name__=="__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 c2p.py filename\n")
        sys.exit()

    main(sys.argv[1])
