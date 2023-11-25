#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float( input('Digite quantos reais você possui: '))

dolar = real / 4.97
euro = real / 5.34

print('Com {}, a pessoa pode comprar {:.2f} Dólares e {:.2f} Euros.'.format(real,dolar,euro))