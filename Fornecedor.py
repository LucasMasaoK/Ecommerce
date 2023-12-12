import sqlite3
from prettytable import PrettyTable

class TFornecedor:
    def __init__(self, pId, pNome, pCNPJ):
        self.id = pId
        self.nome = pNome
        self.cnpj = pCNPJ

class fornecedorController:
    def __init__(self):
        self.connect = sqlite3.connect('Banco.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            """create table if not exists fornecedor (id_fornecedor integer primary key autoincrement, nome text,cnpj text)""")


    def adicionarFornecedor(self):
        nome = input('Digite o Nome do Fornecedor:')
        cnpj = input('Digite o CNPJ do Fornecedor:')
        oFornecedor = TFornecedor(id, nome, cnpj)
        params=(nome, cnpj)
        self.cursor.execute(
            """INSERT INTO FORNECEDOR(nome, cnpj) values ('%s', '%s')""" % params)
        self.connect.commit()
        print(f"Fornecedor {oFornecedor.nome} adicionado com sucesso.")

    def deletarFornecedor(self):
        acho=''
        params = input('Digite o ID:')
        dados=self.cursor.execute("SELECT * FROM FORNECEDOR WHERE ID_FORNECEDOR=?",[params])
        for fornecedor in dados:
            if fornecedor[0] == int(params):
                self.cursor.execute("DELETE FROM FORNECEDOR WHERE ID_FORNECEDOR=?",[params])
                print(
                    f"Fornecedor ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Disciplina: {fornecedor[2]} foi deletado")
                self.connect.commit()
                acho=True
                break
        if acho!=True:
            print(f"Professor com ID {params} não encontrado.")

    def listarFornecedores(self):
        self.query = self.cursor.execute("""SELECT * FROM FORNECEDOR """)
        pretty = PrettyTable(["ID FORNECEDOR", "NOME","CNPJ"])
        for fornecedor in self.query:
            pretty.add_row([fornecedor[0], fornecedor[1], fornecedor[2]])
        print(pretty)

    def editarFornecedor(self):
        self.listarFornecedores()
        while True:
            try:
                pId = int(input('Digite o ID do Fornecedor:'))
                break
            except ValueError:
                print('Valor informado não é um inteiro!')
                continue

        if self.buscarFornecedor(pId):
            while True:
                print('\n-----------EDITAR-----------')
                print("(1) - Nome")
                print("(2) - CNPJ")
                print("(3) - Cancelar")
                inputUsuario = int(input('Digite a opção escolhida:'))

                if inputUsuario == 1:
                    pNome = input('Digite o novo valor para o Nome: ')
                    params = (pNome, pId)
                    self.cursor.execute("""UPDATE FORNECEDOR SET nome= ? WHERE id_fornecedor=?""", params)
                elif inputUsuario == 2:
                    cnpj = input('Digite o novo valor para o CNPJ: ')
                    params = (cnpj, pId)
                    self.cursor.execute("""UPDATE FORNECEDOR SET cnpj= ? WHERE id_fornecedor=?""", params)
                elif inputUsuario == 3:
                    break
                print(f'Fornecedor {pId} alterado com sucesso!')
                self.connect.commit()
                break
        else:
            print(f"Fornecedor com ID {pId} não encontrado.")

    def buscarFornecedor(self, pId):
        acho = ''
        query = self.cursor.execute("""SELECT * FROM FORNECEDOR WHERE ID_FORNECEDOR= '%s' """ % pId)
        for produto in query:
            if produto[0] == int(pId):
                acho = True
                return True
                break
            if acho != True:
                return False
