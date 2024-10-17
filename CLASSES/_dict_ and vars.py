#__dict__ e  vars para atributos de instancia


class Pessoa:

  atributo = 'valor'
  ano_atual = 2024

  def __init__(self , nome , idade):
    self.nome = nome
    self.idade = idade
  def get_ano_nasc(self):
    return Pessoa.ano_atual - self.idade

dados = {'nome': 'gabriel', 'idade': 21}
p1 = Pessoa(**dados)


print(Pessoa.ano_atual)
print(p1.get_ano_nasc())

print(vars(p1))
