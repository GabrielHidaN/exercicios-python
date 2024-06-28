

class Hero:
  def __init__(self , nome , vida , fraqueza , poder):
    self.fraqueza = fraqueza
    self.poder = poder
    self.nome = nome
    self.vida = vida



  def descrever_heroi(self  , nome , poder , fraqueza , vida):
    self.nome = nome
    self.poder = poder
    self.fraqueza = fraqueza
    self.vida = vida

    descrever = f'O Herói {self.nome} tem no total {self.vida}  Pontos de Vida. Sua fraqueza é {self.fraqueza}  e seu poder é {self.poder}.'
    return descrever
'''
  def definir_vencedor(self , heroi_1 , heroi_2):
    self.heroi_1 = heroi_1
    self.heroi_2 = heroi_2

    vencedor = heroi_1 if (heroi_1 > heroi_2 ) else heroi_2
    return vencedor
'''

def definir_poder_herois(nome):



  poder_herois_ar = [ 'breeze', 'locky' , 'tyrius']
  poder_herois_agua = ['poseidon' , 'danke' , 'cold']
  poder_herois_fogo = ['bita' , 'boomble' , 'fubuki']
  poder_herois_terra = ['broky' , 'hiru' , 'demon']



  if nome in poder_herois_ar:
    poder = 'ar'

  elif nome in poder_herois_agua:
    poder = 'agua'

  elif nome in poder_herois_fogo:
    poder = 'fogo'

  elif nome in poder_herois_terra:
    poder = 'terra'
  else:
    poder = None

  return poder


def definir_fraqueza_herois(nome):



  herois_fraqueza_agua = ['bita' , 'breeze' , 'boomble']
  herois_fraqueza_fogo = ['locky' , 'hiru' , 'cold']
  herois_fraqueza_terra = ['poseidon' , 'danke' , 'fubuki']
  herois_fraqueza_ar = ['demon' , 'broky' , 'tyrius']



  if nome in herois_fraqueza_agua:
    fraqueza = 'agua'

  elif nome in herois_fraqueza_fogo:
    fraqueza = 'fogo'

  elif nome in herois_fraqueza_ar:
    fraqueza = 'ar'

  elif nome in herois_fraqueza_terra:
    fraqueza = 'terra'
  else :
    fraqueza = None

  return fraqueza

nome = input('Digite o nome do Herói: \n =>')
poder  = definir_poder_herois(nome = nome)
fraqueza= definir_fraqueza_herois(nome = nome)
heroi_1 = Hero(nome= nome , vida= 100 , poder= poder , fraqueza= fraqueza)

if (poder is  None) or (fraqueza is None):
  print('@@@ Herói não encontrado! @@@')
else:
  descrever = heroi_1.descrever_heroi(nome= nome , fraqueza=fraqueza , poder=poder , vida=100)
  print(descrever)
