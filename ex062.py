#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

termo = n
cont = 1
total = 0
mais = 10
while mais!=0:
    total = total + mais
    while cont<=total:
        print('{} -> '.format(termo),end='')
        termo = termo + r
        cont = cont+1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))