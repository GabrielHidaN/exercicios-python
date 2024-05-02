class Cachorro:
  def __init__(self , nome , cor , acordado = True):
    print('iniciando classe...')
    self.nome = nome
    self.cor = cor
    self.acordado = acordado

  def latir(self):
    print('auauauau')

  def __del__(self):
    print('removendo  instancia da classe')


def criar_cachorro():
  c = Cachorro('Amora' , 'branto e preto' , False)
  print(c.nome)

c = Cachorro('Zeca' , ' marron')
c.latir()
del c

criar_cachorro()
