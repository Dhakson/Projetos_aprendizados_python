lista = []
print("{:^20} {:^5} {:^20}".format("="*30,'MERCADINHO FULEIRAGEM','='*30))
print(' ')
while True:
    produto = input('Produto: ')
    valor = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))
    compras = {'Produtos':produto, 'Preço': valor, 'Quantidade':quantidade}
    lista.append(compras)
    resp = ' '
    while resp not in 'SN':
        resp = input("Adicionar Mais Produto [S/N]? ").upper()
    if resp == 'N':
        break


total = 0
qntd = 0
print("{:^20} {:^5} {:^20}".format("="*30,'NOTA FISCAL','='*30))
print("{:<20} {:<10} {:<15} {:<15}".format("Item", "Quantidade","Valor Unitario","Valor total"))
for compras in lista:
    total_itens = compras["Preço"] * compras["Quantidade"]
    total += total_itens
    produtos = compras["Produtos"]
    qntd_itens = compras ["Quantidade"]
    unit = (f'R${compras["Preço"]:7.2f}')
    total_compra = (f'R${total_itens:7.2f}')
    print("{:<20}  {:<10} {:<15} {:<15}".format(produtos,qntd_itens,unit,total_compra ))

print(' ')
print("{:^20} {:^5} {:^20}".format("="*30,'TOTAL','='*30))
print(f'R${total:7.2f}')