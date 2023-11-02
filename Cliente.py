def CadastrarCliente(idCliente, nomeCliente, CPF, telefone, CEP, endereco):
    clientes.append((idCliente, nomeCliente, CPF, telefone, CEP, endereco))
    return print(f'O {nomeCliente} foi cadastrado com sucesso!')

def GerarIDCliente():
    return len(clientes)

def LocalizaCliente(RidCliente):
    for i in range(0,len(clientes)):
       listaClientes=list(clientes[i])
       for cliente in clientes:
           idCliente, nomeCliente, CPF, telefone, CEP, endereco = cliente
           if idCliente==RidCliente:
            return print(idCliente, nomeCliente, CPF, telefone, CEP, endereco)

clientes = []

#INSERTS INICIAIS
clientes.append(('1', 'Jader', '153.144.230-73', '(69) 99133-3818', '78020-973 ', 'Rua Barão de Melgaço 2754',))
clientes.append(('2', 'Thiago', '728.357.020-91', '(49) 98077-6641', '78048-070', 'Rua Sófia',))
clientes.append(('3', 'Raphael', '220.243.310-41', '(98) 99541-5133', '78056-201', 'Rua das Margaridas',))
clientes.append(('4', 'Lucas', '239.351.830-46', '(73) 98969-6585', '78056-618', 'Rua H-1',))





















