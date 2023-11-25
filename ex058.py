#Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um
#número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar
#Mostrando quantos palpites foram necessários para vencer.
import random
from time import sleep

n: int = 0
adivinhar = 1
derrotas = 0

while n!=adivinhar:
    n = random.randint(0,10)
    print('-=-'*20)
    print('Vou pensar em número de 0 a 10. Tente adivinhar...')
    print('-=-'*20)
    adivinhar = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(2)
    if n ==adivinhar:
        print('PARABÉNS! Você conseguiu me vencer!')
    else:
        print('GANHEI! Eu pensei no número {} e não no {}!'.format(n,adivinhar))
        derrotas+=1
print('Você demorou {} tentativas, para vencer!'.format(derrotas))
