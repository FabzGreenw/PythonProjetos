#Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira
from math import trunc


numero = float(input('Digite qualquer número com ponto: '))

porcaointeira = trunc(numero)

print("O valor do número foi {} e a sua porção inteira é {}.".format(numero,porcaointeira))
#podemos usar a função int para trazer somente o inteiro

