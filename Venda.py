import sqlite3
import datetime

def addItem():
    connection = sqlite3.connect('Banco.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[2]}, Preço: R${produto[4]}")
    while True:
        id_produto = int(input('Digite o ID do produto: '))

        cursor.execute("SELECT * FROM Produtos WHERE id_produto=?", (id_produto,))
        produto = cursor.fetchone()

        if produto:
            qtde = int(input('Digite a quantidade: '))
            estoque = produto[3]

            if qtde <= estoque:
                novo_estoque = estoque - qtde
                cursor.execute("UPDATE Produtos SET estoque=? WHERE id_produto=?", (novo_estoque, id_produto))
                connection.commit()

                preco_unidade = produto[4]
                preco_item_total = qtde * preco_unidade

                with open('comprovante.txt', 'a') as arquivo_comprovante:
                    arquivo_comprovante.write(f'Nome do Produto: {produto[2]}\n')
                    arquivo_comprovante.write(f'Quantidade: {qtde}\n')
                    arquivo_comprovante.write(f'Preço Total do Produto: R${preco_item_total}\n')
                    arquivo_comprovante.write('-' * 30 + '\n')

                print('Produto adicionado à venda com sucesso!\n')
            else:
                print('Não há estoque suficiente para suprir a quantidade desejada.')
        else:
            print('ID do produto não localizado.')
        return preco_item_total


def subMenu():
    preco_total = 0
    sairSub = False
    global preco_item_total
    while not sairSub:
        print('============QUAL A OPÇÃO DESEJADA?================')
        print(f'1- Adicionar Mais itens\n'
              f'2- Ver itens da venda\n'
              f'3 - Fechar venda')
        escolha = input('Digite a opção escolhida: ')
        if escolha == "1":
            preco_item = addItem()
            preco_total += preco_item
            continue
        elif escolha == "2":
            try:
                with open('comprovante.txt', 'r') as arquivo_comprovante:
                    conteudo_comprovante = arquivo_comprovante.read()
                print(f'Conteúdo do comprovante: \n')
                print('-' * 30 + '\n')
                print(conteudo_comprovante)
                continue
            except FileNotFoundError:
                print('Arquivo comprovante.txt não encontrado.')
            continue
        elif escolha == "3":
            try:
                connection = sqlite3.connect('Banco.db')
                cursor = connection.cursor()

                ID_FORMAPGTO = int(input("Escolha a forma de pagamento:\n"
                                            "1 - Dinheiro\n"
                                            "2 - Cartão de crédito\n"
                                            "3 - Cartão de débito\n"
                                            "4 - Transferência bancária\n"
                                            "5 - Pix\n"))

                desconto_percentual = 0
                tem_desconto = input("Há desconto? (S/N): ").upper()
                if tem_desconto == "S":
                    desconto_percentual = float(input("Digite a porcentagem de desconto: "))

                desconto = (preco_total * desconto_percentual / 100)
                valor_com_desconto = preco_total-desconto


                data_venda = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ID_CLIENTE = 1  # Substitua por seu código para obter o ID do cliente
                ID_FUNCIONARIO = buscarFuncionario()

                cursor.execute("""
                    INSERT INTO VENDAS (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, VL_TOTAL, DESCONTO, DATA_VENDA)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (ID_CLIENTE, ID_FUNCIONARIO, ID_FORMAPGTO, preco_total, desconto, data_venda))

                connection.commit()

                with open('comprovante.txt', 'a') as arquivo_comprovante:
                    arquivo_comprovante.write(f'Forma de Pagamento: {ID_FORMAPGTO}\n')
                    arquivo_comprovante.write(f'Valor com Desconto: R${valor_com_desconto}\n')
                    arquivo_comprovante.write('-' * 30 + '\n')

                print("Venda realizada com sucesso!")

            except sqlite3.Error as e:
                print(f"Erro ao realizar a venda: {e}")
            break
        else:
            print("Opção inválida, por favor, tente novamente.")


def limparComprovante():
    try:
        with open('comprovante.txt', 'w') as arquivo_comprovante:
            arquivo_comprovante.write('')
        print('Comprovante limpo com sucesso!')
    except FileNotFoundError:
        print('Arquivo comprovante.txt não encontrado.')


try:
    with open('comprovante.txt', 'w') as arquivo_comprovante:
        arquivo_comprovante.write('')
except FileNotFoundError:
    print('Arquivo comprovante.txt não encontrado.')

def buscarFuncionario():
    while True:
        connection = sqlite3.connect('Banco.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM FUNCIONARIO")
        acho = ''
        params = input('Digite o ID do funcionário:')
        dados = cursor.execute("SELECT * FROM FUNCIONARIO WHERE ID_FUNCIONARIO=?", [params])
        for funcionario in dados:
            if funcionario[0] == int(params):
                print(
                    f"Funcionário encontrado - ID: {funcionario[0]}, Nome: {funcionario[1]}, CPF: {funcionario[2]}")
                return params
        if acho != True:
            print(f"Funcionario com ID {params} não encontrado.")

subMenu()
