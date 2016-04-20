from antlr4 import *
from smallcLexer import smallcLexer
from smallcListener import smallcListener
from smallcVisitor import smallcVisitor
from smallcParser import smallcParser



def main(filename):
    input_file = FileStream(filename)

    # get lexer
    lexer = smallcLexer(input_file)

    # get list of matched tokens
    stream = CommonTokenStream(lexer)

    # pass tokens to the parser
    parser = smallcParser(stream)

    # specify the entry point
    programContext = parser.program() # tree with program as root

    # walk it and attach our listener
    walker = ParseTreeWalker()
    listener = MyListener()
    walker.walk(listener, programContext)



class MyListener(smallcListener):
    def enterProgram(self, ctx:smallcParser.ProgramContext):
        print ("Program: " + ctx.getText())
        return

    def enterHeader(self, ctx:smallcParser.ProgramContext):
        print ("header: " + ctx.getText())
        return

    def enterIncludes(self, ctx:smallcParser.IncludesContext):
        print ("Includes: " + ctx.getText())
        return

    def enterMainFunction(self, ctx:smallcParser.MainFunctionContext):
        print ("MainFunction: " + ctx.getText())
        return

    def enterTypeDecl(self, ctx:smallcParser.TypeDeclContext):
        print ("TypeDecl: " + ctx.getText())
        return

    def enterFunctionBody(self, ctx:smallcParser.FunctionBodyContext):
        print ("FunctionBody: " + ctx.getText())
        return




if __name__=="__main__":
    main("testfiles/hello_world.c")
