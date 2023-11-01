import Venda

def vendasPorCliente(idCliente):
    vendasTupla=Venda.vendas
    vendasList=[]
    for i in range(0,len(vendasTupla)):
        vendasList.append(list(Venda.vendas[i]))
        if idCliente in vendasList:
            for venda in Venda.vendas[i]:
                numeroVenda,cliente, vendasItensTemp, precoTotal=venda
                print(f'{numeroVenda},{cliente}, {vendasItensTemp}, {precoTotal}')


