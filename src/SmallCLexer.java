// Generated from SmallC.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SmallCLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.5.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, PTR=5, COMMA=6, LBRA=7, RBRA=8, LABRA=9, 
		RABRA=10, LCBRA=11, RCBRA=12, QUOTE=13, CHAR=14, FLOAT=15, INT=16, CFUN=17, 
		RETURN=18, NUMBER=19, STRING1=20, STRING2=21, WS=22;
	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "PTR", "COMMA", "LBRA", "RBRA", "LABRA", 
		"RABRA", "LCBRA", "RCBRA", "QUOTE", "CHAR", "FLOAT", "INT", "CFUN", "RETURN", 
		"NUMBER", "STRING1", "STRING2", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'#include'", "'main'", "'void'", "';'", "'*'", "','", "'('", "')'", 
		"'<'", "'>'", "'{'", "'}'", "'\"'", "'char'", "'float'", "'int'", null, 
		"'return'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, "PTR", "COMMA", "LBRA", "RBRA", "LABRA", 
		"RABRA", "LCBRA", "RCBRA", "QUOTE", "CHAR", "FLOAT", "INT", "CFUN", "RETURN", 
		"NUMBER", "STRING1", "STRING2", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SmallCLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SmallC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\30\u008f\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16"+
		"\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21"+
		"\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22"+
		"q\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\6\24{\n\24\r\24\16\24|"+
		"\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u0085\n\26\3\26\3\26\3\27\6\27\u008a"+
		"\n\27\r\27\16\27\u008b\3\27\3\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t"+
		"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27"+
		"-\30\3\2\6\3\2\62;\6\2\f\f\17\17$$^^\4\2$$^^\5\2\13\f\17\17\"\"\u0092"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2"+
		"\2\58\3\2\2\2\7=\3\2\2\2\tB\3\2\2\2\13D\3\2\2\2\rF\3\2\2\2\17H\3\2\2\2"+
		"\21J\3\2\2\2\23L\3\2\2\2\25N\3\2\2\2\27P\3\2\2\2\31R\3\2\2\2\33T\3\2\2"+
		"\2\35V\3\2\2\2\37[\3\2\2\2!a\3\2\2\2#p\3\2\2\2%r\3\2\2\2\'z\3\2\2\2)~"+
		"\3\2\2\2+\u0080\3\2\2\2-\u0089\3\2\2\2/\60\7%\2\2\60\61\7k\2\2\61\62\7"+
		"p\2\2\62\63\7e\2\2\63\64\7n\2\2\64\65\7w\2\2\65\66\7f\2\2\66\67\7g\2\2"+
		"\67\4\3\2\2\289\7o\2\29:\7c\2\2:;\7k\2\2;<\7p\2\2<\6\3\2\2\2=>\7x\2\2"+
		">?\7q\2\2?@\7k\2\2@A\7f\2\2A\b\3\2\2\2BC\7=\2\2C\n\3\2\2\2DE\7,\2\2E\f"+
		"\3\2\2\2FG\7.\2\2G\16\3\2\2\2HI\7*\2\2I\20\3\2\2\2JK\7+\2\2K\22\3\2\2"+
		"\2LM\7>\2\2M\24\3\2\2\2NO\7@\2\2O\26\3\2\2\2PQ\7}\2\2Q\30\3\2\2\2RS\7"+
		"\177\2\2S\32\3\2\2\2TU\7$\2\2U\34\3\2\2\2VW\7e\2\2WX\7j\2\2XY\7c\2\2Y"+
		"Z\7t\2\2Z\36\3\2\2\2[\\\7h\2\2\\]\7n\2\2]^\7q\2\2^_\7c\2\2_`\7v\2\2` "+
		"\3\2\2\2ab\7k\2\2bc\7p\2\2cd\7v\2\2d\"\3\2\2\2ef\7r\2\2fg\7t\2\2gh\7k"+
		"\2\2hi\7p\2\2ij\7v\2\2jq\7h\2\2kl\7u\2\2lm\7e\2\2mn\7c\2\2no\7p\2\2oq"+
		"\7h\2\2pe\3\2\2\2pk\3\2\2\2q$\3\2\2\2rs\7t\2\2st\7g\2\2tu\7v\2\2uv\7w"+
		"\2\2vw\7t\2\2wx\7p\2\2x&\3\2\2\2y{\t\2\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2"+
		"\2|}\3\2\2\2}(\3\2\2\2~\177\n\3\2\2\177*\3\2\2\2\u0080\u0084\7$\2\2\u0081"+
		"\u0082\7^\2\2\u0082\u0085\t\4\2\2\u0083\u0085\5)\25\2\u0084\u0081\3\2"+
		"\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\7$\2\2\u0087"+
		",\3\2\2\2\u0088\u008a\t\5\2\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2"+
		"\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e"+
		"\b\27\2\2\u008e.\3\2\2\2\7\2p|\u0084\u008b\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}