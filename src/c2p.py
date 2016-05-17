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

    # create an AST an attach it to a listener so the listener can fill in the tree
    abstractSyntaxTree = AbstractSyntaxTree();

    # the errorHandler which will group all of the errors
    errorHandler = CompilerErrorHandler(filename)

    try:
        listener = Listener(abstractSyntaxTree)
        # walk the parse tree and fill in the AST
        walker.walk(listener, programContext)

        # print the resulting AST after the walk
        print (abstractSyntaxTree)

        # create a symbol table and symbol table filler, fill in the table and check if everything is declared before it is used in the c file
        symbolTable = SymbolTable()
        functionFiller = VisitorDefinitionProcessor(symbolTable, errorHandler)
        functionFiller.visitProgramNode(abstractSyntaxTree.root)
        symbolTable.traverseOn()
        symbolTable.resetToRoot()
        tableFiller = VisitorDeclarationProcessor(symbolTable, errorHandler)
        tableFiller.visitProgramNode(abstractSyntaxTree.root)
        print(symbolTable)

        # do the type checking
        typeCheck = VisitorTypeChecker(errorHandler)
        typeCheck.visitProgramNode(abstractSyntaxTree.root)

        # generate code
        symbolTable.resetToRoot()
        codeGenerator = VisitorCodeGenerator(symbolTable)
        codeGenerator.visitProgramNode(abstractSyntaxTree.root)

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
