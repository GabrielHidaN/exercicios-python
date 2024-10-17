import json
from desafio_json import CAMINHO_ARQUIVO , Pessoa
with open(CAMINHO_ARQUIVO , 'r') as arquivo:
  dados = json.load(arquivo)
  print(dados)
