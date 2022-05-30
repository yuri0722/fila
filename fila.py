import numpy as np

class Fila:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.fim = -1
    self.inicio = 0
    self.qtd = 0
    self.valores = np.empty(self.capacidade,dtype=int)

  def vazia (self):
    if (self.qtd == 0):
      return True
    return False

  def cheia (self):
    if (self.qtd == self.capacidade):
      return True
    return False

  def imprimir(self):
    for i in range (self.inicio, (self.fim%self.capacidade) + 1,1):
      print(self.valores[i])

  def queue (self, valor):
    if (self.cheia() == True):
      print("Fila Cheia")
    else:
      self.fim = (self.fim + 1) % self.capacidade
      self.valores[self.fim] = valor
      self.qtd += 1

  def dequeue (self):
    if (self.vazia() == True):
      print("Fila Vazia")
    else:
      self.qtd -= 1
      self.inicio = (self.inicio + 1) % self.capacidade
      
    