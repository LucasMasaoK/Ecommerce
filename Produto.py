produtos = {
    1: ['Padrão', 150.00,1, 'Outros', 100],
    2: ['Memoria RAM DDR3 8GB', 150.00, 1, 'Outros', 50],
    3: ['Memoria RAM DDR3 16GB', 250.00, 1, 'Outros', 30]
}

def cadastrarProduto():
    proximo_id = max(produtos.keys()) + 1
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    idFornecedor = input("Digite o ID do fornecedor: ")
    marca = input("Digite a marca do produto: ")
    estoque = int(input("Digite a quantidade em estoque: "))

    produtos[proximo_id] = [nome, preco, idFornecedor, marca, estoque]
    print(f'O {nome} foi cadastrado com sucesso!')


def mostrarProdutos():
    for idProduto, produto_info in produtos.items():
        print(f'ID:{idProduto} - Descrição:{produtos[idProduto][0]} - Preço:R${produtos[idProduto][1]} - Id Fornecedor:{produtos[idProduto][2]} - Marca:{produtos[idProduto][3]} - Estoque:{produtos[idProduto][4]}')

def editarProdutos():
    while True:
        print('\n1 - Criar produtos')
        print('2 - Editar produtos')
        print('3 - Listar produtos')
        print("4 - Menu Principal")
        opcao = input('Dgite a opção desejada: ')
        if opcao == '1':
            cadastrarProduto()
        elif opcao == '2':
            mostrarProdutos()
            id = int(input('Digite o produto que deseja editar: '))
            if id <= max(produtos.keys()):
                while True:
                    print('1 - Nome do Produto')
                    print('2 - Preço do Produto')
                    print('3 - Id do Fornecedor do Produto')
                    print('4 - Marca do Produto')
                    print('5 - Estoque do Produto')
                    print('6 - Apagar o produto')
                    print('s - Sair da tela de edição')
                    opcao = input('Digite a opção que deseja modificar: ')
                    if opcao == "1":
                        nome = input('Digite o novo nome do produto: ')
                        produtos[id][0] = nome
                        print(f'O produto {nome} foi atualizado com sucesso')
                    elif opcao == "2":
                        preco = float(input('Digite o novo preço do produto'))
                        produtos[id][1] = preco
                        print(f'O produto {produtos[id][0]} teve seu preço alterado com sucesso')
                    elif opcao == "3":
                        idFornecedor = int(input('Digite o id do fornecedor do produto'))
                        produtos[id][2] = idFornecedor
                        print(f'O id do fornecedor do {produtos[id][0]} foi alterado com sucesso')
                    elif opcao == "4":
                        marca = input('Digite a nova marca do produto: ')
                        produtos[id][3] = marca
                        print(f'a marca do {produtos[id][0]} foi mudado para {marca}')
                    elif opcao == "5":
                        estoque = int(input('Digite o novo estoque do produto'))
                        produtos[id][4] = estoque
                        print(f'O estoque do {produtos[id][0]} foi alterado para {estoque}')
                    elif opcao == "6":
                        rem = int(input('Digite o id do produto que deseja apagar: '))
                        del produtos[rem]
                    elif opcao == "s":
                        mostrarProdutos()
                        break
                    else:
                        print('Opção inválida, por favor, tente novamente')
            else:
                print('Id inválido, por favor, tente novamente')
                editarProdutos()
        elif opcao == "3":
            mostrarProdutos()
        elif opcao == "4":
            break
