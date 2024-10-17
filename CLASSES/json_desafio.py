import json
from desafio_json import CAMINHO_ARQUIVO , Pessoa
with open(CAMINHO_ARQUIVO , 'r') as arquivo:
  pessoas = json.load(arquivo)
  
  p1 = Pessoa(**pessoas[0])
  p2 = Pessoa(**pessoas[1])

  print(p1.nome)
  print(p2.nome)
