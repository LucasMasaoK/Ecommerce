import sqlite3
from prettytable import PrettyTable
import matplotlib.pyplot as grafico


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
        pretty = PrettyTable(["VENDA", "VENDEDOR", "VALOR TOTAL"])
        data = []
        vlTotal = []
        for vendas in self.query:
            pretty.add_row([vendas[0], vendas[1], vendas[3]])
            data.append(vendas[5])
            vlTotal.append(vendas[3])
        print(pretty)
        print("(1) - Sim")
        print("(2) - Não")
        cEscolha = input('Deseja gerar um relatório gráfico?')
        if int(cEscolha) == 1:
            grafico.ylabel('Valor da Venda')
            grafico.xlabel('Data')
            grafico.plot(data, vlTotal)
            grafico.show()

    def vendasPorPeriodo(self):
            print('\n-----------Data Inicial-----------')
            cInicial=input('Digite a data inicial:')
            cFinal = input('Digite a data Final:')
            params=(cInicial,cFinal)
            self.query=self.cursor.execute("""SELECT V.ID_CLIENTE, V.ID_FUNCIONARIO, V.ID_FORMAPGTO, V.VL_TOTAL, V.DESCONTO, V.DATA_VENDA FROM VENDAS AS V
WHERE V.DATA_VENDA BETWEEN '%s' AND '%s'""" % params)
            vendedor=[]
            vlTotal=[]
            pretty = PrettyTable(["VENDA", "VENDEDOR", "VALOR TOTAL"])
            for vendas in self.query:
                pretty.add_row([vendas[0],vendas[1],vendas[3]])
            print(pretty)
            print("(1) - Sim")
            print("(2) - Não")
            cEscolha=input('Deseja gerar um relatório gráfico?')
            if int(cEscolha)==1:
                vendedor=[]
                vlTotal=[]
                self.query = self.cursor.execute("""SELECT F.NOME, sum(V.VL_TOTAL)FROM VENDAS AS V
                JOIN FUNCIONARIO AS F ON F.ID_FUNCIONARIO=V.ID_FUNCIONARIO
                WHERE V.DATA_VENDA BETWEEN '%s' AND '%s' GROUP BY V.ID_FUNCIONARIO""" % params)
                vendedor = []
                vlTotal = []
                for vendas in self.query:
                    vendedor.append(vendas[0])
                    vlTotal.append(vendas[1])
                grafico.ylabel('Valor da Venda')
                grafico.xlabel('Vendedores')
                grafico.bar(vendedor,vlTotal)
                grafico.show()



