import sqlite3
from prettytable import PrettyTable

class TUsuario:
    def __init__(self, cId, cNome,cEmail, cSenha,cTipo, cDtNascimento, cCpf, cEndereco):
        self.id = cId
        self.nome = cNome
        self.email = cEmail
        self.senha = cSenha
        self.tipo=cTipo
        self.dt_nascimento = cDtNascimento
        self.cpf = cCpf
        self.endereco = cEndereco


class usuarioController:
    def __init__(self):
        self.connect = sqlite3.connect('Banco.db')
        self.cursor = self.connect.cursor()


    def adicionarCliente(self):
        nome = input('Digite o Nome do Cliente:')
        email = input('Digite o Email :')
        senha = input('Digite a senha :')
        tipo= input('Digite o Tipo: ')
        dt_nascimento = input('Digite a Data de Nascimento do Cliente:')
        cpf = input('Digite o CPF do Cliente:')
        endereco = input('Digite o Endereço do Cliente:')
        oUsuario = TUsuario(id, nome, email, senha,tipo, dt_nascimento, cpf, endereco)
        params = (oUsuario.nome,oUsuario.email, oUsuario.senha,oUsuario.tipo, oUsuario.dt_nascimento, oUsuario.cpf, oUsuario.endereco)
        self.cursor.execute(
            """insert into USUARIO (NOME, EMAIL,  SENHA, TIPO, DT_NASCIMENTO, CPF, ENDERECO)
  values (?, ?, ?, ?, ?, ?, ?)""", params)
        self.connect.commit()
        print(f"Cliente {oUsuario.nome} adicionado com sucesso.")

    def deletarCliente(self):
        acho = ''
        params = input('Digite o ID do Cliente:')
        dados = self.cursor.execute("SELECT * FROM USUARIO WHERE id_cliente=?", [params])
        for cliente in dados:
            if cliente[0] == int(params):
                self.cursor.execute("DELETE FROM USUARIO WHERE id_cliente=?", [params])
                print(
                    f"Cliente ID: {cliente[0]}, Nome: {cliente[1]}, Data de Nascimento: {cliente[2]}, CPF: {cliente[3]}, Endereço: {cliente[4]} foi deletado")
                self.connect.commit()
                acho = True
                break
        if not acho:
            print(f"Cliente com ID {params} não encontrado.")

    def listarClientes(self):
        self.query = self.cursor.execute("""SELECT * FROM USUARIO WHERE TIPO='C'""")
        pretty = PrettyTable(["ID CLIENTE", "NOME", "DATA DE NASCIMENTO", "CPF", "ENDEREÇO"])
        for cliente in self.query:
            pretty.add_row([cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]])
        print(pretty)
        acho = ''
        while True:
            params = input('Digite o ID do Cliente:')
            dados = self.cursor.execute("SELECT * FROM USUARIO WHERE ID_CLIENTE=?", [params])
            for funcionario in dados:
                if funcionario[0] == int(params):
                    return funcionario[0]
            if acho != True:
                print(f"Cliente com ID {params} não encontrado.")

    def listarFuncionario(self):
        self.query = self.cursor.execute("""SELECT * FROM USUARIO WHERE TIPO='F'""")
        pretty = PrettyTable(["ID CLIENTE", "NOME", "DATA DE NASCIMENTO", "CPF", "ENDEREÇO"])
        for cliente in self.query:
            pretty.add_row([cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]])
        print(pretty)
        acho = ''
        while True:
            params = input('Digite o ID do funcionário:')
            dados = self.cursor.execute("SELECT * FROM USUARIO WHERE ID_CLIENTE=?", [params])
            for funcionario in dados:
                if funcionario[0] == int(params):
                    return funcionario[0]
            if acho != True:
                print(f"Funcionario com ID {params} não encontrado.")

    def editarCliente(self):
        self.listarClientes()
        while True:
            try:
                cID = int(input('Digite o ID do Cliente:'))
                break
            except ValueError:
                print('Valor informado não é um inteiro!')
                continue

        if self.buscarCliente(cID):
            while True:
                print('\n-----------EDITAR-----------')
                print("(1) - Nome")
                print("(2) - Data de Nascimento")
                print("(3) - CPF")
                print("(4) - Endereço")
                print("(5) - Cancelar")
                inputUsuario = int(input('Digite a opção escolhida:'))

                if inputUsuario == 1:
                    cNovo = input('Digite o novo valor para o Nome: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE USUARIO SET nome= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 2:
                    cNovo = input('Digite o novo valor para a Data de Nascimento: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE USUARIO SET dt_nascimento= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 3:
                    cNovo = input('Digite o novo valor para o CPF: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE USUARIO SET cpf= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 4:
                    cNovo = input('Digite o novo valor para o Endereço: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE USUARIO SET endereco= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 5:
                    break
                print(f'Cliente {cID} alterado com sucesso!')
                self.connect.commit()
                break
        else:
            print(f"Cliente com ID {cID} não encontrado.")


    def buscarCliente(self, cMail):
        acho = ''
        query = self.cursor.execute("""SELECT EMAIL FROM USUARIO WHERE EMAIL= '%s' """ % cMail)
        for usuario in query:
            if usuario[0] == cMail:
                acho = True
                return True
                break
            elif acho != True:
                return False
    def validaSenha(self, cSenha):
        acho = ''
        query = self.cursor.execute("""SELECT SENHA FROM USUARIO WHERE SENHA= '%s' """ % cSenha)
        for senha in query:
            if senha[0] == cSenha:
                acho = True
                return True
                break
            elif acho != True:
                return False

    def login(self):
        sair=False
        while sair!=True:
            print("Bem vindo ao sistema de usuário! \n")
            print('1 - Faça o Login')
            print('2 - Criar Usuário')
            op=int(input('\nDigite a opção escolhida:'))
            if op ==1:
                email = input('Digite seu email: ')
                if  self.buscarCliente(email) == True:
                    senha = input('Digite sua senha: ')
                    if self.validaSenha(senha) == True:
                        print(f"Login bem-sucedido!\n")
                        return True
                    else:
                        print('Usuario ou senha Incorretos\n')
                        continue
                else:
                    print('Usuario não encontrado!')
                    continue
            if op ==2:
                self.adicionarCliente()
                return True
