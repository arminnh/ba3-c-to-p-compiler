# Generated from lists.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\7\37\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2")
        buf.write(u"\6\2\17\n\2\r\2\16\2\20\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6")
        buf.write(u"\6\32\n\6\r\6\16\6\33\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13")
        buf.write(u"\7\3\2\4\3\2\62;\5\2\13\f\17\17\"\" \2\3\3\2\2\2\2\5")
        buf.write(u"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\16\3")
        buf.write(u"\2\2\2\5\22\3\2\2\2\7\24\3\2\2\2\t\26\3\2\2\2\13\31\3")
        buf.write(u"\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16")
        buf.write(u"\3\2\2\2\20\21\3\2\2\2\21\4\3\2\2\2\22\23\7.\2\2\23\6")
        buf.write(u"\3\2\2\2\24\25\7*\2\2\25\b\3\2\2\2\26\27\7+\2\2\27\n")
        buf.write(u"\3\2\2\2\30\32\t\3\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33")
        buf.write(u"\31\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\b\6\2\2")
        buf.write(u"\36\f\3\2\2\2\5\2\20\33\3\b\2\2")
        return buf.getvalue()


class listsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    NUMBER = 1
    COMMA = 2
    LBRACKET = 3
    RBRACKET = 4
    WS = 5

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"NUMBER", u"COMMA", u"LBRACKET", u"RBRACKET", u"WS" ]

    ruleNames = [ u"NUMBER", u"COMMA", u"LBRACKET", u"RBRACKET", u"WS" ]

    grammarFileName = u"lists.g4"

    def __init__(self, input=None):
        super(listsLexer, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


