#Crie um programa onde 4 jogadores joguem um dado e tenham resultados
#aleatórios. Guarde esses resultados em um dicionário. No Final coloque
#esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1': randint(1,6),
             'Jogador2':randint(1,6),
             'Jogador3': randint(1,6),
             'Jogador4':randint(1,6)}
ranking = dict()

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('RANKING DOS JOGADORES:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#é um resultado em forma de lista
#se botar 0 ele vai ordenar por chave se por 1 por valor
for k,v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
