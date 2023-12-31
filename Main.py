from Fornecedor import fornecedorController
from Produto import produtosController
from Usuario import *
from Relatorios import Relatorios
import Venda



def menu():
    print("--------E-COMMERCE DE VENDAS------------")
    print("-----------MENU DE OPÇÕES-----------")
    print("(1) - Fornecedor")
    print("(2) - Produto")
    print("(3) - Cliente")
    print("(4) - Venda")
    print("(5) - Relatório")
    print('(6) - Trocar Usuário')
    print(('(7) - Finalizar Programa\n'))
    inputUsuario=int(input('Digite a opção escolhida:'))
    return inputUsuario

def subMenuFornecedor():
    while True:
        print('\n-----------FORNECEDOR-----------')
        print("(1) - Adicionar")
        print("(2) - Deletar")
        print("(3) - Listar")
        print("(4) - Editar")
        print("(5) - Menu Principal")
        oFornecedorController = fornecedorController()
        inputUsuario=int(input('Digite a opção escolhida:'))

        if inputUsuario==1:
            oFornecedorController.adicionarFornecedor()
            continue

        elif inputUsuario == 2:
            oFornecedorController.deletarFornecedor()
            continue

        elif inputUsuario == 3:
            oFornecedorController.listarFornecedores()
            continue

        elif inputUsuario == 4:
            oFornecedorController.editarFornecedor()
            continue

        elif inputUsuario == 5:
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
            oProdutoController.deletarProduto()
            continue
        elif inputUsuario == 3:
            oProdutoController.listarProdutos()
            continue
        elif inputUsuario == 4:
            oProdutoController.editarProduto()
            continue
        elif inputUsuario == 5:
            break


def subMenuCliente():
    while True:
        print('\n-----------CLIENTE-----------')
        print("(1) - Adicionar")
        print("(2) - Deletar")
        print("(3) - Listar")
        print("(4) - Editar")
        print("(5) - Menu Principal")
        inputUsuario = int(input('Digite a opção escolhida:'))
        if inputUsuario == 1:
            oClienteController.adicionarCliente()
            continue

        elif inputUsuario == 2:
            oClienteController.deletarCliente()
            continue

        elif inputUsuario == 3:
            oClienteController.listarClientes()
            continue

        elif inputUsuario == 4:
            oClienteController.editarCliente()
            continue

        elif inputUsuario == 5:
            break

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


oClienteController = usuarioController()
_usuarioLogado=oClienteController.login()

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
        subMenuCliente()
    elif inputUsuario == 4:
            Venda.subMenu()
    elif inputUsuario == 5:
        subMenuRelatório()
    elif inputUsuario == 6:
        oClienteController.login()
    elif inputUsuario == 7:
        break
    else:
        print('Opção inválida, tente novamente')
