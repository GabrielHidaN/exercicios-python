'''Descrição: Implemente uma função que retorne o maior e o menor número de uma lista.

Exemplo: Entrada: [3, 7, 1, 9, 2] Saída: Maior: 9, Menor: 1'''

def maior_menor(lista):

    if not lista:
        return "A lista está vazia"

    maior = max(lista)
    menor = min(lista)
    
    return f'Maior: {maior}, Menor: {menor}'

        

lista = [-2,22, 1,3,2, 8, 4,5,6,7]
resultado = maior_menor(lista)
print(resultado)