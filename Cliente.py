import sqlite3

class TCliente:
    def __init__(self, cId, cNome, cDtNascimento, cCpf, cEndereco):
        self.id = cId
        self.nome = cNome
        self.dt_nascimento = cDtNascimento
        self.cpf = cCpf
        self.endereco = cEndereco

class clienteController:
    def __init__(self):
        self.connect = sqlite3.connect('Banco.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            """create table if not exists CLIENTES (id_cliente integer primary key autoincrement, 
            nome text, dt_nascimento text, cpf text, endereco text)""")

    def adicionarCliente(self):
        nome = input('Digite o Nome do Cliente:')
        dt_nascimento = input('Digite a Data de Nascimento do Cliente:')
        cpf = input('Digite o CPF do Cliente:')
        endereco = input('Digite o Endereço do Cliente:')
        oCliente = TCliente(id, nome, dt_nascimento, cpf, endereco)
        params = (oCliente.nome, oCliente.dt_nascimento, oCliente.cpf, oCliente.endereco)
        self.cursor.execute(
            """INSERT INTO CLIENTES(nome, dt_nascimento, cpf, endereco) VALUES (?, ?, ?,?)""", params)
        self.connect.commit()
        print(f"Cliente {oCliente.nome} adicionado com sucesso.")

    def deletarCliente(self):
        acho = ''
        params = input('Digite o ID do Cliente:')
        dados = self.cursor.execute("SELECT * FROM CLIENTES WHERE id_cliente=?", [params])
        for cliente in dados:
            if cliente[0] == int(params):
                self.cursor.execute("DELETE FROM CLIENTES WHERE id_cliente=?", [params])
                print(
                    f"Cliente ID: {cliente[0]}, Nome: {cliente[1]}, Data de Nascimento: {cliente[2]}, CPF: {cliente[3]}, Endereço: {cliente[4]} foi deletado")
                self.connect.commit()
                acho = True
                break
        if not acho:
            print(f"Cliente com ID {params} não encontrado.")

    def listarClientes(self):
        query = self.cursor.execute("""SELECT * FROM CLIENTES """)
        print('\n-----------CLIENTES-----------')
        for cliente in query:
            print(
                f"ID: {cliente[0]}, Nome: {cliente[1]}, Data de Nascimento: {cliente[2]}, CPF: {cliente[3]}, Endereço: {cliente[4]}")
        print('\n')

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
                    self.cursor.execute("""UPDATE CLIENTES SET nome= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 2:
                    cNovo = input('Digite o novo valor para a Data de Nascimento: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE CLIENTES SET dt_nascimento= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 3:
                    cNovo = input('Digite o novo valor para o CPF: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE CLIENTES SET cpf= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 4:
                    cNovo = input('Digite o novo valor para o Endereço: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE CLIENTES SET endereco= ? WHERE id_cliente=?""", params)
                elif inputUsuario == 5:
                    break
                print(f'Cliente {cID} alterado com sucesso!')
                self.connect.commit()
                break
        else:
            print(f"Cliente com ID {cID} não encontrado.")


    def buscarCliente(self, cID):
        acho = ''
        query = self.cursor.execute("""SELECT * FROM CLIENTES WHERE ID_CLIENTE= '%s' """ % cID)
        for produto in query:
            if produto[0] == int(cID):
                acho = True
                return True
                break
            if acho != True:
                return False































"""def CadastrarCliente(idCliente, nomeCliente, CPF, telefone, CEP, endereco):
    clientes.append((idCliente, nomeCliente, CPF, telefone, CEP, endereco))
    return print(f'O {nomeCliente} foi cadastrado com sucesso!')

def GerarIDCliente():
    return len(clientes)

def LocalizaCliente(RidCliente):
    for i in range(0,len(clientes)):
       listaClientes=list(clientes[i])
       for cliente in clientes:
           idCliente, nomeCliente, CPF, telefone, CEP, endereco = cliente
           if idCliente==RidCliente:
            return print(idCliente, nomeCliente, CPF, telefone, CEP, endereco)

clientes = []

#INSERTS INICIAIS
clientes.append(('1', 'Jader', '153.144.230-73', '(69) 99133-3818', '78020-973 ', 'Rua Barão de Melgaço 2754',))
clientes.append(('2', 'Thiago', '728.357.020-91', '(49) 98077-6641', '78048-070', 'Rua Sófia',))
clientes.append(('3', 'Raphael', '220.243.310-41', '(98) 99541-5133', '78056-201', 'Rua das Margaridas',))
clientes.append(('4', 'Lucas', '239.351.830-46', '(73) 98969-6585', '78056-618', 'Rua H-1',))"""