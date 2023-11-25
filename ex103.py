"""
Faça um programa que tenha uma função chamada ficha(), que receba
dois parametros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, o mesmo que algum
dado não tenha sido informado corretamente.
"""

def ficha(nome='', gols=0):
    if nome=='':
        nome = '<desconhecido>'


    return f'O jogador {nome} fez {gols} gols(s) no campeonato.'

print('-'*30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de GOLS: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(ficha(nome,gols))
