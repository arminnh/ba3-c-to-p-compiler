from antlr4 import *
from SmallCLexer import SmallCLexer
from SmallCListener import SmallCListener
from SmallCVisitor import SmallCVisitor
from SmallCParser import SmallCParser



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
    listener = MyListener()
    walker.walk(listener, programContext)



class MyListener(SmallCListener):
    def enterProgram(self, ctx:SmallCParser.ProgramContext):
        print ("Program: " + ctx.getText())
        
        return

    def enterHeader(self, ctx:SmallCParser.ProgramContext):
        print ("header: " + ctx.getText())
        return 

    def enterIncludes(self, ctx:SmallCParser.IncludesContext):
        print ("Includes: " + ctx.getText())
        return 

    def enterMainFunction(self, ctx:SmallCParser.MainFunctionContext):
        print ("MainFunction: " + ctx.getText())
        return 

    def enterTypeDecl(self, ctx:SmallCParser.TypeDeclContext):
        print ("TypeDecl: " + ctx.getText())
        return 

    def enterFunctionBody(self, ctx:SmallCParser.FunctionBodyContext):
        print ("FunctionBody: " + ctx.getText())
        return 




if __name__=="__main__":
    main("testfiles/hello_world.c")
