// Generated from SmallC.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SmallCParser}.
 */
public interface SmallCListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SmallCParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(SmallCParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(SmallCParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#header}.
	 * @param ctx the parse tree
	 */
	void enterHeader(SmallCParser.HeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#header}.
	 * @param ctx the parse tree
	 */
	void exitHeader(SmallCParser.HeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#include}.
	 * @param ctx the parse tree
	 */
	void enterInclude(SmallCParser.IncludeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#include}.
	 * @param ctx the parse tree
	 */
	void exitInclude(SmallCParser.IncludeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#stdInclude}.
	 * @param ctx the parse tree
	 */
	void enterStdInclude(SmallCParser.StdIncludeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#stdInclude}.
	 * @param ctx the parse tree
	 */
	void exitStdInclude(SmallCParser.StdIncludeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#customInclude}.
	 * @param ctx the parse tree
	 */
	void enterCustomInclude(SmallCParser.CustomIncludeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#customInclude}.
	 * @param ctx the parse tree
	 */
	void exitCustomInclude(SmallCParser.CustomIncludeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#mainFunction}.
	 * @param ctx the parse tree
	 */
	void enterMainFunction(SmallCParser.MainFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#mainFunction}.
	 * @param ctx the parse tree
	 */
	void exitMainFunction(SmallCParser.MainFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#typeDecl}.
	 * @param ctx the parse tree
	 */
	void enterTypeDecl(SmallCParser.TypeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#typeDecl}.
	 * @param ctx the parse tree
	 */
	void exitTypeDecl(SmallCParser.TypeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void enterFunctionBody(SmallCParser.FunctionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void exitFunctionBody(SmallCParser.FunctionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmallCParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(SmallCParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmallCParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(SmallCParser.NumberContext ctx);
}