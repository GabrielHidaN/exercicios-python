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
    resposta_enviada = input('\n=>')
    if resposta_enviada != resposta:
        return f'Vocẽ Falhou! \n Resposta Errada!\n A Resposta Correta é {resposta}'
    else:
        return f'Parabéns! \nResposta Exata!'

p1 = perguntas_respostas( pergunta= perguntas[0]['pergunta'] , opções=perguntas[0]['opções'] , resposta= perguntas[0]['resposta'])

print(p1)