class Animal:
  def __init__(self ,nome ,  cor , raca , genero):
    self.nome = nome
    self.cor = cor
    self.raca = raca
    self.genero =  genero

  def comer(self):
    print(f'{self.nome} Está comendo')
  def dormir(self):
    hora = 17
    if hora > 18:
       noite = True
    else:
       noite = False

    if noite is True:
      print(f'{self.nome} está dormindo')
    else:
       print(f'{self.nome} está Acordado')


class Mamifero(Animal):
    def __init__(self, nome, cor, raca, genero):
      super().__init__(nome, cor, raca, genero)

class Ave(Animal):
    pass

class Cachorro(Mamifero):
  pass

cachorro = Cachorro(nome= 'Zeca' , cor = 'Marron com branco', raca= 'shitzu' , genero= 'macho')

cachorro.comer()
cachorro.dormir()
