"""
em um sistema de segurança para uma aréa restrita podemos ter sensores q so acionam o alarme se dois eventos acontecerem ao mesmo tempo , movimeno detectado e porta aberta , isso pode ser modelado com uma porta AND

quando a pessoa chegar digitar a senha
se for correta
liberar 
senao 
senha errada
"""


class Securited:

    @classmethod
    def alarme(self, movimento , porta):
        self.movimento = movimento
        self.porta = porta

        alarme_acionado = True if (movimento == True) and (porta == True) else False
        return alarme_acionado

    @classmethod
    def abrir_porta(self , senha_digitada):
        senha = str('123')
        self.senha_digitada = senha_digitada
        
        abrir_porta = True   if senha_digitada == senha else False
        return abrir_porta

abrir_porta = Securited.abrir_porta(input('Digite a senha: \n=>'))

alarme = Securited.alarme(movimento= True , porta=False)

acionar_alarme = 'Uiu Uiu Uiu ' if alarme == True  else '...'
acessar_porta = 'Acesso Negado! Senha Incorreta.' if abrir_porta != True else 'Acesso Autorizado!'

print(acionar_alarme)
print(acessar_porta)