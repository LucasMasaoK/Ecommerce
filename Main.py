import Fornecedor
import Usuario
import Venda
import Produto
import Relatorios


def menu():
    print('1 - Venda')
    print('2 - Relatório')
    inputUsuario=int(input('Digite a opção escolhida:'))
    return inputUsuario

Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Mercado Livre','01.216.614/0001-78')
Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Magazine Luizo','44.714.778/0001-38')


_usuarioLogado=Usuario.login()
if _usuarioLogado:
    while True:
        inputUsuario = menu()
        if inputUsuario == 1:
            Venda.addItem()
            continue
        if inputUsuario == 2:
            Relatorios.vendasPorCliente(1)
else:
    exit()

