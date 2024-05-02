import os

carrinho = []
while True:

  menu ='''
Olá oque deseja Fazer?\n
[a]\tadicionar um item ao Carrinho\n
[r]\tremover um item do Carrinho\n
[l]\tlistar carrinho \n
'''
  opcoes = input(menu)
  if opcoes == 'a':
    os.system('cls')
    item = input('Digite o Item que deseja adicionar no carrinho: ')
    carrinho.append(item)

  elif opcoes == 'r':
    os.system('cls')
    indice_str = input('Escolha o Indice que deseja Remover: ')
    try:
      indice_str = int(indice_str)
      del carrinho[indice_str]
    except IndexError:
      print('Você deve escolher um indice Valido!')
    except ValueError:
      print('Você deve escolher um indice inteiro!')
    except:
      print('Erro desconhecido!')
  elif opcoes == 'l':
    os.system('cls')
    if len(carrinho) == 0:
      print('Nada para listar!')

    for i ,produto in enumerate(carrinho):
        print( i, produto)
  else:
    os.system('cls')
    print('Opção Invalida! \n  Escolha [a]\t [r]\t [l]\n')
