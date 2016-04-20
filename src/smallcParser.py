# Generated from smallc.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\30")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\33")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\6\5$\n\5\r\5\16\5%\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\64")
        buf.write("\n\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\20\22\62\2\16\3\2\2")
        buf.write("\2\4\21\3\2\2\2\6\32\3\2\2\2\b\34\3\2\2\2\n)\3\2\2\2\f")
        buf.write("\63\3\2\2\2\16\17\5\4\3\2\17\20\5\b\5\2\20\3\3\2\2\2\21")
        buf.write("\22\5\6\4\2\22\5\3\2\2\2\23\24\7\3\2\2\24\25\7\f\2\2\25")
        buf.write("\26\7\25\2\2\26\27\7\4\2\2\27\30\7\25\2\2\30\33\7\r\2")
        buf.write("\2\31\33\3\2\2\2\32\23\3\2\2\2\32\31\3\2\2\2\33\7\3\2")
        buf.write("\2\2\34\35\5\n\6\2\35\36\7\5\2\2\36\37\7\n\2\2\37 \7\6")
        buf.write("\2\2 !\7\13\2\2!#\7\16\2\2\"$\5\f\7\2#\"\3\2\2\2$%\3\2")
        buf.write("\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\7\17\2\2(\t\3\2")
        buf.write("\2\2)*\t\2\2\2*\13\3\2\2\2+,\7\23\2\2,-\7\n\2\2-.\7\27")
        buf.write("\2\2./\7\13\2\2/\64\7\7\2\2\60\61\7\24\2\2\61\62\7\26")
        buf.write("\2\2\62\64\7\7\2\2\63+\3\2\2\2\63\60\3\2\2\2\64\r\3\2")
        buf.write("\2\2\5\32%\63")
        return buf.getvalue()


class smallcParser ( Parser ):

    grammarFileName = "smallc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'.'", "'main'", "'void'", 
                     "';'", "'*'", "','", "'('", "')'", "'<'", "'>'", "'{'", 
                     "'}'", "'char'", "'float'", "'int'", "<INVALID>", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PTR", "COMMA", "LBRA", 
                      "RBRA", "LABRA", "RABRA", "LCBRA", "RCBRA", "CHAR", 
                      "FLOAT", "INT", "CFUN", "RETURN", "ID", "NUMBER", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_header = 1
    RULE_includes = 2
    RULE_mainFunction = 3
    RULE_typeDecl = 4
    RULE_functionBody = 5

    ruleNames =  [ "program", "header", "includes", "mainFunction", "typeDecl", 
                   "functionBody" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    PTR=6
    COMMA=7
    LBRA=8
    RBRA=9
    LABRA=10
    RABRA=11
    LCBRA=12
    RCBRA=13
    CHAR=14
    FLOAT=15
    INT=16
    CFUN=17
    RETURN=18
    ID=19
    NUMBER=20
    STRING=21
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
            return self.getTypedRuleContext(smallcParser.HeaderContext,0)


        def mainFunction(self):
            return self.getTypedRuleContext(smallcParser.MainFunctionContext,0)


        def getRuleIndex(self):
            return smallcParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = smallcParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.header()
            self.state = 13
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

        def includes(self):
            return self.getTypedRuleContext(smallcParser.IncludesContext,0)


        def getRuleIndex(self):
            return smallcParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = smallcParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.includes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABRA(self):
            return self.getToken(smallcParser.LABRA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(smallcParser.ID)
            else:
                return self.getToken(smallcParser.ID, i)

        def RABRA(self):
            return self.getToken(smallcParser.RABRA, 0)

        def getRuleIndex(self):
            return smallcParser.RULE_includes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludes" ):
                listener.enterIncludes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludes" ):
                listener.exitIncludes(self)




    def includes(self):

        localctx = smallcParser.IncludesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_includes)
        try:
            self.state = 24
            token = self._input.LA(1)
            if token in [smallcParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(smallcParser.T__0)
                self.state = 18
                self.match(smallcParser.LABRA)
                self.state = 19
                self.match(smallcParser.ID)
                self.state = 20
                self.match(smallcParser.T__1)
                self.state = 21
                self.match(smallcParser.ID)
                self.state = 22
                self.match(smallcParser.RABRA)

            elif token in [smallcParser.CHAR, smallcParser.FLOAT, smallcParser.INT]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

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
            return self.getTypedRuleContext(smallcParser.TypeDeclContext,0)


        def LBRA(self):
            return self.getToken(smallcParser.LBRA, 0)

        def RBRA(self):
            return self.getToken(smallcParser.RBRA, 0)

        def LCBRA(self):
            return self.getToken(smallcParser.LCBRA, 0)

        def RCBRA(self):
            return self.getToken(smallcParser.RCBRA, 0)

        def functionBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smallcParser.FunctionBodyContext)
            else:
                return self.getTypedRuleContext(smallcParser.FunctionBodyContext,i)


        def getRuleIndex(self):
            return smallcParser.RULE_mainFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainFunction" ):
                listener.enterMainFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainFunction" ):
                listener.exitMainFunction(self)




    def mainFunction(self):

        localctx = smallcParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mainFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.typeDecl()
            self.state = 27
            self.match(smallcParser.T__2)
            self.state = 28
            self.match(smallcParser.LBRA)
            self.state = 29
            self.match(smallcParser.T__3)
            self.state = 30
            self.match(smallcParser.RBRA)
            self.state = 31
            self.match(smallcParser.LCBRA)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.functionBody()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==smallcParser.CFUN or _la==smallcParser.RETURN):
                    break

            self.state = 37
            self.match(smallcParser.RCBRA)
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
            return self.getToken(smallcParser.CHAR, 0)

        def FLOAT(self):
            return self.getToken(smallcParser.FLOAT, 0)

        def INT(self):
            return self.getToken(smallcParser.INT, 0)

        def getRuleIndex(self):
            return smallcParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)




    def typeDecl(self):

        localctx = smallcParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << smallcParser.CHAR) | (1 << smallcParser.FLOAT) | (1 << smallcParser.INT))) != 0)):
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
            return self.getToken(smallcParser.CFUN, 0)

        def LBRA(self):
            return self.getToken(smallcParser.LBRA, 0)

        def STRING(self):
            return self.getToken(smallcParser.STRING, 0)

        def RBRA(self):
            return self.getToken(smallcParser.RBRA, 0)

        def RETURN(self):
            return self.getToken(smallcParser.RETURN, 0)

        def NUMBER(self):
            return self.getToken(smallcParser.NUMBER, 0)

        def getRuleIndex(self):
            return smallcParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = smallcParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionBody)
        try:
            self.state = 49
            token = self._input.LA(1)
            if token in [smallcParser.CFUN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(smallcParser.CFUN)
                self.state = 42
                self.match(smallcParser.LBRA)
                self.state = 43
                self.match(smallcParser.STRING)
                self.state = 44
                self.match(smallcParser.RBRA)
                self.state = 45
                self.match(smallcParser.T__4)

            elif token in [smallcParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(smallcParser.RETURN)
                self.state = 47
                self.match(smallcParser.NUMBER)
                self.state = 48
                self.match(smallcParser.T__4)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





