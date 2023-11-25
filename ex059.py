# crie um programa que leia dois valores e mostre um menu na tela
# [1] Somar
# [2] Multiplicar
# [3] maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep


n = int(input('Digite o primeiro valor: '))
n2 = int (input('Digite o segundo valor: '))
opcao = 0
while opcao!=5:
    opcao=int(input('Escolha a opção desejada.\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\nOpção: '))

    if opcao==1:
        print('A Soma é: {}'.format(n+n2))
    elif opcao==2:
        print('O produto é: {}'.format(n*n2))
    elif opcao==3:
        if n>n2:
            print('O maior é: {}'.format(n))
        elif n2 > n:
            print('O maior é: {}'.format(n2))
        else:
            print('Os dois são {} portanto não há maior.'.format(n))
    elif opcao ==4:
        print('Digite os novos números')
        n = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao ==5:
        print('Saindo do programa...')
        sleep(2)
    else:
        print("Opção invalida, digite novamente.")
