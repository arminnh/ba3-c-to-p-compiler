// Generated from SmallC.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SmallCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, PTR=5, COMMA=6, LBRA=7, RBRA=8, LABRA=9, 
		RABRA=10, LCBRA=11, RCBRA=12, QUOTE=13, CHAR=14, FLOAT=15, INT=16, CFUN=17, 
		RETURN=18, NUMBER=19, STRING1=20, STRING2=21, WS=22;
	public static final int
		RULE_program = 0, RULE_header = 1, RULE_include = 2, RULE_stdInclude = 3, 
		RULE_customInclude = 4, RULE_mainFunction = 5, RULE_typeDecl = 6, RULE_functionBody = 7, 
		RULE_number = 8;
	public static final String[] ruleNames = {
		"program", "header", "include", "stdInclude", "customInclude", "mainFunction", 
		"typeDecl", "functionBody", "number"
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

	@Override
	public String getGrammarFileName() { return "SmallC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SmallCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public HeaderContext header() {
			return getRuleContext(HeaderContext.class,0);
		}
		public MainFunctionContext mainFunction() {
			return getRuleContext(MainFunctionContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			header();
			setState(19);
			mainFunction();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class HeaderContext extends ParserRuleContext {
		public List<IncludeContext> include() {
			return getRuleContexts(IncludeContext.class);
		}
		public IncludeContext include(int i) {
			return getRuleContext(IncludeContext.class,i);
		}
		public HeaderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_header; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterHeader(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitHeader(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitHeader(this);
			else return visitor.visitChildren(this);
		}
	}

	public final HeaderContext header() throws RecognitionException {
		HeaderContext _localctx = new HeaderContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_header);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(21);
				match(T__0);
				setState(22);
				include();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IncludeContext extends ParserRuleContext {
		public TerminalNode LABRA() { return getToken(SmallCParser.LABRA, 0); }
		public TerminalNode STRING1() { return getToken(SmallCParser.STRING1, 0); }
		public TerminalNode RABRA() { return getToken(SmallCParser.RABRA, 0); }
		public TerminalNode STRING2() { return getToken(SmallCParser.STRING2, 0); }
		public IncludeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterInclude(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitInclude(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitInclude(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IncludeContext include() throws RecognitionException {
		IncludeContext _localctx = new IncludeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_include);
		try {
			setState(32);
			switch (_input.LA(1)) {
			case LABRA:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				match(LABRA);
				setState(29);
				match(STRING1);
				setState(30);
				match(RABRA);
				}
				break;
			case STRING2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				match(STRING2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StdIncludeContext extends ParserRuleContext {
		public StdIncludeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stdInclude; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterStdInclude(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitStdInclude(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitStdInclude(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StdIncludeContext stdInclude() throws RecognitionException {
		StdIncludeContext _localctx = new StdIncludeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_stdInclude);
		try {
			enterOuterAlt(_localctx, 1);
			{
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CustomIncludeContext extends ParserRuleContext {
		public CustomIncludeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_customInclude; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterCustomInclude(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitCustomInclude(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitCustomInclude(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CustomIncludeContext customInclude() throws RecognitionException {
		CustomIncludeContext _localctx = new CustomIncludeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_customInclude);
		try {
			enterOuterAlt(_localctx, 1);
			{
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainFunctionContext extends ParserRuleContext {
		public TypeDeclContext typeDecl() {
			return getRuleContext(TypeDeclContext.class,0);
		}
		public TerminalNode LBRA() { return getToken(SmallCParser.LBRA, 0); }
		public TerminalNode RBRA() { return getToken(SmallCParser.RBRA, 0); }
		public TerminalNode LCBRA() { return getToken(SmallCParser.LCBRA, 0); }
		public TerminalNode RCBRA() { return getToken(SmallCParser.RCBRA, 0); }
		public List<FunctionBodyContext> functionBody() {
			return getRuleContexts(FunctionBodyContext.class);
		}
		public FunctionBodyContext functionBody(int i) {
			return getRuleContext(FunctionBodyContext.class,i);
		}
		public MainFunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainFunction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterMainFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitMainFunction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitMainFunction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MainFunctionContext mainFunction() throws RecognitionException {
		MainFunctionContext _localctx = new MainFunctionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_mainFunction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			typeDecl();
			setState(39);
			match(T__1);
			setState(40);
			match(LBRA);
			setState(41);
			match(T__2);
			setState(42);
			match(RBRA);
			setState(43);
			match(LCBRA);
			setState(45); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(44);
				functionBody();
				}
				}
				setState(47); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CFUN || _la==RETURN );
			setState(49);
			match(RCBRA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeDeclContext extends ParserRuleContext {
		public TerminalNode CHAR() { return getToken(SmallCParser.CHAR, 0); }
		public TerminalNode FLOAT() { return getToken(SmallCParser.FLOAT, 0); }
		public TerminalNode INT() { return getToken(SmallCParser.INT, 0); }
		public TypeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterTypeDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitTypeDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitTypeDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeDeclContext typeDecl() throws RecognitionException {
		TypeDeclContext _localctx = new TypeDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_typeDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR) | (1L << FLOAT) | (1L << INT))) != 0)) ) {
			_errHandler.recoverInline(this);
			} else {
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionBodyContext extends ParserRuleContext {
		public TerminalNode CFUN() { return getToken(SmallCParser.CFUN, 0); }
		public TerminalNode LBRA() { return getToken(SmallCParser.LBRA, 0); }
		public TerminalNode STRING2() { return getToken(SmallCParser.STRING2, 0); }
		public TerminalNode RBRA() { return getToken(SmallCParser.RBRA, 0); }
		public TerminalNode RETURN() { return getToken(SmallCParser.RETURN, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public FunctionBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterFunctionBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitFunctionBody(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitFunctionBody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionBodyContext functionBody() throws RecognitionException {
		FunctionBodyContext _localctx = new FunctionBodyContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_functionBody);
		try {
			setState(62);
			switch (_input.LA(1)) {
			case CFUN:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				match(CFUN);
				setState(54);
				match(LBRA);
				setState(55);
				match(STRING2);
				setState(56);
				match(RBRA);
				setState(57);
				match(T__3);
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 2);
				{
				setState(58);
				match(RETURN);
				setState(59);
				number();
				setState(60);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(SmallCParser.NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).enterNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmallCListener ) ((SmallCListener)listener).exitNumber(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SmallCVisitor ) return ((SmallCVisitor<? extends T>)visitor).visitNumber(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\30E\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2"+
		"\3\3\3\3\7\3\32\n\3\f\3\16\3\35\13\3\3\4\3\4\3\4\3\4\5\4#\n\4\3\5\3\5"+
		"\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7\60\n\7\r\7\16\7\61\3\7\3\7\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tA\n\t\3\n\3\n\3\n\2\2\13"+
		"\2\4\6\b\n\f\16\20\22\2\3\3\2\20\22?\2\24\3\2\2\2\4\33\3\2\2\2\6\"\3\2"+
		"\2\2\b$\3\2\2\2\n&\3\2\2\2\f(\3\2\2\2\16\65\3\2\2\2\20@\3\2\2\2\22B\3"+
		"\2\2\2\24\25\5\4\3\2\25\26\5\f\7\2\26\3\3\2\2\2\27\30\7\3\2\2\30\32\5"+
		"\6\4\2\31\27\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3"+
		"\2\2\2\35\33\3\2\2\2\36\37\7\13\2\2\37 \7\26\2\2 #\7\f\2\2!#\7\27\2\2"+
		"\"\36\3\2\2\2\"!\3\2\2\2#\7\3\2\2\2$%\3\2\2\2%\t\3\2\2\2&\'\3\2\2\2\'"+
		"\13\3\2\2\2()\5\16\b\2)*\7\4\2\2*+\7\t\2\2+,\7\5\2\2,-\7\n\2\2-/\7\r\2"+
		"\2.\60\5\20\t\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63"+
		"\3\2\2\2\63\64\7\16\2\2\64\r\3\2\2\2\65\66\t\2\2\2\66\17\3\2\2\2\678\7"+
		"\23\2\289\7\t\2\29:\7\27\2\2:;\7\n\2\2;A\7\6\2\2<=\7\24\2\2=>\5\22\n\2"+
		">?\7\6\2\2?A\3\2\2\2@\67\3\2\2\2@<\3\2\2\2A\21\3\2\2\2BC\7\25\2\2C\23"+
		"\3\2\2\2\6\33\"\61@";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}