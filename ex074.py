#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#depois disso, mostre a listagem de núemros gerados e também indique, o menor
# e o maior valor que estão na tupla

import random

tupla = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print('Os valores sorteados foram:', end='')
for n in tupla:
    print(f' {n}', end ='')

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')