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

import argparse
import traceback
import sys
import time

arg_save_ast          = False
arg_save_symbol_table = False
arg_timings           = False
arg_quiet             = False
arg_out_filename      = "out.p"

def output(text, print_arg=None):
    if print_arg is not None:
        if print_arg:
            print(text)
    elif not arg_quiet:
        print(text)

def main(filename):
    timeNow = time.time()
    input_file = FileStream(filename)
    output("file read:            " + str(time.time() - timeNow), arg_timings)

    # get lexer
    timeNow = time.time()
    lexer = SmallCLexer(input_file)
    output("file lexed:           " + str(time.time() - timeNow), arg_timings)

    # get list of matched tokens
    timeNow = time.time()
    stream = CommonTokenStream(lexer)
    output("file tokenized:       " + str(time.time() - timeNow), arg_timings)

    # pass tokens to the parser
    parser = SmallCParser(stream)

    # specify the entry point
    timeNow = time.time()
    programContext = parser.program() # tree with program as root
    output("file parsed:          " + str(time.time() - timeNow), arg_timings)

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
        output("AST built:            " + str(time.time() - timeNow), arg_timings)

        # output the resulting AST after the walk
        output(str(abstractSyntaxTree))

        # create a symbol table and symbol table filler, fill in the table and check if everything is declared before it is used in the c file
        symbolTable = SymbolTable()
        timeNow = time.time()
        functionFiller = VisitorDefinitionProcessor(symbolTable, errorHandler)
        functionFiller.visitProgramNode(abstractSyntaxTree.root)
        output("symbol table filled:  " + str(time.time() - timeNow), arg_timings)
        symbolTable.traverseOn()
        symbolTable.resetToRoot()
        timeNow = time.time()
        tableFiller = VisitorDeclarationProcessor(symbolTable, errorHandler)
        tableFiller.visitProgramNode(abstractSyntaxTree.root)
        output("symbol table checked: " + str(time.time() - timeNow), arg_timings)
        output(str(symbolTable))

        # do the type checking
        timeNow = time.time()
        typeCheck = VisitorTypeChecker(errorHandler)
        typeCheck.visitProgramNode(abstractSyntaxTree.root)
        output("program type checked: " + str(time.time() - timeNow), arg_timings)

        # generate code
        # if not errorHandler.errorCount():
        #     symbolTable.resetToRoot()
        #     timeNow = time.time()
        #     codeGenerator = VisitorCodeGenerator(symbolTable, arg_out_filename)
        #     codeGenerator.visitProgramNode(abstractSyntaxTree.root)
        #     output("code generated:       " + str(time.time() - timeNow), arg_timings)

    except Exception as e:
        ex_type, ex, tb = sys.exc_info()
        traceback.print_exception(ex_type, ex, tb)

    if errorHandler.errorCount():
        print(str(errorHandler.errorCount()) + " error" + ("s" if errorHandler.errorCount() != 1 else ""))
        errorHandler.printErrors()


if __name__=="__main__":

    argparser = argparse.ArgumentParser(description="A C to P compiler")

    argparser.add_argument("filename",                                         help="The filename of the c program")
    argparser.add_argument("-save-ast", "--save-ast", "-saveast", "--saveast", help="Serializes the AST and saves it to c2p_AST.txt", action="store_true", default=False) # saveast as per assignment constraints
    argparser.add_argument("-save-symbol-table", "--save-symbol-table",        help="Serializes the symbol table and saves it to c2p_symbol_table.txt", action="store_true", default=False)
    argparser.add_argument("-t", "--timings",                                  help="Shows how long each step of the process takes", action="store_true", default=False)
    argparser.add_argument("-q", "--quiet",                                    help="Disables the printing of the AST and symbol table", action="store_true", default=False)
    argparser.add_argument("-o",                                               help="Specifies the output filename (preferably with .p filename extension)", default="out.p")
    args = argparser.parse_args()

    arg_save_ast = args.save_ast
    arg_save_symbol_table = args.save_symbol_table
    arg_timings = args.timings
    arg_quiet  = args.quiet
    arg_out_filename = args.o

    # output("args: " + str(args) + "\n" + "save_ast: " + str(arg_save_ast) + ", save_symbl_table: " + str(arg_save_symbol_table) + ", timings: " + str(arg_timings) + ", quiet: " + str(arg_quiet) + "\n")

    main(args.filename)
