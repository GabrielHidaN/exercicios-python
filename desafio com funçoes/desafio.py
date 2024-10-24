"""
crie funções que duplicam , triplicam e quadruplicam o numero enviado como parametro"
"""

def multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

for numero in [10,20,30,40]:
    print(f'{numero}  Duplicado = {duplicar(numero=numero)}')
    print('='*30)
    print(f'{numero}  Triplicado = {triplicar(numero=numero)}')
    print('='*30)
    print(f'{numero}  Quadruplicado = {quadriplicar(numero=numero)}')
    print('='*30)