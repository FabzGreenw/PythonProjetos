# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre
#
# A) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato
s = 0
c = 0
b = 0
nomee = ''
while True:
    nome = input('Qual o nome do produto? ')
    preco = float(input('Qual o preço do produto? '))
    s = s + preco
    if preco >1000:
        c+=1
    if b == 0 or preco <b:
        b = preco
        nomee=nome

    escolha = ' '
    while escolha not in 'SN':
     escolha = input('Quer continuar? [S/N]').strip().upper()[0]
    if escolha =='N':
        break
print(f'O total da compra foi R${s:.2f}\nTemos {c} produtos custando mais de R$1000.00\nO produto mais barato foi {nomee} que custa R${b:.2f}')
