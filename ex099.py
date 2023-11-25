#Faça um programa que tenha uma função maior(), que receba vários parametros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def tracinhos():
    print('-='*20)
def contador(* valores):
    tracinhos()
    print('Analisando os valores passados...')
    tam = len(valores)
    maior = 0
    for num in valores:
        print(f'{num} ', end='')
        if num>maior:
            maior = num
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
contador(2,9,4,5,7,1)
contador(4,7,0)
contador(1,2)
contador(6)
contador()