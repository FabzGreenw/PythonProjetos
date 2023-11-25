#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
#OU IMPAR.

n = int(input('Digite um número inteiro: '))

if n%2==0:
    print('o numero {}, é par'.format(n))
else:
    print('O numero {}, é impar'.format(n))
