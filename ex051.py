#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No Final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

print('{}'.format(n), end='-> ')

for c in range (1,10):
    n = n + r
    print('{}'.format(n), end='-> ')
print('ACABOU')