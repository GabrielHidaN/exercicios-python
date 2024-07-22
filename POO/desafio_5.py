'''
Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas.

'''

class Paciente:
  historico_consultas = []
  def __init__(self, nome , idade ):
    self.nome = nome
    self.idade = idade

  def consultar(self):

    consulta = f'==== Consultando ====\nNome: {self.nome}\nIdade: {self.idade}\n'

    return consulta

paciente_1 = Paciente('jose', 52)
consulta_historico  = paciente_1.consultar()
Paciente.historico_consultas.append(consulta_historico)
paciente_2 = Paciente('Maria', 22)
consulta_historico  = paciente_2.consultar()
Paciente.historico_consultas.append(consulta_historico)

for consulta in Paciente.historico_consultas:
  print(consulta)
