#atributos de classe


class Pessoa:

  atributo = 'valor'
  ano_atual = 2024

  def __init__(self , nome , idade):
    self.nome = nome
    self.idade = idade
  def get_ano_nasc(self):
    return Pessoa.ano_atual - self.idade

p1 = Pessoa('joao' , 35)
p2 = Pessoa('gabriel' , 21)


print(Pessoa.ano_atual)
print(p1.get_ano_nasc())
print(p2.get_ano_nasc())
