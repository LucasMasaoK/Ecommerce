def login():
    sair=False
    while sair!=True:
        email=input('Digite seu email:')
        senha=input('Digite sua senha:')
        if email=='admin' and senha=='admin':
            print('Usuario Logado!\n')
            return True
        else:
            print('Usuario ou senha Incorretos\n')
            continue

