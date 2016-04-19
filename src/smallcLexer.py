# Generated from smallc.g4 by ANTLR 4.5.2
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3&\n\3\r\3\16\3")
        buf.write("\'\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5\61\n\5\r\5\16\5\62")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\6\rD\n\r\r\r\16\rE\3\r\3\r\2\2\16\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\3")
        buf.write("\2c|\3\2\62;\5\2\13\f\17\17\"\"K\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5%\3\2\2\2\7)\3\2\2")
        buf.write("\2\t\60\3\2\2\2\13\64\3\2\2\2\r\66\3\2\2\2\178\3\2\2\2")
        buf.write("\21:\3\2\2\2\23<\3\2\2\2\25>\3\2\2\2\27@\3\2\2\2\31C\3")
        buf.write("\2\2\2\33\34\7%\2\2\34\35\7k\2\2\35\36\7p\2\2\36\37\7")
        buf.write("e\2\2\37 \7n\2\2 !\7w\2\2!\"\7f\2\2\"#\7g\2\2#\4\3\2\2")
        buf.write("\2$&\t\2\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2")
        buf.write("\2(\6\3\2\2\2)*\7*\2\2*+\7\60\2\2+,\7,\2\2,-\7A\2\2-.")
        buf.write("\7+\2\2.\b\3\2\2\2/\61\t\3\2\2\60/\3\2\2\2\61\62\3\2\2")
        buf.write("\2\62\60\3\2\2\2\62\63\3\2\2\2\63\n\3\2\2\2\64\65\7.\2")
        buf.write("\2\65\f\3\2\2\2\66\67\7*\2\2\67\16\3\2\2\289\7+\2\29\20")
        buf.write("\3\2\2\2:;\7>\2\2;\22\3\2\2\2<=\7@\2\2=\24\3\2\2\2>?\7")
        buf.write("}\2\2?\26\3\2\2\2@A\7\177\2\2A\30\3\2\2\2BD\t\4\2\2CB")
        buf.write("\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\r")
        buf.write("\2\2H\32\3\2\2\2\6\2\'\62E\3\b\2\2")
        return buf.getvalue()


class smallcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    ID = 2
    STRING = 3
    NUMBER = 4
    COMMA = 5
    LBRA = 6
    RBRA = 7
    LABRA = 8
    RABRA = 9
    LCBRA = 10
    RCBRA = 11
    WS = 12

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#include'", "'(.*?)'", "','", "'('", "')'", "'<'", "'>'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "NUMBER", "COMMA", "LBRA", "RBRA", "LABRA", 
            "RABRA", "LCBRA", "RCBRA", "WS" ]

    ruleNames = [ "T__0", "ID", "STRING", "NUMBER", "COMMA", "LBRA", "RBRA", 
                  "LABRA", "RABRA", "LCBRA", "RCBRA", "WS" ]

    grammarFileName = "smallc.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


