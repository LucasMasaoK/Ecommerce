import Produto

def addItem():
    sair = False
    precoTotal = 0
    while sair!=True:
        Produto.mostrarProdutos()
        idProduto=int(input('Digite o ID do produto:'))
        if Produto.localizaProduto(idProduto)>0:
            qtde = int(input('Digite a quantidade:'))
            precoUnid = Produto.precoProduto(idProduto)
            precoItemTotal = qtde * precoUnid
            precoTotal = precoTotal + precoItemTotal
            vendasItensTemp.append((idProduto, qtde, precoUnid, precoItemTotal))
            print(f'Produto adicionado a venda com sucesso!')
        print(f'1- Adicionar Mais itens\n'
                        f'2- Ver itens da venda\n'
              f'3 - Fechar venda')
        escolha = int(input('Digite a opção escolhida:'))
        if escolha == 1:
            continue
        elif escolha == 2:
            print(f'Itens da venda')
            print(vendasItensTemp)
            continue
        elif escolha == 3:
            numeroVenda=GerarIDVenda()#cliente
            vendasItens.append((numeroVenda, idProduto, qtde, precoUnid, precoItemTotal))
            vendas.append((numeroVenda, 1, vendasItensTemp, precoTotal))
            print('Venda finalizada com sucesso')
            print(f'{numeroVenda}, {1}, {vendasItensTemp}, {precoTotal}')
            log(numeroVenda, 1, vendasItensTemp, precoTotal)
            break

def log(numeroVenda,cliente,vendasItens,precoTotal):
    log=open('log.txt','w')
    log.write(f'Numero da venda:{numeroVenda} Cliente:{cliente}, Itens da venda: {vendasItens}, Preco Total: {precoTotal}\n')
    log.close()


def GerarIDVenda():
    return len(vendas)

vendasItens=[]
vendasItensTemp=[]
vendas = []
