#Passo1
    #CRIAR UMA LISTA VAZIA ONDE IRÁ ARMAZENAR OS DADOS
dados = []
#Passo2
    #CRIAR UM LOOP ATÉ QUE O USARIO NÃO QUEIRA MAIS ADICIONAR DADOS
while True:
    # - Variveis 
    nome = input('Nome:')
    idade = int(input('Idade: '))
    cidade = input('Cidade: ')
    #CRIAR UM DICIONARIO PARA RECEBER AS CHAVES-VALOR 
    pessoas = {'Nome':nome,'Idade':idade,'Cidade':cidade}
    #ADICIONAR O DICIONARIO A LISTA VAZIA
    dados.append(pessoas) #RECEBERÁ TODOS OS DADOS QUE O USARIO IRÁ DIGITAR
    resp = ' '
    while resp not in "SN":
        resp = input('Continuar [S/N]? ').upper()
    if resp == 'N':
        break

#PASSO 3
    # - QUANTIDADE DE PESSOAS QUE FORAM CADASTRADAS
qntd = len(dados) #irá pecorrer e vai retonar a quantidade que tem dentro da lista
print('TOTAL DE PESSOAS CADASTRADA')
print(qntd)
#PASSO 4
total = [] #uma lista vazia para saber quais foram as pessoas e seus dados
for pessoas in dados:
    nomes = pessoas["Nome"]
    idades = pessoas["Idade"]
    uf = pessoas["Cidade"]
    total.append(f'Nome:{nomes} \nIdade: {idade} \nCidade:{uf}')
#LAÇO QUE IRÁ PECORRER E MOSTRARAR OS DADOS 
for info in total:
    print(info)
