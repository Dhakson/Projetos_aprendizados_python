#PASSO 1
    #DEFINIR OS PLANOS,VELOCIDADES E PREÇOS DA INTERNT
planos = {"Plano_Iniciante":{"Velocidade":100, "Preço":50},
          "Plano_Intermediario":{"Velocidade":150, "Preço": 150},
          "Plano_Master":{"Velocidade":200, "Preço":200}
}

#PASSO 2 MOSTRAR OS PLANOS OFERECIDO 
print('*****Bem Vindo à DISC NET*****')
print('Planos Oferecidos:')
for plano, info in planos.items():
    print( )
    plano_int = plano
    velo = info["Velocidade"]
    precos = info["Preço"]
    print(f'{plano_int} \nVelocidade {velo}Mbps \nValor R${precos:7.2f}')
#PASSO 3 FAZ O USUARIO ESCOLHER A OPÇÃO
print( )
opcao = 0
while opcao != 4:
    print('ESCOLHA O PLANO QUE COMBINA COM VOCÊ')
    print('[1] - Plano Iniciante \n[2] - Plano Intermediario \n[3] - Plano Master \n[4] - SAIR')
    opcao = int(input('Opção: '))
    if opcao == 1 :
        print('Bem vindo ao Plano Iniciante')
        print('Aqui a sua Conexão é Garantida!')
        break
    elif opcao == 2:
        print('Bem vindo ao Plano Intermediario')
        print('Aqui a sua Conexão é Garantida!')
        break
    elif opcao == 3:
        print('Bem vindo ao Plano Master')
        print('Aqui a sua Conexão é Garantida!')
        break
    else:
        if opcao == 4:
            print('Finalizando o Programa')
            break
        else:
            print('Opção Invalida. Escolha uma Opção',end=' ')

print('DISC NET Agradece pela Preferencia')