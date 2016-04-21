# Generated from SmallC.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\30")
        buf.write("E\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\7\3\32\n\3\f")
        buf.write("\3\16\3\35\13\3\3\4\3\4\3\4\3\4\5\4#\n\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7\60\n\7\r\7\16\7\61")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\tA\n\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3")
        buf.write("\2\20\22?\2\24\3\2\2\2\4\33\3\2\2\2\6\"\3\2\2\2\b$\3\2")
        buf.write("\2\2\n&\3\2\2\2\f(\3\2\2\2\16\65\3\2\2\2\20@\3\2\2\2\22")
        buf.write("B\3\2\2\2\24\25\5\4\3\2\25\26\5\f\7\2\26\3\3\2\2\2\27")
        buf.write("\30\7\3\2\2\30\32\5\6\4\2\31\27\3\2\2\2\32\35\3\2\2\2")
        buf.write("\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\33\3\2\2")
        buf.write("\2\36\37\7\13\2\2\37 \7\26\2\2 #\7\f\2\2!#\7\27\2\2\"")
        buf.write("\36\3\2\2\2\"!\3\2\2\2#\7\3\2\2\2$%\3\2\2\2%\t\3\2\2\2")
        buf.write("&\'\3\2\2\2\'\13\3\2\2\2()\5\16\b\2)*\7\4\2\2*+\7\t\2")
        buf.write("\2+,\7\5\2\2,-\7\n\2\2-/\7\r\2\2.\60\5\20\t\2/.\3\2\2")
        buf.write("\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\64\7\16\2\2\64\r\3\2\2\2\65\66\t\2\2\2\66\17\3\2")
        buf.write("\2\2\678\7\23\2\289\7\t\2\29:\7\27\2\2:;\7\n\2\2;A\7\6")
        buf.write("\2\2<=\7\24\2\2=>\5\22\n\2>?\7\6\2\2?A\3\2\2\2@\67\3\2")
        buf.write("\2\2@<\3\2\2\2A\21\3\2\2\2BC\7\25\2\2C\23\3\2\2\2\6\33")
        buf.write("\"\61@")
        return buf.getvalue()


