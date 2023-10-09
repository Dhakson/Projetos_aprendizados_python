# Inicializa uma lista vazia para armazenar as compras
compras = []

# Loop para coletar informações sobre os produtos
while True:
    produto = input('Produto: ')
    valor = float(input('Preço: '))
    quantidade = int(input('Quantidade: '))
    
    # Cria um dicionário para representar a compra e o adiciona à lista de compras
    compra = {'Produto': produto, 'Preco': valor, 'Quantidade': quantidade}
    compras.append(compra)
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Adicionar Mais Produtos [S/N]? ').upper()
    
    if resp == 'N':
        break

# Inicializa variáveis para a quantidade total e o valor total das compras
qntd = 0
total = 0
itens = 0

# Exibe um cabeçalho para a nota fiscal
print('=' * 60)
print('{:>30}'.format('NOTA FISCAL'))
print("{:<20} {:<10} {:<15}".format("Produto", "Quantidade", "Valor total"))

# Loop para listar os produtos, suas quantidades e valores totais
for i, compra in enumerate(compras, 1):
    qntd += compra["Quantidade"]
    total_itens = compra["Preco"] * compra["Quantidade"]
    nome_produto = compra["Produto"]
    qntd_prodouto = compra["Quantidade"]
    total_compra = (f'R${total_itens:7.2f}')
    total += total_itens
    itens += qntd_prodouto
    # Exibe os detalhes da compra na nota fiscal
    print("{:<20} {:<10} {:<15} ".format(nome_produto, qntd_prodouto, total_compra))

print('{:<20}'.format("TOTAL DE ITENS ADICIONADO:"))
print('{:<20}'.format(itens))
# Exibe o valor total das compras
print('='*60)
print('{:>15}'.format('TOTAL'))
print(f'R$\033[1;91m{total:7.2f}\033[0m')
#PERGUNTA A FORMA DE PAGAMENTO QUE O CLIENTE DESEJA EFETUAR
print('''FORMA DE PAGAMENTO:
    [1] - Á VISTA 10% DE DESCONTO  
    [2] - PIX 5% DE DESCONTO
    [3] - CARTÃO DE CRÉDITO ATÉ 2X
    [4] - CARTÃO DE CREDITO 3X MAIS COM 20% DE ACRESCIMO
    [5] - SAIR  ''')
opcao = int(input('Escolha a Opção: '))
if opcao != 5:
    if opcao == 1:
        desconto = total - (total * 10 / 100)
        print(desconto)
    elif opcao == 2:
        desconto = total - (total * 5 / 100)
        print(desconto)
    elif opcao == 3:
        print('Não tem Desconto e Nem acrescimo')
    elif opcao == 4:
        parcelas = int(input('Parcelas: '))
        if parcelas >= 3:
            desconto = total + (total * 20/ 100)
            total_par = desconto / parcelas 
            print(f'R${desconto:7.2f}')
            print(f'Parcelas {parcelas} de R${total_par:.2f}')
    elif opcao == 5:
        print( )

print('VOLTE SEMPRE!')