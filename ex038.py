#Escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n = int(input('Digite o primeiro número inteiro: '))
n2 =int(input('Digite o segundo número inteiro: '))

if n>n2:
    print('O primeiro número {} é maior que {}.'.format(n,n2))
elif n2>n:
    print('O segundo número {} é maior que {}.'.format(n2,n))
else:
    print('Não existe valor maior, os dois são iguais!')