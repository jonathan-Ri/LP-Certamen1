import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from MyVisitor import MyVisitor

from antlr4.tree.Trees import Trees
#asdakmdasdkdasnkasdknd

if __name__ == '__main__':
  while (True):
    if len(sys.argv) > 1:
      input_stream = FileStream(sys.argv[1])
    else:
      input_stream = InputStream(sys.stdin.readline())

    lexer = GramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GramaticaParser(token_stream)
    tree = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)
    print(Trees.toStringTree(tree, None, parser))
