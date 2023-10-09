# Lista vazia para armazenar os números
lista = []

# PASSO 1
# Pergunta ao usuário o número que deseja digitar
# Pergunta se o usuário quer continuar ou não
while True:
    numeros = int(input('Digite Números Inteiros: '))  # Pergunta ao usuário
    lista.append(numeros)  # Adiciona o número à lista
    resp = ' '
    while resp not in 'SN':
        resp = input('CONTINUAR [S/N]: ').upper()
    if resp == 'N':
        break

# PASSO 2
# Procura saber se o número digitado é par
# Contagem da quantidade de números pares encontrados
cont = 0
qntd = []
for i, numero in enumerate(lista):
    if numero % 2 == 0:
        cont += 1
        qntd.append(i)  # Armazena a posição do número par

# PASSO 3
# Mostra em um print a quantidade de números pares
print(f'A quantidade de números pares: {cont}')

# PASSO 4
# Mostra as posições dos números pares, considerando singular ou plural
for pos in qntd:
    if len(qntd) == 1:
        print(f'Está na Posição: {pos}')
    else:
        print(f'Estão nas Posições: {pos}')
