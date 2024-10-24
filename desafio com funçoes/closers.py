""""
Closers Funções que retornan outras funções!
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa Noite')

for nome in ['João', 'José', 'Maria', 'Pedro']:
    print(falar_bomdia(nome))
    print('='*10)
    print(falar_boanoite(nome))