class SmallCParser ( Parser ):

    grammarFileName = "SmallC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'main'", "'void'", "';'", 
                     "'*'", "','", "'('", "')'", "'<'", "'>'", "'{'", "'}'", 
                     "'\"'", "'char'", "'float'", "'int'", "<INVALID>", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PTR", "COMMA", "LBRA", "RBRA", "LABRA", 
                      "RABRA", "LCBRA", "RCBRA", "QUOTE", "CHAR", "FLOAT", 
                      "INT", "CFUN", "RETURN", "NUMBER", "STRING1", "STRING2", 
                      "WS" ]

    RULE_program = 0
    RULE_header = 1
    RULE_include = 2
    RULE_stdInclude = 3
    RULE_customInclude = 4
    RULE_mainFunction = 5
    RULE_typeDecl = 6
    RULE_functionBody = 7
    RULE_number = 8

    ruleNames =  [ "program", "header", "include", "stdInclude", "customInclude", 
                   "mainFunction", "typeDecl", "functionBody", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PTR=5
    COMMA=6
    LBRA=7
    RBRA=8
    LABRA=9
    RABRA=10
    LCBRA=11
    RCBRA=12
    QUOTE=13
    CHAR=14
    FLOAT=15
    INT=16
    CFUN=17
    RETURN=18
    NUMBER=19
    STRING1=20
    STRING2=21
    WS=22

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(SmallCParser.HeaderContext,0)


        def mainFunction(self):
            return self.getTypedRuleContext(SmallCParser.MainFunctionContext,0)


        def getRuleIndex(self):
            return SmallCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SmallCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.header()
            self.state = 19
            self.mainFunction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallCParser.IncludeContext)
            else:
                return self.getTypedRuleContext(SmallCParser.IncludeContext,i)


        def getRuleIndex(self):
            return SmallCParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = SmallCParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SmallCParser.T__0:
                self.state = 21
                self.match(SmallCParser.T__0)
                self.state = 22
                self.include()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABRA(self):
            return self.getToken(SmallCParser.LABRA, 0)

        def STRING1(self):
            return self.getToken(SmallCParser.STRING1, 0)

        def RABRA(self):
            return self.getToken(SmallCParser.RABRA, 0)

        def STRING2(self):
            return self.getToken(SmallCParser.STRING2, 0)

        def getRuleIndex(self):
            return SmallCParser.RULE_include

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude" ):
                listener.enterInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude" ):
                listener.exitInclude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude" ):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)




    def include(self):

        localctx = SmallCParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_include)
        try:
            self.state = 32
            token = self._input.LA(1)
            if token in [SmallCParser.LABRA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(SmallCParser.LABRA)
                self.state = 29
                self.match(SmallCParser.STRING1)
                self.state = 30
                self.match(SmallCParser.RABRA)

            elif token in [SmallCParser.STRING2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(SmallCParser.STRING2)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StdIncludeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SmallCParser.RULE_stdInclude

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStdInclude" ):
                listener.enterStdInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStdInclude" ):
                listener.exitStdInclude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStdInclude" ):
                return visitor.visitStdInclude(self)
            else:
                return visitor.visitChildren(self)




    def stdInclude(self):

        localctx = SmallCParser.StdIncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stdInclude)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CustomIncludeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SmallCParser.RULE_customInclude

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCustomInclude" ):
                listener.enterCustomInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCustomInclude" ):
                listener.exitCustomInclude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCustomInclude" ):
                return visitor.visitCustomInclude(self)
            else:
                return visitor.visitChildren(self)




    def customInclude(self):

        localctx = SmallCParser.CustomIncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_customInclude)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDecl(self):
            return self.getTypedRuleContext(SmallCParser.TypeDeclContext,0)


        def LBRA(self):
            return self.getToken(SmallCParser.LBRA, 0)

        def RBRA(self):
            return self.getToken(SmallCParser.RBRA, 0)

        def LCBRA(self):
            return self.getToken(SmallCParser.LCBRA, 0)

        def RCBRA(self):
            return self.getToken(SmallCParser.RCBRA, 0)

        def functionBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallCParser.FunctionBodyContext)
            else:
                return self.getTypedRuleContext(SmallCParser.FunctionBodyContext,i)


        def getRuleIndex(self):
            return SmallCParser.RULE_mainFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainFunction" ):
                listener.enterMainFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainFunction" ):
                listener.exitMainFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainFunction" ):
                return visitor.visitMainFunction(self)
            else:
                return visitor.visitChildren(self)




    def mainFunction(self):

        localctx = SmallCParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mainFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.typeDecl()
            self.state = 39
            self.match(SmallCParser.T__1)
            self.state = 40
            self.match(SmallCParser.LBRA)
            self.state = 41
            self.match(SmallCParser.T__2)
            self.state = 42
            self.match(SmallCParser.RBRA)
            self.state = 43
            self.match(SmallCParser.LCBRA)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.functionBody()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SmallCParser.CFUN or _la==SmallCParser.RETURN):
                    break

            self.state = 49
            self.match(SmallCParser.RCBRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(SmallCParser.CHAR, 0)

        def FLOAT(self):
            return self.getToken(SmallCParser.FLOAT, 0)

        def INT(self):
            return self.getToken(SmallCParser.INT, 0)

        def getRuleIndex(self):
            return SmallCParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = SmallCParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmallCParser.CHAR) | (1 << SmallCParser.FLOAT) | (1 << SmallCParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CFUN(self):
            return self.getToken(SmallCParser.CFUN, 0)

        def LBRA(self):
            return self.getToken(SmallCParser.LBRA, 0)

        def STRING2(self):
            return self.getToken(SmallCParser.STRING2, 0)

        def RBRA(self):
            return self.getToken(SmallCParser.RBRA, 0)

        def RETURN(self):
            return self.getToken(SmallCParser.RETURN, 0)

        def number(self):
            return self.getTypedRuleContext(SmallCParser.NumberContext,0)


        def getRuleIndex(self):
            return SmallCParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = SmallCParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionBody)
        try:
            self.state = 62
            token = self._input.LA(1)
            if token in [SmallCParser.CFUN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(SmallCParser.CFUN)
                self.state = 54
                self.match(SmallCParser.LBRA)
                self.state = 55
                self.match(SmallCParser.STRING2)
                self.state = 56
                self.match(SmallCParser.RBRA)
                self.state = 57
                self.match(SmallCParser.T__3)

            elif token in [SmallCParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(SmallCParser.RETURN)
                self.state = 59
                self.number()
                self.state = 60
                self.match(SmallCParser.T__3)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SmallCParser.NUMBER, 0)

        def getRuleIndex(self):
            return SmallCParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = SmallCParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(SmallCParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





