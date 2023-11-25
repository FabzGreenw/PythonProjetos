#Escreva um programa que faça o computador "Pensar" em um número inteiro
# entre a 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador
#O programa deverá escrever na tla se o usuário venceu ou perdeu.

import random
from time import sleep
n = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
adivinhar = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)
if n ==adivinhar:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número 0 {} e não no {}!'.format(n,adivinhar))

