# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

aluno01 = input('Digite o nome do aluno 01: ')
aluno02 = input('Digite o nome do aluno 02: ')
aluno03 = input('Digite o nome do aluno 03: ')
aluno04 = input('Digite o nome do aluno 04: ')

numero = random.randint(1, 4)

if numero == 1:
    print('O numero sorteado foi {} o aluno escolhido foi o(a): {}'.format(numero, aluno01))
elif numero == 2:
    print('O numero sorteado foi {} o aluno escolhido foi o(a): {}'.format(numero,aluno02))
elif numero == 3:
    print('O numero sorteado foi {} o aluno escolhido foi o (a): {}'.format(numero,aluno03))
elif numero == 4:
    print('O numero sorteado foi {} o aluno escolhido foi o (a): {}'.format(numero,aluno04))
