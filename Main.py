from Fornecedor import fornecedorController
from Produto import produtosController
import Usuario
import Venda

import Cliente
import Relatorios

def menu():
    print("--------E-COMMERCE DE VENDAS------------")
    print("-----------MENU DE OPÇÕES-----------")
    print("(1) - Fornecedor")
    print("(2) - Produto")
    print("(3) - Cliente")
    print("(4) - Venda")
    print("(5) - Relatório")
    print('(6) - Trocar Usuário\n')
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
            fornecedorController.adicionar()
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
        print("(4) - Menu Principal")
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
            break


def subMenuCliente():
    print('\n-----------CLIENTE-----------')
    print("(1) - Adicionar")
    print("(2) - Remover")
    print("(3) - Listar")
    print("(4) - Menu Principal")
    inputUsuario = int(input('Digite a opção escolhida:'))

def subMenuVenda():
    while True:
        print('\n-----------VENDA-----------')
        print("(1) - Adicionar")
        print("(2) - Remover")
        print("(3) - Listar")
        print("(4) - Menu Principal")
        inputUsuario = int(input('Digite a opção escolhida:'))
        if inputUsuario == 1:
            Venda.subMenu()
            continue
        elif inputUsuario == 2:
            continue
        elif inputUsuario == 3:
            continue
        elif inputUsuario == 4:
            break

def subMenuRelatório():
    print("(1) - Cadastrar Produto")
    print("(2) - Mostrar Produto")
    print("(3) - Vender produto")
    print("(4) - Acessar carrinho")
    inputUsuario = int(input('Digite a opção escolhida:'))



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
        subMenuVenda()
    elif inputUsuario == 5:
        subMenuRelatório()
        Relatorios.vendasPorCliente(1)
    elif inputUsuario == 6:
        Usuario.login()
    else:
        print('Opção inválida, tente novamente')