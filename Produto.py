import sqlite3
from Fornecedor import fornecedorController
class TProduto:
    def __init__(self,pID_fornecedor,pNome,pEstoque,pVL_venda):
        self.id_fornecedor=pID_fornecedor
        self.nome=pNome
        self.estoque=pEstoque
        self.vl_venda=pVL_venda


class produtosController:
    def __init__(self):
        self.connect = sqlite3.connect('Banco.db')
        self.cursor = self.connect.cursor()
        self.oFornecedor = fornecedorController()

    def adicionarProduto(self):
        self.oFornecedor.listarFornecedores()
        while True:
            try:
                cID_fornecedor = int(input("Digite o ID do Fornecedor: "))
                break
            except ValueError:
                print('Valor informado não é um inteiro!')
                continue
        if self.oFornecedor.buscarFornecedor(cID_fornecedor):
            cNome = input("Digite o nome do Produto: ")
            cEstoque = input("Digite a quantidade de Estoque: ")
            cVL_venda = input("Digite o valor de venda R$: ")
            self.oProduto=TProduto(cID_fornecedor,cNome,cEstoque,cVL_venda)
            params=(self.oProduto.id_fornecedor,self.oProduto.nome,self.oProduto.estoque,self.oProduto.vl_venda)
            self.cursor.execute(
                """INSERT INTO PRODUTOS(id_fornecedor,nome,estoque,vl_venda) 
                VALUES ('%s', '%s', '%s', '%s')""" % params)
            self.connect.commit()
            print(f'O {self.oProduto.nome} foi cadastrado com sucesso!')
        else:
            print(f"Fornecedor com ID {cID_fornecedor} não encontrado.")

    def deletarProduto(self):
        acho = ''
        params = input("Digite o ID do Produto: ")
        query = self.cursor.execute("""SELECT * FROM PRODUTOS WHERE ID_PRODUTO='%s'""" % params)
        for produto in query:
            if produto[0] == int(params):
                query = self.cursor.execute("""DELETE FROM PRODUTOS WHERE ID_PRODUTO='%s'""" % params)
                print(
                    f"Produto Removido - ID: {produto[0]}, Nome: {produto[1]}, VL Venda: {produto[4]}")
                self.connect.commit()
                acho = True
                break
            if acho != True:
                print(f"Produto com ID {params} não encontrado.")

    def listarProdutos(self):
        query = self.cursor.execute("""SELECT * FROM PRODUTOS """)
        print('\n-----------PRODUTOS-----------')
        for produto in query:
            print(
                    f"ID: {produto[0]}, Nome: {produto[2]}, VL Venda: {produto[4]}")
        print('\n')
    def editarProduto(self):
        self.listarProdutos()
        while True:
            try:
                cID = int(input('Digite o ID do Produto:'))
                break
            except ValueError:
                print('Valor informado não é um inteiro!')
                continue
        if self.buscarProduto(cID):
            while True:
                print('\n-----------EDITAR-----------')
                print("(1) - Nome")
                print("(2) - Fornecedor")
                print("(3) - Quantidade")
                print("(4) - Valor")
                print("(5) - Cancelar")
                inputUsuario = int(input('Digite a opção escolhida:'))
                if inputUsuario == 1:
                    cNovo = input('Digite o novo valor: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE PRODUTOS SET nome= '%s' WHERE ID_PRODUTO='%s'""" % params)
                elif inputUsuario == 2:
                    self.oFornecedor.listarFornecedor()
                    cNovo = input('Digite o novo valor: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE PRODUTOS SET id_fornecedor= '%s' WHERE ID_PRODUTO='%s'""" % params)
                elif inputUsuario == 3:
                    cNovo = input('Digite o novo valor: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE PRODUTOS SET estoque= '%s' WHERE ID_PRODUTO='%s'""" % params)
                elif inputUsuario == 4:
                    cNovo = input('Digite o novo valor: ')
                    params = (cNovo, cID)
                    self.cursor.execute("""UPDATE PRODUTOS SET vl_venda= '%s' WHERE ID_PRODUTO='%s'""" % params)
                elif inputUsuario == 5:
                    break
                print(f'Produto {cID} alterado com sucesso!')
                self.connect.commit()
                break
        else:
            print(f"Produto com ID {cID} não encontrado.")

    def buscarProduto(self,pID):
        acho=''
        query=self.cursor.execute("""SELECT * FROM PRODUTOS WHERE ID_PRODUTO= '%s' """ % pID)
        for produto in query:
            if produto[0] == int(pID):
                acho = True
                return True
                break
            if acho != True:
                return False

