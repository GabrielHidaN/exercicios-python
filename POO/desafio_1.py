'''Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).'''


class Aluno:

  def __init__(self , nome , matricula , notas):
    self.nome = nome
    self.matricula = matricula
    self.notas = notas

class Notas(Aluno):
  def __init__(self, nome, matricula, notas):
    super().__init__(nome, matricula, notas)

  def mostrar_notas():
    i = 1
    mostrando_nota = ''
    for nota in notas:
      mostrando_nota += f'Nota {i}: {nota}\n'
      i += 1
    return mostrando_nota
  def mostrar_resultado_escolar():
      total_nota = 0
      resultado = ''
      qtd_notas = len(notas)

      for nota in notas:
        total_nota += nota
      media = total_nota / qtd_notas
      if media >= 7:
        resultado = 'Aprovado'
      else:
        resultado = 'Reprovado'
      return resultado
notas = []
for i in range(4):
  nota_ = int(input('Digite a Nota: '))
  notas.append(nota_)


notas_aluno_1 = Notas(nome='gabriel' , matricula= 6 , notas= notas)
mostrar_notas = f'========== NOTAS ========== \nAluno:\t{notas_aluno_1.nome}\nMatricula:\t{notas_aluno_1.matricula}\n{Notas.mostrar_notas()}'

print(mostrar_notas)

resultado = f'========== RESULTADO ==========\nO Aluno {notas_aluno_1.nome} , está: {Notas.mostrar_resultado_escolar()}'
print(resultado)
