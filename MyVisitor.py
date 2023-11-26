from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser


class MyVisitor(GramaticaVisitor):

  def __init__(self):
    self.capas = 1
    self.estados = ['Susceptibles', 'Expuestos', 'Infectados', 'Recuperados']
    self.espacios = 3
    self.iteraciones = 1
    self.paciente0 = [1, 1, 1]

  def visitRUN(self, ctx):
    print('RUN')
    print(ctx.PUNTO().getText()[1:-1].split(','))

  def visitRUN2(self, ctx):
    print('RUN 2')
    print(ctx)

  def visitRUN3(self, ctx):
    print('RUN 3')
    print(ctx)
