# Generated from smallc.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\17")
        buf.write("\33\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\27\n\4\3\5\3\5\3\5")
        buf.write("\2\2\6\2\4\6\b\2\2\27\2\n\3\2\2\2\4\r\3\2\2\2\6\26\3\2")
        buf.write("\2\2\b\30\3\2\2\2\n\13\5\4\3\2\13\f\5\b\5\2\f\3\3\2\2")
        buf.write("\2\r\16\5\6\4\2\16\5\3\2\2\2\17\20\7\3\2\2\20\21\7\13")
        buf.write("\2\2\21\22\7\5\2\2\22\23\7\4\2\2\23\24\7\5\2\2\24\27\7")
        buf.write("\f\2\2\25\27\3\2\2\2\26\17\3\2\2\2\26\25\3\2\2\2\27\7")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\t\3\2\2\2\3\26")
        return buf.getvalue()


class smallcParser ( Parser ):

    grammarFileName = "smallc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'.'", "<INVALID>", "'(.*?)'", 
                     "<INVALID>", "','", "'('", "')'", "'<'", "'>'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "NUMBER", "COMMA", "LBRA", "RBRA", "LABRA", "RABRA", 
                      "LCBRA", "RCBRA", "WS" ]

    RULE_program = 0
    RULE_header = 1
    RULE_includes = 2
    RULE_mainFunction = 3

    ruleNames =  [ "program", "header", "includes", "mainFunction" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    STRING=4
    NUMBER=5
    COMMA=6
    LBRA=7
    RBRA=8
    LABRA=9
    RABRA=10
    LCBRA=11
    RCBRA=12
    WS=13

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = smallcParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.header()
            self.state = 9
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = smallcParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludes" ):
                return visitor.visitIncludes(self)
            else:
                return visitor.visitChildren(self)




    def includes(self):

        localctx = smallcParser.IncludesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_includes)
        try:
            self.state = 20
            token = self._input.LA(1)
            if token in [smallcParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(smallcParser.T__0)
                self.state = 14
                self.match(smallcParser.LABRA)
                self.state = 15
                self.match(smallcParser.ID)
                self.state = 16
                self.match(smallcParser.T__1)
                self.state = 17
                self.match(smallcParser.ID)
                self.state = 18
                self.match(smallcParser.RABRA)

            elif token in [smallcParser.EOF]:
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


        def getRuleIndex(self):
            return smallcParser.RULE_mainFunction

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

        localctx = smallcParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





