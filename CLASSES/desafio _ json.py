'''
Exercicio - salve sua classe em json
salve os dados da sua classe em json
e depois crie novamente as instâncias
da classe com os dados salvos
faça em arquivos separados
'''
import json
CAMINHO_ARQUIVO = 'desafio_json.py'

class Pessoa:

  def __init__(self, nome , idade):
    self.nome = nome
    self.idade = idade

p1 = Pessoa('Gabriel' , 20 )
p2 = Pessoa('Aline' , 18 )
p3 = Pessoa('Josefa' , 10 )
db = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO , 'w') as arquivo:
  json.dump(db, arquivo , ensure_ascii=False, indent=2)
