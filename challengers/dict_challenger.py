#ex sistema de perguntas e respostas

perguntas= [
    {
    'pergunta': 'Quanto é 5X5?',
    'opções' : ['10','20','25','30','35'],
    'resposta':'25'
    },

    {
    'pergunta': 'Quanto é 30/3?',
    'opções' : ['10','20','25','30','35'],
    'resposta':'10'
    },

    {
    'pergunta': 'Quanto é 30-10?',
    'opções' : ['10','20','25','30','35'],
    'resposta':'20'
    },
]


def perguntas_respostas(pergunta , opções , resposta ):
    print(pergunta)
    for op in opções:
        print()
        print(op)
    resposta_enviada = input('\n=>\t')
    if resposta_enviada != resposta:
        return  False
    else:
         return True



indice = 0
acertos = 0
while indice < len(perguntas):

    p1 = perguntas_respostas( pergunta= perguntas[indice]['pergunta'] , opções=perguntas[indice]['opções'] , resposta= perguntas[indice]['resposta'])
    if p1 == False:
        print(f'\nVocẽ Falhou! \nResposta Errada!\n')

    else:
        print(f'\nParabéns! \nResposta Exata!')
        acertos += 1
    indice += 1

print(f'Você teve {acertos} Acertos!')
    