'''
Exercicio - salve sua classe em json
salve os dados da sua classe em json
e depois crie novamente as instâncias
da classe com os dados salvos
faça em arquivos separados
'''

class Pessoa:
  ano_atual = 2024

  def __init__(self, nome , idade , genero):
    self.nome = nome
    self.idade = idade
    self.genero = genero

  def ano_nasc(self):
    return Pessoa.ano_atual - self.idade

  def atribuir_genero(self):
    if self.genero == 'masc':
      self.genero =  'masculino'
      return self.genero
    elif self.genero == 'fem':
      self.genero = 'feminino'
      return self.genero

p1 = Pessoa('gabriel' , 21 , 'masc')
p2 = Pessoa('Aline' , 18 , 'fem')

p1.atribuir_genero()
p2.atribuir_genero()
p1_json = vars(p1)
p2_json = vars(p2)
print(p1_json)
print(p2_json)
