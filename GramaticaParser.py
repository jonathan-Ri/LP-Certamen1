# Generated from Gramatica.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,4,1,16,8,1,11,1,12,1,17,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,52,8,5,1,5,0,0,6,0,2,4,6,8,10,
        0,0,51,0,12,1,0,0,0,2,15,1,0,0,0,4,19,1,0,0,0,6,25,1,0,0,0,8,33,
        1,0,0,0,10,51,1,0,0,0,12,13,5,1,0,0,13,1,1,0,0,0,14,16,3,10,5,0,
        15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,
        0,0,19,20,5,2,0,0,20,21,5,7,0,0,21,22,5,3,0,0,22,23,5,7,0,0,23,24,
        5,4,0,0,24,5,1,0,0,0,25,26,5,2,0,0,26,27,5,7,0,0,27,28,5,3,0,0,28,
        29,5,7,0,0,29,30,5,3,0,0,30,31,5,7,0,0,31,32,5,4,0,0,32,7,1,0,0,
        0,33,34,5,2,0,0,34,35,5,7,0,0,35,36,5,3,0,0,36,37,5,7,0,0,37,38,
        5,3,0,0,38,39,5,7,0,0,39,40,5,5,0,0,40,41,5,7,0,0,41,42,5,3,0,0,
        42,43,5,7,0,0,43,44,5,3,0,0,44,45,5,7,0,0,45,46,5,4,0,0,46,9,1,0,
        0,0,47,52,3,4,2,0,48,52,3,6,3,0,49,52,3,8,4,0,50,52,3,0,0,0,51,47,
        1,0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,11,1,0,0,0,
        2,17,51
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'apagar'", "'run('", "','", "')'", "',('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "NEXLINE", 
                      "WS", "ESPACIO", "CAPAS", "ITERACIONES", "PACIENTE0" ]

    RULE_apagar = 0
    RULE_prog = 1
    RULE_runStatemen = 2
    RULE_runItStatemen = 3
    RULE_runItPStatemen = 4
    RULE_statement = 5

    ruleNames =  [ "apagar", "prog", "runStatemen", "runItStatemen", "runItPStatemen", 
                   "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    INT=7
    NEXLINE=8
    WS=9
    ESPACIO=10
    CAPAS=11
    ITERACIONES=12
    PACIENTE0=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ApagarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_apagar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApagar" ):
                return visitor.visitApagar(self)
            else:
                return visitor.visitChildren(self)




    def apagar(self):

        localctx = GramaticaParser.ApagarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_apagar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(GramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = GramaticaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunStatemenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_runStatemen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRunStatemen" ):
                return visitor.visitRunStatemen(self)
            else:
                return visitor.visitChildren(self)




    def runStatemen(self):

        localctx = GramaticaParser.RunStatemenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_runStatemen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(GramaticaParser.T__1)
            self.state = 20
            self.match(GramaticaParser.INT)
            self.state = 21
            self.match(GramaticaParser.T__2)
            self.state = 22
            self.match(GramaticaParser.INT)
            self.state = 23
            self.match(GramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunItStatemenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_runItStatemen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRunItStatemen" ):
                return visitor.visitRunItStatemen(self)
            else:
                return visitor.visitChildren(self)




    def runItStatemen(self):

        localctx = GramaticaParser.RunItStatemenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_runItStatemen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(GramaticaParser.T__1)
            self.state = 26
            self.match(GramaticaParser.INT)
            self.state = 27
            self.match(GramaticaParser.T__2)
            self.state = 28
            self.match(GramaticaParser.INT)
            self.state = 29
            self.match(GramaticaParser.T__2)
            self.state = 30
            self.match(GramaticaParser.INT)
            self.state = 31
            self.match(GramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunItPStatemenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_runItPStatemen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRunItPStatemen" ):
                return visitor.visitRunItPStatemen(self)
            else:
                return visitor.visitChildren(self)




    def runItPStatemen(self):

        localctx = GramaticaParser.RunItPStatemenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_runItPStatemen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(GramaticaParser.T__1)
            self.state = 34
            self.match(GramaticaParser.INT)
            self.state = 35
            self.match(GramaticaParser.T__2)
            self.state = 36
            self.match(GramaticaParser.INT)
            self.state = 37
            self.match(GramaticaParser.T__2)
            self.state = 38
            self.match(GramaticaParser.INT)
            self.state = 39
            self.match(GramaticaParser.T__4)
            self.state = 40
            self.match(GramaticaParser.INT)
            self.state = 41
            self.match(GramaticaParser.T__2)
            self.state = 42
            self.match(GramaticaParser.INT)
            self.state = 43
            self.match(GramaticaParser.T__2)
            self.state = 44
            self.match(GramaticaParser.INT)
            self.state = 45
            self.match(GramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def runStatemen(self):
            return self.getTypedRuleContext(GramaticaParser.RunStatemenContext,0)


        def runItStatemen(self):
            return self.getTypedRuleContext(GramaticaParser.RunItStatemenContext,0)


        def runItPStatemen(self):
            return self.getTypedRuleContext(GramaticaParser.RunItPStatemenContext,0)


        def apagar(self):
            return self.getTypedRuleContext(GramaticaParser.ApagarContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.runStatemen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.runItStatemen()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.runItPStatemen()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.apagar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





