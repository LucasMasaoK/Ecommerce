import Produto
import datetime
import Usuario

def addItem():
        Produto.mostrarProdutos()
        idProduto=int(input('Digite o ID do produto:'))
        if idProduto in Produto.produtos:
            qtde = int(input('Digite a quantidade: '))
            estoque= Produto.produtos[idProduto][4]
            if qtde<=estoque:
                Produto.produtos[idProduto][4]=estoque-qtde
                precoUnid = Produto.produtos[idProduto][1]
                precoItemTotal = qtde * precoUnid
                with open('comprovante.txt', 'a') as arquivocomprovante:
                    arquivocomprovante.write(f'Nome do Produto: {Produto.produtos[idProduto][0]}\n')
                    arquivocomprovante.write(f'Quantidade: {qtde}\n')
                    arquivocomprovante.write(f'Preço Total do Produto: R${precoItemTotal}\n')
                    arquivocomprovante.write('-' * 30 + '\n')  # Adiciona uma linha divisória para separar as entradas no arquivo
                print(f'Produto adicionado a venda com sucesso! \n')
            else:
                print('Não há estoque o suficiente para suprir a quantidade desejada.')
        else:
            print("Id do produto não localizado.")



def subMenu():
    addItem()
    sairSub = False
    while sairSub != True:
        print('============QUAL A OPÇÃO DESEJADA?================')
        print(f'1- Adicionar Mais itens\n'
              f'2- Ver itens da venda\n'
              f'3 - Fechar venda')
        escolha = input('Digite a opção escolhida: ')
        if escolha == "1":
            addItem()
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
            data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            email = Usuario.logado[0]
            with open('comprovante.txt', 'a') as arquivo_comprovante:
                arquivo_comprovante.write(f'Data e Hora da Venda: {data_hora_atual}\n')
                arquivo_comprovante.write(f'Preço Total da Compra: R${precoTotal}\n')
                arquivo_comprovante.write(f'Cliente: {email}\n')  # Utiliza a variável email do módulo Usuario
                arquivo_comprovante.write('-' * 30 + '\n')  # Adiciona uma linha divisória
                print('Compra finalizada com sucesso! Comprovante atualizado. \n')
            with open('comprovante.txt', 'r') as arquivo_comprovante:
                conteudo_comprovante = arquivo_comprovante.read()
                print(conteudo_comprovante)
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

precoTotal = 0.0

try:
    with open('comprovante.txt', 'w') as arquivo_comprovante:
        arquivo_comprovante.write('')
except FileNotFoundError:
    print('Arquivo comprovante.txt não encontrado.')


