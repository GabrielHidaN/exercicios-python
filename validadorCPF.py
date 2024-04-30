

resultado = 0

cpf = '13366946458'
noveDigitos = cpf[:9]

regressar = len(cpf)
for digito in noveDigitos:
  regressar -= 1
  resultado += int(digito) * int(regressar)
  print(digito , regressar)
print(resultado)
