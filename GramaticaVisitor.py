# Generated from Gramatica.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#apagar.
    def visitApagar(self, ctx:GramaticaParser.ApagarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#prog.
    def visitProg(self, ctx:GramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#runStatemen.
    def visitRunStatemen(self, ctx:GramaticaParser.RunStatemenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#runItStatemen.
    def visitRunItStatemen(self, ctx:GramaticaParser.RunItStatemenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#runItPStatemen.
    def visitRunItPStatemen(self, ctx:GramaticaParser.RunItPStatemenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#statement.
    def visitStatement(self, ctx:GramaticaParser.StatementContext):
        return self.visitChildren(ctx)



del GramaticaParser