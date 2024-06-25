#Desafio do Heroi

'''
POO

Cada heroi deverá receber atributos de força , vida , fraqueza , e especial!

deverá existir metodos de atacar , defender , e jogar o especial

Dois herois iram lutar , resultando em um vencedor e um derrotado!

'''

class Hero:
  def __init__(self , name , force , life , frailty , special):
    self.name = name
    self.force = force
    self.life = life
    self.frailty = frailty
    self.special = special


  def atacar(self):
    print(f'O heroi {self.name} tem a force de {self.force}')

heroi_1 = Hero(name='bita'  , force=80 , life= 100 , frailty= 'tiro no pe ' , special= 'raduken')

heroi_1.atacar()
