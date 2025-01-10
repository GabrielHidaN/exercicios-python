import math

class Calculadora:
  def __init__(self , n1 , n2 ):
    self.n1 = n1
    self.n2 = n2

  def somar(self):
    print( self.n1 + self.n2)

  def media(self):
    print((self.n1 + self.n2) / 2)

soma = Calculadora(10 , 20)
soma.somar()
media = Calculadora(10 , 2)
media.media()
