
def par_ou_impar(numero):
    
    par_impar = 'Par' if (numero%2) == 0 else 'Impar'
    return par_impar

numero = (int(input('Digite um Número Positivo para verificação: \n =>')))
resultado = par_ou_impar(numero=numero)

print(f'O Número {numero} é {resultado}.')
