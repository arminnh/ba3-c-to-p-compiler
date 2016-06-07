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

import argparse
import traceback
import sys
import time
import os.path


# GLOBAL VARIABLES
SAVE_AST          = False
SAVE_SYMBOL_TABLE = False
PRINT_TIMINGS     = False
PRINT_NOTHING     = False
OUT_FILE_NAME     = "out.p"


def output(text, is_timing=False):
    if PRINT_NOTHING:
        return

    if is_timing and not PRINT_TIMINGS:
        return

    print(text)


def parseFile(filename):
    timeNow = time.time()
    input_file = FileStream(filename)
    output("file read:            " + str(time.time() - timeNow), is_timing=True)

    # get lexer
    timeNow = time.time()
    lexer = CLexer(input_file)
    output("file lexed:           " + str(time.time() - timeNow), is_timing=True)

    # get list of matched tokens
    timeNow = time.time()
    stream = CommonTokenStream(lexer)
    output("file tokenized:       " + str(time.time() - timeNow), is_timing=True)

    # pass tokens to the parser
    parser = CParser(stream)

    # specify the entry point
    timeNow = time.time()
    programContext = parser.program() # tree with program as root
    output("file parsed:          " + str(time.time() - timeNow), is_timing=True)

    # quit if there are any syntax errors
    if parser._syntaxErrors > 0:
        sys.exit(0)

    return programContext


def buildAST(parseTreeRoot):
    timeNow = time.time()

    # create an AST an attach it to a listener so the listener can fill in the tree
    abstractSyntaxTree = AbstractSyntaxTree()

    walker = ParseTreeWalker()
    listener = Listener(abstractSyntaxTree)
    # attach the listener, walk the parse tree, and fill in the AST
    walker.walk(listener, parseTreeRoot)

    # output the resulting AST after the walk
    output("AST built:            " + str(time.time() - timeNow), is_timing=True)

    if SAVE_AST:
        # os.path.splitext(name) splits name into tuple: (name without extension, extension)
        filename = os.path.splitext(OUT_FILE_NAME)[0] + "_AST.txt"
        outfile = open(filename, "w")
        outfile.write(str(abstractSyntaxTree))
        outfile.close()

    return abstractSyntaxTree


def scopeCheck(abstractSyntaxTree, errorHandler, symbolTable):
    timeNow = time.time()
    functionFiller = VisitorDefinitionProcessor(symbolTable, errorHandler)
    functionFiller.visitProgramNode(abstractSyntaxTree.root)
    output("symbol table filled:  " + str(time.time() - timeNow), is_timing=True)

    symbolTable.traverseOn()
    symbolTable.resetToRoot()

    timeNow = time.time()
    tableFiller = VisitorDeclarationProcessor(symbolTable, errorHandler)
    tableFiller.visitProgramNode(abstractSyntaxTree.root)
    output("symbol table checked: " + str(time.time() - timeNow), is_timing=True)

    if SAVE_SYMBOL_TABLE:
        # os.path.splitext(name) splits name into tuple: (name without extension, extension)
        filename = os.path.splitext(OUT_FILE_NAME)[0] + "_symbol_table.txt"
        outfile = open(filename, "w")
        outfile.write(str(symbolTable))
        outfile.close()


def typeCheck(abstractSyntaxTree, errorHandler):
    timeNow = time.time()
    typeCheck = VisitorTypeChecker(errorHandler)
    typeCheck.visitProgramNode(abstractSyntaxTree.root)
    output("program type checked: " + str(time.time() - timeNow), is_timing=True)


def generateCode(abstractSyntaxTree, symbolTable):
    timeNow = time.time()
    codeGenerator = VisitorCodeGenerator(symbolTable, OUT_FILE_NAME)
    codeGenerator.visitProgramNode(abstractSyntaxTree.root)
    output("code generated:       " + str(time.time() - timeNow), is_timing=True)


def main(filename):
    # get the root of the parse tree of the input file
    parseTreeRoot = parseFile(filename)

    # the errorHandler which will group all of the errors
    errorHandler = ErrorHandler(filename)

    try:
        # create an AST an attach it to a listener so the listener can fill in the tree
        abstractSyntaxTree = buildAST(parseTreeRoot)

        # create a symbol table and symbol table filler, fill in the table and check if everything is declared before it is used in the c file
        symbolTable = SymbolTable()
        scopeCheck(abstractSyntaxTree, errorHandler, symbolTable)

        # do the type checking
        typeCheck(abstractSyntaxTree, errorHandler)

        # output the decorated AST and the symbolTable after decorating the AST
        output(str(abstractSyntaxTree))
        output(str(symbolTable))

        # generate code
        symbolTable.resetToRoot()
        if not errorHandler.errorCount():
            generateCode(abstractSyntaxTree, symbolTable)

    except Exception as e:
        ex_type, ex, tb = sys.exc_info()
        traceback.print_exception(ex_type, ex, tb)

    if errorHandler.errorCount() or errorHandler.warningCount():
        print(str(errorHandler.errorCount()) + " error" + ("s" if errorHandler.errorCount() != 1 else ""))
        print(str(errorHandler.warningCount()) + " warning" + ("s" if errorHandler.warningCount() != 1 else ""))
        errorHandler.printErrors()


if __name__=="__main__":
    argparser = argparse.ArgumentParser(description="A C to P compiler")

    argparser.add_argument("filename",                                         help="The filename of the c program")
    # saveast as per assignment constraint
    argparser.add_argument("-save-ast", "--save-ast", "-saveast", "--saveast", help="Serializes the AST and saves it to {OUTFILE}_AST.txt", action="store_true", default=False)
    argparser.add_argument("-save-symbol-table", "--save-symbol-table",        help="Serializes the symbol table and saves it to {OUTFILE}_symbol_table.txt", action="store_true", default=False)
    argparser.add_argument("-t", "--timings",                                  help="Shows how long each step of the process takes", action="store_true", default=False)
    argparser.add_argument("-q", "--quiet",                                    help="Disables the printing of the AST and symbol table", action="store_true", default=False)
    argparser.add_argument("-o",                                               help="Specifies the output filename (preferably with .p filename extension)", default="out.p")
    args = argparser.parse_args()

    # set global variables
    SAVE_AST          = args.save_ast
    SAVE_SYMBOL_TABLE = args.save_symbol_table
    PRINT_TIMINGS     = args.timings
    PRINT_NOTHING     = args.quiet
    OUT_FILE_NAME     = args.o

    main(args.filename)
