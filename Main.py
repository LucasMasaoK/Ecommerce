from Fornecedor import fornecedorController
from Produto import produtosController
from Relatorios import Relatorios
import Usuario
import Venda
import Cliente


def menu():
    print("--------E-COMMERCE DE VENDAS------------")
    print("-----------MENU DE OPÇÕES-----------")
    print("(1) - Fornecedor")
    print("(2) - Produto")
    print("(3) - Cliente")
    print("(4) - Venda")
    print("(5) - Relatório")
    print('(6) - Trocar Usuário')
    print(('(7) - finalizar programa\n'))
    inputUsuario=int(input('Digite a opção escolhida:'))
    return inputUsuario

def subMenuFornecedor():
    while True:
        print('\n-----------FORNECEDOR-----------')
        print("(1) - Adicionar")
        print("(2) - Remover")
        print("(3) - Listar")
        print("(4) - Menu Principal")
        inputUsuario=int(input('Digite a opção escolhida:'))
        oFornecedorController = fornecedorController()
        if inputUsuario==1:
            oFornecedorController.adicionar()
        elif inputUsuario == 2:
            continue
        elif inputUsuario == 3:
            continue
        elif inputUsuario == 4:
            break
        else:
            print('Opção inválida, tente novamente')

def subMenuProduto():
    while True:
        print('\n-----------PRODUTOS-----------')
        print("(1) - Adicionar")
        print("(2) - Remover")
        print("(3) - Listar")
        print("(4) - Editar")
        print("(5) - Menu Principal")
        oProdutoController=produtosController()
        inputUsuario = int(input('Digite a opção escolhida:'))
        if inputUsuario == 1:
            oProdutoController.adicionarProduto()
            continue
        elif inputUsuario == 2:
            oProdutoController.removerProduto()
            continue
        elif inputUsuario == 3:
            oProdutoController.listarProdutos()
            continue
        elif inputUsuario == 4:
            oProdutoController.editarProduto()
            continue


def subMenuCliente():
    print('\n-----------CLIENTE-----------')
    print("(1) - Adicionar")
    print("(2) - Remover")
    print("(3) - Listar")
    print("(4) - Menu Principal")
    inputUsuario = int(input('Digite a opção escolhida:'))

def subMenuRelatório():
    while True:
        print('\n-----------RELATÓRIOS-----------')
        print("(1) - Vendas por Periodo")
        print("(2) - Vendas por Vendedor")
        print("(3) - Vender produto")
        print("(4) - Acessar carrinho")
        inputUsuario = int(input('Digite a opção escolhida:'))
        oRelatorios = Relatorios()
        if inputUsuario == 1:
            oRelatorios.vendasPorPeriodo()
            continue
        elif inputUsuario == 2:
            oRelatorios.vendasVendedor()
            continue
        elif inputUsuario == 3:
            continue
        elif inputUsuario == 4:
            break



_usuarioLogado=Usuario.login()

while True:
    if _usuarioLogado:
        inputUsuario = menu()
    else:
        exit()

    if inputUsuario==1:
        subMenuFornecedor()

    elif inputUsuario == 2:
        subMenuProduto()
    elif inputUsuario == 3:

        RidCliente = input('Digite um ID:')
        Cliente.LocalizaCliente(RidCliente)
    elif inputUsuario == 4:
        while True:
            Venda.subMenu()
            break
    elif inputUsuario == 5:
        subMenuRelatório()
    elif inputUsuario == 6:
        Usuario.login()
    elif inputUsuario == 7:
        break
    else:
        print('Opção inválida, tente novamente')
