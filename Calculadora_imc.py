# PASSO 1: Definir uma função para classificar o IMC de acordo com a fórmula dada
def corporal(imc):
    if imc < 16.9:
        return "Muito Abaixo do Peso"
    elif 17 <= imc < 18.4:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Normal"
    elif 25 <= imc < 29.9:
        return "Acima do Peso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 40:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

# PASSO 2: Coletar dados dos pacientes e calcular seus IMC
dados = []  # Inicializar uma lista vazia para armazenar os dados dos pacientes

# Entrar em um loop para coletar dados de vários pacientes
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = peso / (altura ** 2)  # Calcular o IMC
    classificar = corporal(imc)  # Usar a função para classificar o IMC
    pessoas = {'Nome': nome, 'Peso': peso, 'Altura': altura, 'Classificar': classificar, 'Imc': imc}
    dados.append(pessoas)  # Adicionar informações do paciente à lista

    # Perguntar ao usuário se deseja continuar
    resp = ' '
    while resp not in 'SN':
        resp = input('Continuar [S/N]:').upper()
    if resp == 'N':
        break

# PASSO 3: Apresentar os resultados dos IMC dos pacientes
total = []  # Inicializar uma lista vazia para armazenar os resultados formatados

# Loop para formatar os resultados
for pessoas in dados:
    nome = pessoas["Nome"]
    peso = pessoas["Peso"]
    altura = pessoas["Altura"]
    classificar = pessoas["Classificar"]
    imc = pessoas["Imc"]
    total.append(f'Nome: {nome} \nPeso: {peso:7.2f}Kg \nAltura: {altura:5.2f}m \nImc: {imc:7.2f}\nClassificação: {classificar}')

#PASSO 4: Imprimir os resultados formatados na tela

qntd = 0
for info, i in enumerate(total, 1):
    print(f'Paciente º{info}')
    print(i)
    qntd += 1
