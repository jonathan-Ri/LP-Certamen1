# Generated from Gramatica.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,4,5,40,8,5,11,5,12,5,41,1,
        6,4,6,45,8,6,11,6,12,6,46,1,7,3,7,50,8,7,1,7,1,7,1,8,4,8,55,8,8,
        11,8,12,8,56,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,1,0,3,2,0,65,90,97,122,1,0,48,57,2,0,9,9,32,32,63,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,26,1,0,0,0,5,31,
        1,0,0,0,7,33,1,0,0,0,9,35,1,0,0,0,11,39,1,0,0,0,13,44,1,0,0,0,15,
        49,1,0,0,0,17,54,1,0,0,0,19,20,5,97,0,0,20,21,5,112,0,0,21,22,5,
        97,0,0,22,23,5,103,0,0,23,24,5,97,0,0,24,25,5,114,0,0,25,2,1,0,0,
        0,26,27,5,114,0,0,27,28,5,117,0,0,28,29,5,110,0,0,29,30,5,40,0,0,
        30,4,1,0,0,0,31,32,5,44,0,0,32,6,1,0,0,0,33,34,5,41,0,0,34,8,1,0,
        0,0,35,36,5,44,0,0,36,37,5,40,0,0,37,10,1,0,0,0,38,40,7,0,0,0,39,
        38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,12,1,0,0,
        0,43,45,7,1,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,14,1,0,0,0,48,50,5,13,0,0,49,48,1,0,0,0,49,50,1,0,0,0,
        50,51,1,0,0,0,51,52,5,10,0,0,52,16,1,0,0,0,53,55,7,2,0,0,54,53,1,
        0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,
        59,6,8,0,0,59,18,1,0,0,0,5,0,41,46,49,56,1,6,0,0
    ]

class GramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    ID = 6
    INT = 7
    NEXLINE = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'apagar'", "'run('", "','", "')'", "',('" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "NEXLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "ID", "INT", "NEXLINE", 
                  "WS" ]

    grammarFileName = "Gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


