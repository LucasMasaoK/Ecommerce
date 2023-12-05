import sqlite3

class TProduto:
    def __init__(self,pID_produto,pID_fornecedor,pNome,pEstoque,pVL_venda):
        self.id_produto=pID_produto
        self.id_fornecedor=pID_fornecedor
        self.nome=pNome
        self.estoque=pEstoque
        self.vl_venda=pVL_venda


class produtosController:
    def __init__(self):
        self.connect = sqlite3.connect('Banco.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS PRODUTOS (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        id_fornecedor INTEGER, 
        nome TEXT,
        estoque INTEGER,
        vl_venda FLOAT)""")

    def adicionarProduto(self):
        cID_produto = input("Digite o ID do Produto: ")
        cID_fornecedor = input("Digite o ID do Fornecedor: ")
        cNome = input("Digite o nome do Produto: ")
        cEstoque = input("Digite a quantidade de Estoque: ")
        cVL_venda = input("Digite o valor de venda R$: ")
        oProduto=TProduto(cID_produto,cID_fornecedor,cNome,cEstoque,cVL_venda)
        params=(cID_produto,cID_fornecedor,cNome,cEstoque,cVL_venda)
        self.cursor.execute(
            """INSERT INTO PRODUTOS(id_produto,id_fornecedor,nome,estoque,vl_venda) 
            VALUES ('%s', '%s', '%s', '%s', '%s')""" % params)
        self.connect.commit()
        print(f'O {oProduto.nome} foi cadastrado com sucesso!')

    def buscarProduto(self):
        acho=''
        params = input("Digite o ID do Produto: ")
        query=self.cursor.execute("""SELECT * FROM PRODUTOS WHERE ID_PRODUTO= '%s' """ % params)
        for produto in query:
            if produto[0] == int(params):
                print(
                    f"Professor encontrado - ID: {produto[0]}, Nome: {produto[1]}, VL Venda: {produto[4]}")
                acho = True
                break
            if acho != True:
                print(f"Professor com ID {params} não encontrado.")

    def listarProdutos(self):
        query = self.cursor.execute("""SELECT * FROM PRODUTOS """)
        for produto in query:
            print(
                    f"ID: {produto[0]}, Nome: {produto[2]}, VL Venda: {produto[4]}")

    def removerProduto(self):
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

