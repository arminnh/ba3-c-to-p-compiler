from antlr4 import *
from smallcLexer import smallcLexer
from smallcListener import smallcListener
from smallcVisitor import smallcVisitor
from smallcParser import smallcParser

def main(filename):
    input_file = FileStream(filename)
    lexer = smallcLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = smallcParser(stream)
    tree = parser.program() # top rule

if __name__=="__main__":
    main("testfiles/hello_world.c")
