

resultado = 0

cpfEnviado = input('digite seu cpf: ')
noveDigitos = cpfEnviado[:9]

regressar = 10
for digito in noveDigitos:
  resultado += int(digito) * int(regressar)
  regressar -= 1
primeiroDigito = (resultado * 10) % 11

primeiroDigito = primeiroDigito if primeiroDigito <= 9 else 0



dezDigitos = noveDigitos + str(primeiroDigito)
regressar2 = 11

resultado2 = 0

for digito in dezDigitos:
  resultado2 += int(digito) * regressar2
  regressar2 -= 1
segundoDigito = (resultado2 * 10) % 11
segundoDigito= segundoDigito if segundoDigito <= 9 else 0

cpfGerado = f'{noveDigitos}{primeiroDigito}{segundoDigito}'


if cpfEnviado == cpfGerado :
  print(f'{cpfEnviado} é valido')
else:
  print('CPF invalido')
