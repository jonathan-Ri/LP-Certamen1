// Generated from /home/reo/ANTLR/Control1/Gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class GramaticaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, ID=2, INT=3, WS=4, ENCENDER=5, APAGAR=6, MOVER=7, DIBUJAR=8, PUNTO=9, 
		ROTAR=10, REPETIR=11, SUMA=12, RESTA=13, MULTIPLICACION=14, DIVISION=15, 
		LPAREN=16, RPAREN=17, AVANZAR=18, ATRAS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "ID", "INT", "WS", "ENCENDER", "APAGAR", "MOVER", "DIBUJAR", 
			"PUNTO", "ROTAR", "REPETIR", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", 
			"LPAREN", "RPAREN", "AVANZAR", "ATRAS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':'", null, null, null, "'encender'", "'apagar'", "'mover'", "'dibujar'", 
			null, "'rotar'", "'repetir'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
			"'avanzar'", "'atras'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "ID", "INT", "WS", "ENCENDER", "APAGAR", "MOVER", "DIBUJAR", 
			"PUNTO", "ROTAR", "REPETIR", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", 
			"LPAREN", "RPAREN", "AVANZAR", "ATRAS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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


	public GramaticaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0013\u0086\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0001\u0004\u0001"+
		"+\b\u0001\u000b\u0001\f\u0001,\u0001\u0002\u0004\u00020\b\u0002\u000b"+
		"\u0002\f\u00021\u0001\u0003\u0004\u00035\b\u0003\u000b\u0003\f\u00036"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0000\u0000\u0013\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\u0001\u0000\u0003\u0002\u0000"+
		"AZaz\u0001\u000009\u0003\u0000\t\n\r\r  \u0088\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0001\'\u0001"+
		"\u0000\u0000\u0000\u0003*\u0001\u0000\u0000\u0000\u0005/\u0001\u0000\u0000"+
		"\u0000\u00074\u0001\u0000\u0000\u0000\t:\u0001\u0000\u0000\u0000\u000b"+
		"C\u0001\u0000\u0000\u0000\rJ\u0001\u0000\u0000\u0000\u000fP\u0001\u0000"+
		"\u0000\u0000\u0011X\u0001\u0000\u0000\u0000\u0013^\u0001\u0000\u0000\u0000"+
		"\u0015d\u0001\u0000\u0000\u0000\u0017l\u0001\u0000\u0000\u0000\u0019n"+
		"\u0001\u0000\u0000\u0000\u001bp\u0001\u0000\u0000\u0000\u001dr\u0001\u0000"+
		"\u0000\u0000\u001ft\u0001\u0000\u0000\u0000!v\u0001\u0000\u0000\u0000"+
		"#x\u0001\u0000\u0000\u0000%\u0080\u0001\u0000\u0000\u0000\'(\u0005:\u0000"+
		"\u0000(\u0002\u0001\u0000\u0000\u0000)+\u0007\u0000\u0000\u0000*)\u0001"+
		"\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-\u0004\u0001\u0000\u0000\u0000.0\u0007\u0001"+
		"\u0000\u0000/.\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u00001/\u0001"+
		"\u0000\u0000\u000012\u0001\u0000\u0000\u00002\u0006\u0001\u0000\u0000"+
		"\u000035\u0007\u0002\u0000\u000043\u0001\u0000\u0000\u000056\u0001\u0000"+
		"\u0000\u000064\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000078\u0001"+
		"\u0000\u0000\u000089\u0006\u0003\u0000\u00009\b\u0001\u0000\u0000\u0000"+
		":;\u0005e\u0000\u0000;<\u0005n\u0000\u0000<=\u0005c\u0000\u0000=>\u0005"+
		"e\u0000\u0000>?\u0005n\u0000\u0000?@\u0005d\u0000\u0000@A\u0005e\u0000"+
		"\u0000AB\u0005r\u0000\u0000B\n\u0001\u0000\u0000\u0000CD\u0005a\u0000"+
		"\u0000DE\u0005p\u0000\u0000EF\u0005a\u0000\u0000FG\u0005g\u0000\u0000"+
		"GH\u0005a\u0000\u0000HI\u0005r\u0000\u0000I\f\u0001\u0000\u0000\u0000"+
		"JK\u0005m\u0000\u0000KL\u0005o\u0000\u0000LM\u0005v\u0000\u0000MN\u0005"+
		"e\u0000\u0000NO\u0005r\u0000\u0000O\u000e\u0001\u0000\u0000\u0000PQ\u0005"+
		"d\u0000\u0000QR\u0005i\u0000\u0000RS\u0005b\u0000\u0000ST\u0005u\u0000"+
		"\u0000TU\u0005j\u0000\u0000UV\u0005a\u0000\u0000VW\u0005r\u0000\u0000"+
		"W\u0010\u0001\u0000\u0000\u0000XY\u0005(\u0000\u0000YZ\u0003\u0005\u0002"+
		"\u0000Z[\u0005,\u0000\u0000[\\\u0003\u0005\u0002\u0000\\]\u0005)\u0000"+
		"\u0000]\u0012\u0001\u0000\u0000\u0000^_\u0005r\u0000\u0000_`\u0005o\u0000"+
		"\u0000`a\u0005t\u0000\u0000ab\u0005a\u0000\u0000bc\u0005r\u0000\u0000"+
		"c\u0014\u0001\u0000\u0000\u0000de\u0005r\u0000\u0000ef\u0005e\u0000\u0000"+
		"fg\u0005p\u0000\u0000gh\u0005e\u0000\u0000hi\u0005t\u0000\u0000ij\u0005"+
		"i\u0000\u0000jk\u0005r\u0000\u0000k\u0016\u0001\u0000\u0000\u0000lm\u0005"+
		"+\u0000\u0000m\u0018\u0001\u0000\u0000\u0000no\u0005-\u0000\u0000o\u001a"+
		"\u0001\u0000\u0000\u0000pq\u0005*\u0000\u0000q\u001c\u0001\u0000\u0000"+
		"\u0000rs\u0005/\u0000\u0000s\u001e\u0001\u0000\u0000\u0000tu\u0005(\u0000"+
		"\u0000u \u0001\u0000\u0000\u0000vw\u0005)\u0000\u0000w\"\u0001\u0000\u0000"+
		"\u0000xy\u0005a\u0000\u0000yz\u0005v\u0000\u0000z{\u0005a\u0000\u0000"+
		"{|\u0005n\u0000\u0000|}\u0005z\u0000\u0000}~\u0005a\u0000\u0000~\u007f"+
		"\u0005r\u0000\u0000\u007f$\u0001\u0000\u0000\u0000\u0080\u0081\u0005a"+
		"\u0000\u0000\u0081\u0082\u0005t\u0000\u0000\u0082\u0083\u0005r\u0000\u0000"+
		"\u0083\u0084\u0005a\u0000\u0000\u0084\u0085\u0005s\u0000\u0000\u0085&"+
		"\u0001\u0000\u0000\u0000\u0004\u0000,16\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}