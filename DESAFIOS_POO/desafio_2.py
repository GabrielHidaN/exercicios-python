'''
Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, considerando descontos de impostos e benefícios.
'''

class Funcionario:

  empresa = 'G technology'

  def __init__(self , nome , cargo):
    self.nome = nome
    self.cargo = cargo

  def calcular_salario(self):

    cargos_ti = ['dev', 'cibersec' , 'devops']

    if self.cargo in cargos_ti:
      salario_dev = 3000
      salario_sec = 5000
      salario_devops = 4000
      if self.cargo == 'dev':
        salario = salario_dev
      elif self.cargo == 'cibersec':
        salario = salario_sec
      elif self.cargo == 'devops':
        salario = salario_devops

    vale_transporte = 80
    vale_alimentacao = 150
    beneficios_total = vale_alimentacao + vale_transporte
    salario_imposto = salario - ((salario * 3)/100)
    salario_total = int(beneficios_total + salario_imposto)

    return salario_total

funcionario = Funcionario('Gabriel' , 'cibersec')

print(funcionario.nome)
print(funcionario.cargo)
print(funcionario.calcular_salario())
