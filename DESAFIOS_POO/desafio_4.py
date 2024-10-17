'''
Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a velocidade atual.
'''

class Carro:
  def __init__(self, marca , modelo , velocidade):
    self.marca = marca
    self.modelo = modelo
    self.velocidade = velocidade

  def ligar_carro(self):
    print('Ligando o Motor...')
    motor_ligado = True
    return motor_ligado

  def desligar_carro(self):
    print('Desligando o Motor...')
    motor_ligado = False
    return motor_ligado

  def acelerar(self, motor_ligado = False):
    if motor_ligado == True:
      print('Vruuuuum Vruuuumm')
      velocidade_atual = self.velocidade
      return velocidade_atual

    print('motor desligado')

golf = Carro('wolkswagen' , 'golf' , '80km')
golf.ligar_carro()
golf.acelerar(True)

print(f'Carro: {golf.modelo}\nMarca: {golf.marca}\nVelocidade: {golf.velocidade}')
