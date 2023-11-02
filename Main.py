import Fornecedor
import Usuario
import Venda
import Produto
import Cliente

def menu():
    print('1 - Venda')
    inputUsuario=int(input('Digite a opção escolhida:'))
    return inputUsuario

Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Mercado Livre','01.216.614/0001-78')
Fornecedor.CadastroFornecedor(Fornecedor.GerarIDFornecedor(),'Magazine Luizo','44.714.778/0001-38')


_usuarioLogado=Usuario.login()


if _usuarioLogado:
    inputUsuario = menu()
else:
    exit()

if inputUsuario==1:
    Venda.addItem()

elif inputUsuario == 2:
    # idCliente = len(Clientes.GerarIDCliente())
    # nomeCliente = input('Digite so nome do cliente:')
    # CPF = input(f'{nomeCliente} digite seu CPF:')
    # telefone = input(f'{nomeCliente} digite seu CPF:')
    # CEP = input(f'{nomeCliente} digite seu CEP:')
    # endereco = input(f'{nomeCliente} digite seu Endereço:')
    # Clientes.CadastrarCliente(idCliente, nomeCliente, CPF, telefone, CEP, endereco)
    # listaClientes = Clientes.clientes
    # print(listaClientes)
    RidCliente = input('Digite um ID:')
    Clientes.LocalizaCliente(RidCliente)