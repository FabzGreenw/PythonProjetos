#Faça um programa que leia 5 valores números e guarde-os em uma lista.
#No Final, mostre qual foi o maior e o menor valor digitado e as suas
#respectivas posições na lista.
lista = list()
pmaior = 0
pmenor = 0
for c in range (0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

maior = max(lista)
minimo = min(lista)

for c, v in enumerate(lista):
    if v==maior:
        pmaior=c
    if v==minimo:
        pmenor=c
print(lista)
print(f'O valor {maior} maior está na posição {pmaior}.')
print(f'O valor {minimo} menor está na posição {pmenor}.')