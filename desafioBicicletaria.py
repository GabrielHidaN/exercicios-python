class Bicicleta:
  def __init__(self  ,cor , modelo , ano , valor ) :

    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor


  def buzinar (self):
    print('plim plim')

  def parar (self):
    print('parando bike')
    print('bicicleta parada')

  def correr(self):
    print('vrumm ...')


#  def __str__(self) :
#    return f"Bicicleta : cor : {self.cor} , modelo: {self.modelo} , ano :{self.ano} , valor :{self.valor}"

  def __str__(self):
    return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave , valor in self.__dict__.items()])}"

bike1 = Bicicleta("azul", "caloi", 2017, 600)


registrar_bike_vendida = ''

registrar_bike_vendida += f'Bicicleta Vendida , Modelo {bike1.modelo} , cor {bike1.cor} , ano {bike1.ano} , valor {bike1.valor} \n'


bike2 = Bicicleta("vermelha", "monark", 1989 , 300)



print(bike1)
print(bike2)
