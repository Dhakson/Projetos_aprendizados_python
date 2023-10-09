# Importa o módulo 'date' da biblioteca 'datetime' para calcular a idade com base no ano atual

from datetime import date

# Inicializa uma lista vazia para armazenar informações sobre as pessoas

pessoas = []

# Loop infinito para coletar informações sobre as pessoas

while True:
    nome = input('Nome: ')  # Pergunta o nome do usuário
    nasc = int(input('Ano de Nascimento: '))  # Pergunta o ano de nascimento
    idade = date.today().year - nasc  # Calcula a idade com base no ano atual
    
    # Cria um dicionário com as informações da pessoa e adiciona à lista de pessoas
    pessoa = {
        'Nome': nome,
        'Ano de Nascimento': nasc,
        'Idade': idade
    }
    pessoas.append(pessoa)
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer Adicionar mais alguém [S/N]: ').upper()
    
    if resp == 'N':
        break

# Loop para imprimir informações sobre as pessoas e determinar a situação de alistamento

for pessoa in pessoas:
    if pessoa['Idade'] < 18:
        print(f'Olá, {pessoa["Nome"]}, você nasceu em {pessoa["Ano de Nascimento"]} e tem {pessoa["Idade"]} anos.')
        print('Não precisa se alistar.')
    elif 18 <= pessoa['Idade'] < 22:
        print(f'Olá, {pessoa["Nome"]}, você nasceu em {pessoa["Ano de Nascimento"]} e tem {pessoa["Idade"]} anos.')
        print('Precisa se alistar.')
    else:
        print(f'Olá, {pessoa["Nome"]}, você nasceu em {pessoa["Ano de Nascimento"]} e tem {pessoa["Idade"]} anos.')
        print('Precisa regularizar a sua situação em uma Junta Militar.')
