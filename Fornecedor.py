def CadastroFornecedor():
    nome=input('Digite o nome do Fornecedor:')
    cnpj=input('Digite o CNPJ:')
    fornecedores.append((GerarIDFornecedor(),nome,cnpj))
    return print(f'O {nome} foi cadastrado com sucesso!')

def GerarIDFornecedor():
    return len(fornecedores)

def AcessarFornecedor(idFornecedor):
    for i in range(0,len(fornecedores)):
       listaFornecedor=list(fornecedores[i])
       print(listaFornecedor)
       for fornecedor in fornecedores:
          codigo,nome,cnpj=fornecedor
          if idFornecedor==codigo:
            return cnpj

fornecedores=[]
fornecedores.append(('0','Padrão','00000000000'))

