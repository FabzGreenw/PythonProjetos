#Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
from time import sleep

print('-=-'*20)
print('                         Jokenpô')
print('-=-'*20)

print('É hora de jogar!')
valor = str(input('Digite Pedra, Papel ou Tesoura: ' ))

palavra = ['Pedra', 'Papel', 'Tesoura']

escolhida = choice(palavra)

print('Validando....')
sleep(2)

print('O usuário jogou {}.'.format(valor))
print('A máquina jogou {}.'.format(escolhida))

if valor == escolhida:
    print('Empatamos com {}'.format(valor))
elif valor == 'Pedra' and escolhida == 'Tesoura':
    print('Você venceu!')
elif valor == 'Tesoura' and escolhida == 'Papel':
    print('Você venceu!')
elif valor == 'Papel' and escolhida == 'Pedra':
    print('Você venceu!')
else:
    print('Eu ganhei há!')


