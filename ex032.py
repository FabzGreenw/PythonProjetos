#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year

if ano%4==0:
    if ano%100==0:
        if ano%400==0:
            print('O ano {} é bissexto e possui 366 dias'.format(ano))
        else:
            print('O Ano {} não é um ano bissexto e possui 365 dias'.format(ano))
    else:
        print('O ano {} é bissexto e possui 366 dias'.format(ano))
else:
    print('O Ano {} não é um ano bissexto e possui 365 dias'.format(ano))


