print('*****Bem Vindo ao VELO DISC*****')
print()
planos = {
    "plano_iniciante": {"Velocidade": 50, "Preço": 120},
    "plano_medio": {"Velocidade": 100, "Preço": 185},
    "plano_premium": {"Velocidade": 200, "Preço": 240},
    "plano_Ultra_Plus": {"Velocidade": 400, "Preço": 350}
}

print('******PLANOS DA VELO DISC*****')
for plano, info in planos.items():
    print(f'{plano} - {info["Velocidade"]} Mbps \nR${info["Preço"]:7.2f}')

opcao = 0  # Inicializa opcao com 0 para entrar no loop
while opcao != 4:
    opcao = int(input('Escolha a opção (1/2/3/4): '))
    if opcao == 1:
        print('Você escolheu o Plano Iniciante')
    elif opcao == 2:
        print('Você escolheu o Plano Médio')
    elif opcao == 3:
        print('Você escolheu o Plano Premium')
    elif opcao == 4:
        print('Você escolheu o Plano Ultra Plus')
    else:
        print('Opção Inválida. Tente Novamente')

# Fora do loop, após o usuário escolher um plano
print('Obrigado por escolher a VELO DISC!')
