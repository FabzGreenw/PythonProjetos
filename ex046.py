#Faça um programa que mostre na tela uma contagem regresiva para o
#estouro de fogos de artificio, indo de 10 até 0, com um pause de 1 segundo
#entre eles
from time import sleep

for c in range (10,-1, -1):
    print('Contagem regresiva {}.'.format(c))
    sleep(1)
print('Feliz ANO NOVO!')