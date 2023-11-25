#Faça um programa que jogue par ou impar com o computador. O jogo será
#Interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
#que ele conquistou no final do jogo

import random

variavel = ['PAR','IMPAR']
computador = random.choice(variavel)
numero = random.randint(1,10)
escolha = ''
v = 0
s = 0
while True:

    numeropessoa = int(input('Digite um número de 1 a 10: '))
    s = numeropessoa + numero

    if computador == 'PAR':
        print('O computador escolheu PAR, portanto você ficou com impar')
        escolha = 'IMPAR'
    else:
        escolha = 'PAR'
        print('O computador escolheu IMPAR, portanto você ficou com PAR')

    if s%2==0 and escolha =='PAR':
        print(f'Parabéns você venceu o número {s} é PAR')
        v+=1
    elif s%2==1 and escolha =='IMPAR':
        print(f'Parabéns você venceu o numero {s} é IMPAR')
        v+=1
    else:
        print(f'Você perdeu, o número {s} é {computador}')
        break
print(f'A quantidade de vitórias consecutivas conquistadas foi de {v}.')
