#Faça um programa que leia o peso de um cinco pessoas. No Final, mostre qual foi o maior e menor peso lidos.

maior = 0
menor = 0
for c in range (1,6):
    peso = float(input('Peso da {}ª Pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi de {} KG\nO menor peso foi de {} KG'.format(maior,menor))