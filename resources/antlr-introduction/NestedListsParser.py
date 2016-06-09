# Generated from NestedLists.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\6")
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\3\5\3\27\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\36\n\4\3\4\2\2\5\2\4\6\2\2 \2\b\3\2")
        buf.write("\2\2\4\26\3\2\2\2\6\35\3\2\2\2\b\t\7\3\2\2\t\n\5\4\3\2")
        buf.write("\n\13\7\4\2\2\13\3\3\2\2\2\f\27\5\6\4\2\r\22\5\6\4\2\16")
        buf.write("\17\7\5\2\2\17\21\5\6\4\2\20\16\3\2\2\2\21\24\3\2\2\2")
        buf.write("\22\20\3\2\2\2\22\23\3\2\2\2\23\27\3\2\2\2\24\22\3\2\2")
        buf.write("\2\25\27\3\2\2\2\26\f\3\2\2\2\26\r\3\2\2\2\26\25\3\2\2")
        buf.write("\2\27\5\3\2\2\2\30\31\7\3\2\2\31\32\5\4\3\2\32\33\7\4")
        buf.write("\2\2\33\36\3\2\2\2\34\36\7\6\2\2\35\30\3\2\2\2\35\34\3")
        buf.write("\2\2\2\36\7\3\2\2\2\5\22\26\35")
        return buf.getvalue()


class NestedListsParser ( Parser ):

    grammarFileName = "NestedLists.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT" ]

    RULE_nstdlst = 0
    RULE_lst = 1
    RULE_itm = 2

    ruleNames =  [ "nstdlst", "lst", "itm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INT=4

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NstdlstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lst(self):
            return self.getTypedRuleContext(NestedListsParser.LstContext,0)


        def getRuleIndex(self):
            return NestedListsParser.RULE_nstdlst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNstdlst" ):
                listener.enterNstdlst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNstdlst" ):
                listener.exitNstdlst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNstdlst" ):
                return visitor.visitNstdlst(self)
            else:
                return visitor.visitChildren(self)




    def nstdlst(self):

        localctx = NestedListsParser.NstdlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nstdlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(NestedListsParser.T__0)
            self.state = 7
            self.lst()
            self.state = 8
            self.match(NestedListsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def itm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NestedListsParser.ItmContext)
            else:
                return self.getTypedRuleContext(NestedListsParser.ItmContext,i)


        def getRuleIndex(self):
            return NestedListsParser.RULE_lst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLst" ):
                listener.enterLst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLst" ):
                listener.exitLst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst" ):
                return visitor.visitLst(self)
            else:
                return visitor.visitChildren(self)




    def lst(self):

        localctx = NestedListsParser.LstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lst)
        self._la = 0 # Token type
        try:
            self.state = 20
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.itm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.itm()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NestedListsParser.T__2:
                    self.state = 12
                    self.match(NestedListsParser.T__2)
                    self.state = 13
                    self.itm()
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lst(self):
            return self.getTypedRuleContext(NestedListsParser.LstContext,0)


        def INT(self):
            return self.getToken(NestedListsParser.INT, 0)

        def getRuleIndex(self):
            return NestedListsParser.RULE_itm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItm" ):
                listener.enterItm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItm" ):
                listener.exitItm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItm" ):
                return visitor.visitItm(self)
            else:
                return visitor.visitChildren(self)




    def itm(self):

        localctx = NestedListsParser.ItmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_itm)
        try:
            self.state = 27
            token = self._input.LA(1)
            if token in [NestedListsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(NestedListsParser.T__0)
                self.state = 23
                self.lst()
                self.state = 24
                self.match(NestedListsParser.T__1)

            elif token in [NestedListsParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(NestedListsParser.INT)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





