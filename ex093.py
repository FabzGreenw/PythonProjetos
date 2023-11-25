#Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou
#Depois vai ler o nome do jogador e quantas partidas ele jogou
#Depois vai ler a quantidade de gols feitos em cada partida.
#No Final, tudo isso será guardado em um dicionário incluindo o total
# de gols feitos durante o compeonato.

jogador = dict()
gols = list()
total = 0
jogador['nome']= str(input('Nome do Jogador: '))

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0,partidas):
    gol = int(input(f'Quantos gols na partida {c+1} ?'))
    gols.append(gol)
    total+=gol
jogador['gols'] = gols
jogador['total'] = total
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador Joelson jogou {partidas} partidas.')
for c in range (0, partidas):
    print(f'  =>Na partida {c+1}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
