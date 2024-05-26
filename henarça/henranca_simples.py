class Veiculo:
  def __init__(self , cor , marca , qtd_pneu , placa , tipo):
    self.cor = cor
    self.marca = marca
    self.qtd_pneu = qtd_pneu
    self.placa = placa
    self.tipo = tipo

  def ligar(self):
    return 'Ligando Motor'

  def buzinar (self , tipo):
    self.tipo = tipo
    if tipo == 'moto' :

      return 'bibbiiiiiit'
    elif tipo == 'carro':

      return 'popoooooom'


class Moto(Veiculo):
  pass
class Carro(Veiculo):
  pass
class Bike(Veiculo):
  pass

moto = Moto("preta" , "yamaha" , 2 , "exd-1234", "moto")
print(moto.ligar())
print(moto.cor , moto.placa)
carro = Carro("prata" , "honda", 4 , "kbr-0061 " ,"carro")

print(carro.cor , carro.placa)
print(carro.buzinar("carro"))
