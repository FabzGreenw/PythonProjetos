#Faça um programa que leia um número qualquer e mostre o seu fatorial

n = int(input('Digite o número desejado: '))
print('{}! = '.format(n),end='')
produto = 1
while n>=1:
    if n>1:
        print('{}X'.format(n),end='')
        n-=1
        produto += produto * n
    else:
        print(n,end='')
        n -=1
print('= {}'.format(produto))