# Generated from lists.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\7 \4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\3\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\5\3\30\n\3")
        buf.write(u"\3\4\3\4\5\4\34\n\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\36")
        buf.write(u"\2\n\3\2\2\2\4\27\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n")
        buf.write(u"\13\7\5\2\2\13\f\5\4\3\2\f\r\7\6\2\2\r\16\b\2\1\2\16")
        buf.write(u"\3\3\2\2\2\17\24\5\6\4\2\20\21\7\4\2\2\21\23\5\4\3\2")
        buf.write(u"\22\20\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25\3\2")
        buf.write(u"\2\2\25\30\3\2\2\2\26\24\3\2\2\2\27\17\3\2\2\2\27\30")
        buf.write(u"\3\2\2\2\30\5\3\2\2\2\31\34\5\b\5\2\32\34\5\2\2\2\33")
        buf.write(u"\31\3\2\2\2\33\32\3\2\2\2\34\7\3\2\2\2\35\36\7\3\2\2")
        buf.write(u"\36\t\3\2\2\2\5\24\27\33")
        return buf.getvalue()


class listsParser ( Parser ):

    grammarFileName = "lists.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"','", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"NUMBER", u"COMMA", u"LBRACKET", u"RBRACKET", 
                      u"WS" ]

    RULE_lst = 0
    RULE_seq = 1
    RULE_item = 2
    RULE_number = 3

    ruleNames =  [ u"lst", u"seq", u"item", u"number" ]

    EOF = Token.EOF
    NUMBER=1
    COMMA=2
    LBRACKET=3
    RBRACKET=4
    WS=5

    def __init__(self, input):
        super(listsParser, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LstContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(listsParser.LstContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._LBRACKET = None # Token

        def LBRACKET(self):
            return self.getToken(listsParser.LBRACKET, 0)

        def seq(self):
            return self.getTypedRuleContext(listsParser.SeqContext,0)


        def RBRACKET(self):
            return self.getToken(listsParser.RBRACKET, 0)

        def getRuleIndex(self):
            return listsParser.RULE_lst

        def enterRule(self, listener):
            if hasattr(listener, "enterLst"):
                listener.enterLst(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLst"):
                listener.exitLst(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLst"):
                return visitor.visitLst(self)
            else:
                return visitor.visitChildren(self)




    def lst(self):

        localctx = listsParser.LstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            localctx._LBRACKET = self.match(listsParser.LBRACKET)
            self.state = 9
            self.seq()
            self.state = 10
            self.match(listsParser.RBRACKET)
            print("another list %d:%d" % ((0 if localctx._LBRACKET is None else localctx._LBRACKET.line), (0 if localctx._LBRACKET is None else localctx._LBRACKET.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SeqContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(listsParser.SeqContext, self).__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(listsParser.ItemContext,0)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(listsParser.COMMA)
            else:
                return self.getToken(listsParser.COMMA, i)

        def seq(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(listsParser.SeqContext)
            else:
                return self.getTypedRuleContext(listsParser.SeqContext,i)


        def getRuleIndex(self):
            return listsParser.RULE_seq

        def enterRule(self, listener):
            if hasattr(listener, "enterSeq"):
                listener.enterSeq(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSeq"):
                listener.exitSeq(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSeq"):
                return visitor.visitSeq(self)
            else:
                return visitor.visitChildren(self)




    def seq(self):

        localctx = listsParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_seq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if _la==listsParser.NUMBER or _la==listsParser.LBRACKET:
                self.state = 13
                self.item()
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 14
                        self.match(listsParser.COMMA)
                        self.state = 15
                        self.seq() 
                    self.state = 20
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(listsParser.ItemContext, self).__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(listsParser.NumberContext,0)


        def lst(self):
            return self.getTypedRuleContext(listsParser.LstContext,0)


        def getRuleIndex(self):
            return listsParser.RULE_item

        def enterRule(self, listener):
            if hasattr(listener, "enterItem"):
                listener.enterItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItem"):
                listener.exitItem(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitItem"):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = listsParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_item)
        try:
            self.state = 25
            token = self._input.LA(1)
            if token in [listsParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.number()

            elif token in [listsParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.lst()

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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(listsParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(listsParser.NUMBER, 0)

        def getRuleIndex(self):
            return listsParser.RULE_number

        def enterRule(self, listener):
            if hasattr(listener, "enterNumber"):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumber"):
                listener.exitNumber(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNumber"):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = listsParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(listsParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





