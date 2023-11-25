#Faça um programa que tenha uma lista chamada números e duas funções
#chamada sorteia() e somapar(). A primeira funçao vai sortear 5 números e vai
#colocá-los dentro da lista e a segunda função vai mostrar a soma entre
#todos os valores pares sorteados pela função anterior.
from random import randint
def somapar(lista):
    soma=0
    print(f'Somando os valores pares de {lista}, ', end='')
    for c in lista:
        if c%2==0:
            soma+=c
    print(f'temos {soma}')
def sorteia():
    lista=list()
    print('Sorteando os 5 valores da lista ', end='')
    lista =[randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
    for c in lista:
        print(f'{c} ', end='')
    print('PRONTO!')
    somapar(lista)
sorteia()

