from prettytable import PrettyTable
usuarios = {"thiago":[3112]}
def login():
    sair=False
    while sair!=True:
        print(" Bem vindo ao sistema de usuário ")
        print('1 - Faça o Login')
        print('2 - Criar Usuário')
        op=int(input('Digite a opção escolhida:'))
        email=input('Digite seu email:')
        senha=input('Digite sua senha:')
        if op ==1:
            if email == 'admin' and senha == 'admin':
                print('Usuario Logado!\n')
                return True
            if email in usuarios:
                if senha == usuarios[email][0]:
                    print("Login bem-sucedido!")
                    return True
            print('Usuario ou senha Incorretos\n')
        if op ==2:
            usuarios[email] = [senha]
            print("Usuário criado com sucesso!")
            return True


def criar_usuario():
    email = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[email] = [senha]
    print("Usuário criado com sucesso!")
