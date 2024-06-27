#Desafio do Heroi

'''
POO

Cada heroi deverá receber atributos de força , vida , fraqueza , e especial!

deverá existir metodos de atacar , defender , e jogar o especial

Dois herois iram lutar , resultando em um vencedor e um derrotado!

'''


class Hero:
  def __init__(self , nome , poder , fraqueza  , vida ):
    self.nome = nome
    self.poder = poder
    self.fraqueza = fraqueza
    self.vida = vida

  def fraqueza_herois(self , nome , vida):

    self.nome = nome
    self.vida = vida


    herois_fraqueza_agua = ['bita' , 'breeze' , 'boomble']
    herois_fraqueza_fogo = ['locky' , 'poseidon' , 'tyrius']

    if nome in herois_fraqueza_agua:
        vida = (vida / 100) * 75

    elif nome in herois_fraqueza_fogo:
        vida = (vida / 100) * 75

    return vida

  def batalhar(self , heroi_1 , heroi_2):
    self.heroi_1 = heroi_1
    self.heroi_2 = heroi_2

    vencedor = heroi_1 if (heroi_1 > heroi_2 ) else heroi_2
    return vencedor

heroi_1 = Hero(nome= 'bita' , poder='choque' , fraqueza='agua' , vida= 100)
vida = heroi_1.fraqueza_herois( 'bita' , 100)
print(vida)
