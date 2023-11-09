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

def removerFornecedor():
    idFornecedor=int(input('Digite o ID do Fornecedor:'))
    for i in range(0,len(fornecedores)):
       listaFornecedor=list(fornecedores[i])
       for fornecedor in fornecedores:
          codigo,nome,cnpj=fornecedor
          if codigo==idFornecedor:
            fornecedores.remove(idFornecedor)

def listarFornecedor():
    print(fornecedores)


fornecedores=[]
fornecedores.append(('0','Padrão','00000000000'))
fornecedores.append((GerarIDFornecedor(),'Mercado Livre','01.216.614/0001-78'))
fornecedores.append((GerarIDFornecedor(),'Magazine Luizo','44.714.778/0001-38'))
fornecedores.append((GerarIDFornecedor(),'Max Steel','45.714.778/0001-38'))

