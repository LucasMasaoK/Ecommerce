import Venda

def vendasPorCliente(idCliente):
    vendasTupla=Venda.vendas
    vendasList=[]
    for i in range(0,len(vendasTupla)):
        vendasList.append(list(vendasTupla[i]))
        if idCliente in vendasList[i]:
            for venda in vendasList:
                numeroVenda,cliente, vendasItensTemp, precoTotal=venda
                print(f'{numeroVenda},{cliente}, {vendasItensTemp}, {precoTotal}\n')


