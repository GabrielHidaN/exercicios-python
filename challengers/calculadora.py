while True:

  # o programa pede que o usuario informe os valores
  num_1 = input('Digite um número: \n')
  num_2 = input('Digite outro número: \n')
  num1_float = ''
  num2_float = ''

  operadores = '+-*/'


  validador = None
  try:
    num1_float= float(num_1)
    num2_float = float(num_2)
    validador = True

  except:
    validador = None

  if validador is None:
    print('Um ou Ambos os Números é/são inválidos!\n')
    continue

  # o programa pede que o usuario informe qual será a operação desejada
  operador = input('Digite o operador: \n')

  if len(operador)> 1:
      print('Você deve indicar UM operador apenas!\n')
      continue
  else:
    if operador not in operadores:
      print('Operador inválido!\n')

# Calculos

  if operador == '+':
    resultado = num1_float + num2_float
    print(f'@ O Resultado da Soma ( {num1_float} + {num2_float} ) é = {resultado} @\n')

  elif operador == '-':
    resultado = num1_float - num2_float
    print(f'@ O Resultado da Subtração ( {num1_float} - {num2_float} ) é = {resultado} @\n')

  elif operador == '*':
    resultado = num1_float * num2_float
    print(f'@ O Resultado da Multiplicação ( {num1_float} * {num2_float} ) é = {resultado} @\n')

  elif operador == '/':
    resultado = num1_float / num2_float
    print(f'@ O Resultado da Subtração ( {num1_float} / {num2_float} ) é = {resultado} @\n')

  sair = input('Deseja encerrar o Programa? [s]im \n')
  sair = sair.lower().startswith('s')

  if sair is True:
    break
  else:
    continue
