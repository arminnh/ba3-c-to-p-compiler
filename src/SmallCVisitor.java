// Generated from SmallC.g4 by ANTLR 4.5.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link SmallCParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface SmallCVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link SmallCParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(SmallCParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#header}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHeader(SmallCParser.HeaderContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#include}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInclude(SmallCParser.IncludeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#stdInclude}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStdInclude(SmallCParser.StdIncludeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#customInclude}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCustomInclude(SmallCParser.CustomIncludeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#mainFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMainFunction(SmallCParser.MainFunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#typeDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeDecl(SmallCParser.TypeDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#functionBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionBody(SmallCParser.FunctionBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link SmallCParser#number}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber(SmallCParser.NumberContext ctx);
}