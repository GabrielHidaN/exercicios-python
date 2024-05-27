class Passaro:
  def voar(self):
    print('Voando')

class Pardal(Passaro):
  def voar(self):
    super().voar()

class Avestruz(Passaro):
  def voar(self):
    print('Não pode voar')

def plano_de_voo(obj):
  obj.voar()



plano_de_voo(Pardal())
plano_de_voo(Avestruz())
