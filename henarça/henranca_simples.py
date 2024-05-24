class Veiculo:
  def __init__(self , cor , marca , qtd_pneu , placa ):
    self.cor = cor
    self.marca = marca
    self.qtd_pneu = qtd_pneu
    self.placa = placa

  def ligar(self):
    print('Ligando Motor')

class Moto(Veiculo):
  pass
class Carro(Veiculo):
  pass
class Bike(Veiculo):
  pass

moto = Moto("preta" , "yamaha" , 2 , "exd-1234")
moto.ligar()
print(moto.cor , moto.placa)
