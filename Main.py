import Fornecedor
import Usuario
import Venda
import Produto



def menu():
    print('1 - Comprar')
    print('2 - Produtos')
    print('4 - Relatório')
    print('5 - Criar Fornecedor')
    print('6 - Trocar Usuário')
    inputUsuario=int(input('Digite a opção escolhida: '))
    return inputUsuario

Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Mercado Livre','01.216.614/0001-78')
Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Magazine Luizo','44.714.778/0001-38')
Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Max Steel','45.714.778/0001-38')

_usuarioLogado=Usuario.login()


if _usuarioLogado:
    while True:
        inputUsuario = menu()
        if inputUsuario == 1:
            Venda.addItem()
            continue
        elif inputUsuario == 2:
            Produto.editarProdutos()
        elif inputUsuario == 5:
            nome_fornecedor = input("Digite o nome do fornecedor: ")
            cnpj = input("Digite o CNPJ do fornecedor: ")
            Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(), nome_fornecedor, cnpj)
        elif inputUsuario == 6:
            Usuario.login()
else:
    exit()
