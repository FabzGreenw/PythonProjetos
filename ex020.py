#O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada

from random import shuffle

aluno01 = str(input('Digite o nome do aluno 01: '))
aluno02 = str(input('Digite o nome do aluno 02: '))
aluno03 = str(input('Digite o nome do aluno 03: '))
aluno04 = str(input('Digite o nome do aluno 04: '))

lista = [aluno01,aluno02,aluno03,aluno04]

shuffle(lista)

print('A ordem de apresentação será ')
print(lista)



