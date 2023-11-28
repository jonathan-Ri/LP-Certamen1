from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser
import numpy as np
import random
import matplotlib.pyplot as plt


class MyVisitor(GramaticaVisitor):

  def __init__(self):
    self.capas = 1
    self.estados = {
        0: 'Susceptibles',
        1: 'Expuestos',
        2: 'Infectados',
        3: 'Recuperados',
        4: 'Recuperados',
        5: 'Recuperados'
    }
    self.espacios = 3
    self.iteraciones = 1
    self.paciente0 = [1, 1, 1]

  def visitRunStatemen(self, ctx):
    espacio = int(ctx.INT(0).getText())
    capas = int(ctx.INT(1).getText())
    #creacion de matriz
    matriz = []
    for p in range(0, capas):
      capa = matriz_np = np.array([[0] * espacio] * espacio)
      matriz.append(capa)
    self.paciente0 = [
        random.randint(0, espacio - 1),
        random.randint(0, espacio - 1),
        random.randint(0, capas - 1)
    ]
    matriz[self.paciente0[0]][self.paciente0[1]][self.paciente0[2]] = 2
    print(self.paciente0)

    print("matriz antes:\n", matriz)
    matriz = self.infestar(espacio, capas, matriz)
    print("Matriz luego", matriz)
    self.dibujarMatriz(matriz, capas)
    return True

  def visitRunItStatemen(self, ctx):
    espacio = int(ctx.INT(0).getText())
    capas = int(ctx.INT(1).getText())
    iteraciones = int(ctx.INT(2).getText())
    matriz = []
    for p in range(0, capas):
      capa = matriz_np = np.array([[0] * espacio] * espacio)
      matriz.append(capa)
    self.paciente0 = [
        random.randint(0, espacio - 1),
        random.randint(0, espacio - 1),
        random.randint(0, capas - 1)
    ]
    matriz[self.paciente0[0]][self.paciente0[1]][self.paciente0[2]] = 2
    print(self.paciente0)
    print("matriz antes:\n", matriz)

    for q in range(0, iteraciones):
      matriz = self.infestar(espacio, capas, matriz)
    self.dibujarMatriz(matriz, capas)
    print("Matriz luego de [", iteraciones, "] iteraciones\n", matriz)

    return True

  def visitRunItPStatemen(self, ctx):
    espacio = int(ctx.INT(0).getText())
    capas = int(ctx.INT(1).getText())
    iteraciones = int(ctx.INT(2).getText())
    pacienteO = [
        int(ctx.INT(3).getText()),
        int(ctx.INT(4).getText()),
        int(ctx.INT(5).getText())
    ]
    print(pacienteO)
    self.paciente0 = pacienteO
    matriz = []
    for p in range(0, capas):
      capa = matriz_np = np.array([[0] * espacio] * espacio)
      matriz.append(capa)
    self.paciente0 = [
        random.randint(0, espacio - 1),
        random.randint(0, espacio - 1),
        random.randint(0, capas - 1)
    ]
    matriz[self.paciente0[0]][self.paciente0[1]][self.paciente0[2]] = 2
    print(self.paciente0)
    print("matriz antes:\n", matriz)

    for q in range(0, iteraciones):
      matriz = self.infestar(espacio, capas, matriz)
    self.dibujarMatriz(matriz, capas)
    print("Matriz luego de [", iteraciones, "] iteraciones\n", matriz)

    return True

  def vecinos(self, infestado, espacio, capas):
    vecinos = []
    if infestado[1] > 0:
      vecinos.append([infestado[0], infestado[1] - 1, infestado[2]])
    if infestado[1] < (espacio - 1):
      vecinos.append([infestado[0], infestado[1] + 1, infestado[2]])
    if infestado[0] > 0:
      vecinos.append([infestado[0] - 1, infestado[1], infestado[2]])
    if infestado[0] < (espacio - 1):
      vecinos.append([infestado[0] + 1, infestado[1], infestado[2]])
    if infestado[2] > 0:
      vecinos.append([infestado[0], infestado[1], infestado[2] - 1])
    if infestado[2] < (capas - 1):
      vecinos.append([infestado[0], infestado[1], infestado[2] + 1])
    return vecinos

  def infestar(self, espacio, capas, matriz):
    expuestosNuevos = []
    for i in range(0, espacio):
      for j in range(0, espacio):
        for z in range(0, capas):
          if matriz[i][j][z] == 2:
            infestado = [i, j, z]
            vecinos = self.vecinos(infestado, espacio, capas)
            for y in range(0, len(vecinos)):
              if matriz[vecinos[y][0]][vecinos[y][1]][vecinos[y][2]] == 0:
                matriz[vecinos[y][0]][vecinos[y][1]][vecinos[y][2]] = 1
                expuestosNuevos.append(
                    [vecinos[y][0], vecinos[y][1], vecinos[y][2]])
    for x in range(0, espacio):
      for y in range(0, espacio):
        for k in range(0, capas):
          if ([x, y, k] not in expuestosNuevos) and (matriz[x][y][k] != 0):
            matriz[x][y][k] = matriz[x][y][k] + 1
    return matriz

  def dibujarMatriz(self, matriz, capas):
  # Define un nuevo colormap personalizado
  custom_cmap = plt.cm.colors.ListedColormap(['white', 'green', 'yellow', '#FFDAB9', '#FFA500', '#8B4513'])
  num_matrices = len(matriz)
  if (num_matrices == 1):
      plt.imshow(matriz[0], cmap=custom_cmap, interpolation='nearest')
      plt.colorbar()
      plt.show()
  elif (num_matrices == 2):
      fig, axs = plt.subplots(1, 2, figsize=(15, 5))
      axs[0].imshow(matriz[0], cmap=custom_cmap, interpolation='nearest')
      axs[0].set_title('Matriz 1')
      axs[1].imshow(matriz[1], cmap=custom_cmap, interpolation='nearest')
      axs[1].set_title('Matriz 2')
      plt.show()
  else:
      num_filas = int(np.ceil(np.sqrt(num_matrices)))
      num_columnas = int(np.ceil(num_matrices / num_filas))
      fig, axs = plt.subplots(num_filas, num_columnas, figsize=(4, 4))
      for i in range(0, num_matrices):
          fila = i // num_columnas
          columna = i % num_columnas
          axs[fila, columna].imshow(matriz[i], cmap=custom_cmap, interpolation='nearest')
          axs[fila, columna].set_title(f'Matriz {i + 1}')
      plt.tight_layout()
      plt.show()
  return True

  def visitApagar(self, ctx):
    return False
