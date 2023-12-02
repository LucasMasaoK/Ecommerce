import sqlite3


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


    def adicionar(self):
        nome = input('Digite o Nome do Fornecedor:')
        cnpj = input('Digite o CNPJ do Fornecedor:')
        oFornecedor = TFornecedor(id, nome, cnpj)
        params=(nome, cnpj)
        self.cursor.execute(
            f"""insert into fornecedor(nome, cnpj) values (?, ?)""",[params])
        self.connect.commit()
        print(f"Fornecedor {oFornecedor.nome} adicionado com sucesso.")


    def buscar(self):
        acho=''
        params = input('Digite o ID:')
        dados=self.cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor=?",[params])
        for fornecedor in dados:
            if fornecedor[0] == int(params):
                print(
                    f"Professor encontrado - ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Disciplina: {fornecedor[2]}")
                acho=True
                break
        if acho!=True:
            print(f"Professor com ID {params} não encontrado.")

    def deletar(self):
        acho=''
        params = input('Digite o ID:')
        dados=self.cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor=?",[params])
        for fornecedor in dados:
            if fornecedor[0] == int(params):
                self.cursor.execute("DELETE FROM fornecedor where id_fornecedor=?",[params])
                print(
                    f"Professor ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Disciplina: {fornecedor[2]} foi deletado")
                self.connect.commit()
                acho=True
                break
        if acho!=True:
            print(f"Professor com ID {params} não encontrado.")


