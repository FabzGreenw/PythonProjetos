#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

termo = n
cont = 1

while cont<=10:
    print('{} -> '.format(termo),end='')
    termo = termo + r
    cont = cont+1
print('FIM')
