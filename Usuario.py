
usuarios = {"thiago": ["3112"]}
logado= ["log"]
def login():
    sair=False
    while sair!=True:
        print(" Bem vindo ao sistema de usuário ")
        print('1 - Faça o Login')
        print('2 - Criar Usuário')
        op=int(input('Digite a opção escolhida:'))
        if op ==1:
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            if email == 'admin' and senha == 'admin':
                print('Usuario Logado!\n')
                logado[0]="admin"
                return True
            if email in usuarios:
                if senha in usuarios[email][0]:
                    print(f"Login bem-sucedido!\n Bem vindo {email}")
                    logado[0]=email
                    return True
            print('Usuario ou senha Incorretos\n')
        if op ==2:
            criar_usuario()
            return True


def criar_usuario():
    email = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[email] = [senha]
    logado[0]=email
    print("Usuário criado com sucesso!")
    imprimirLogin()

def imprimirLogin():
    print(logado[0])
