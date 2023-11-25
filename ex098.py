#Faça um programa que tenha uma função chamada contador(), que recebe
#três parâmetros: inicio, fim e passo e realize a contagem

#Seu programa tem que realizar três contagnes atráves da função criada.
#A) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep

def contador(i,f,p):

    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range (i,f,p):
            print(f'{c} ', end='')
        print('FIM!')
    elif i> f and p>0:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range (i, f-1, -p):
            print(f'{c} ', end='')
        print('FIM!')
    elif i>f and p<0:
        print(f'Contagem de {i} até {f} de {p*-1} em {p*-1}')
        for c in range(i, f-1, p):
            print(f'{c} ', end='')
        print('FIM!')
    else:
        print(f'Contagem de {i} até {f} de 1 em 1')
        for c in range (i, f-1, -1):
            print(f'{c} ', end='')
        print('FIM!')

print('-='*20)
for c in range(1, 11):
    print(f'{c} ', end='')
    sleep(0.2)
print('FIM!')

print('-='*20)
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(0.2)
print('FIM!')
print('-='*20)
print('AGORA É A SUA VEZ DE PERSONALIZAR A CONTAGEM!')
i = int(input('Início: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

contador(i,f,p)


