import sqlite3
from prettytable import PrettyTable


class Relatorios:
    def __init__(self):
        self.connect = sqlite3.connect('Banco.db')
        self.cursor = self.connect.cursor()


    def vendasVendedor(self):
        while True:
            try:
                cVendor=input('Digite o ID do Vendedor:')
                break
            except ValueError:
                print('Valor informado não é um inteiro')
                continue
        self.query=self.cursor.execute("""SELECT V.ID_CLIENTE, V.ID_FUNCIONARIO, V.ID_FORMAPGTO, V.VL_TOTAL, V.DESCONTO, V.DATA_VENDA FROM VENDAS AS V
                                        JOIN FUNCIONARIO AS F ON V.ID_FUNCIONARIO= F.ID_FUNCIONARIO
                                        WHERE F.ID_FUNCIONARIO='%s'  """ % cVendor)
        for vendas in self.query:
            print(f'Venda {vendas[0]}, Funcionario:{vendas[1]}, Valor Total:{vendas[3]}')

    def vendasPorPeriodo(self):
            print('\n-----------Data Inicial-----------')
            cInicial=input('Digite a data inicial:')
            cFinal = input('Digite a data Final:')
            params=(cInicial,cFinal)
            self.query=self.cursor.execute("""SELECT V.ID_CLIENTE, V.ID_FUNCIONARIO, V.ID_FORMAPGTO, V.VL_TOTAL, V.DESCONTO, V.DATA_VENDA FROM VENDAS AS V
WHERE V.DATA_VENDA BETWEEN '%s' AND '%s'""" % params)
            pretty = PrettyTable(["VENDA", "VENDEDOR", "VALOR TOTAL"])
            for vendas in self.query:
                pretty.add_row([vendas[0],vendas[1],vendas[3]])
                #print(f'Venda {vendas[0]}, Funcionario:{vendas[1]}, Valor Total:{vendas[3]}')
            print(pretty)


