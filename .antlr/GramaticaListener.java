// Generated from /home/reo/ANTLR/Control1/Gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GramaticaParser}.
 */
public interface GramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(GramaticaParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(GramaticaParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(GramaticaParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(GramaticaParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#encenderStatement}.
	 * @param ctx the parse tree
	 */
	void enterEncenderStatement(GramaticaParser.EncenderStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#encenderStatement}.
	 * @param ctx the parse tree
	 */
	void exitEncenderStatement(GramaticaParser.EncenderStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#apagarStatement}.
	 * @param ctx the parse tree
	 */
	void enterApagarStatement(GramaticaParser.ApagarStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#apagarStatement}.
	 * @param ctx the parse tree
	 */
	void exitApagarStatement(GramaticaParser.ApagarStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#moverStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoverStatement(GramaticaParser.MoverStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#moverStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoverStatement(GramaticaParser.MoverStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#dibujarStatement}.
	 * @param ctx the parse tree
	 */
	void enterDibujarStatement(GramaticaParser.DibujarStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#dibujarStatement}.
	 * @param ctx the parse tree
	 */
	void exitDibujarStatement(GramaticaParser.DibujarStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#rotarStatement}.
	 * @param ctx the parse tree
	 */
	void enterRotarStatement(GramaticaParser.RotarStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#rotarStatement}.
	 * @param ctx the parse tree
	 */
	void exitRotarStatement(GramaticaParser.RotarStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#repetirStatement}.
	 * @param ctx the parse tree
	 */
	void enterRepetirStatement(GramaticaParser.RepetirStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#repetirStatement}.
	 * @param ctx the parse tree
	 */
	void exitRepetirStatement(GramaticaParser.RepetirStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(GramaticaParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(GramaticaParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(GramaticaParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(GramaticaParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link GramaticaParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(GramaticaParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GramaticaParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(GramaticaParser.FactorContext ctx);
}