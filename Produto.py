def cadastrarProduto(idProduto,nome,preco,idFornecedor,marca):
    produtos.append((idProduto,nome,preco,idFornecedor,marca))
    return print(f'O {nome} foi cadastrado com sucesso!')

def GerarIDProduto():
    return len(produtos)

def precoProduto(RidProduto):
    for i in range(0,len(produtos)):
       listaProdutos=list(produtos[i])
       print(listaProdutos)
       for produto in produtos:
          idProduto,nome,preco,idFornecedor,marca=produto
          if int(idProduto)==RidProduto:
            return float(preco)

def localizaProduto(RidProduto):
    for i in range(0,len(produtos)):
       listaProdutos=list(produtos[i])
       print(listaProdutos)
       for produto in produtos:
          idProduto,nome,preco,idFornecedor,marca=produto
          if int(idProduto)==RidProduto:
            return int(idProduto)



produtos = []

produtos.append(('1','Padrão','150','1','Outros'))

