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
    