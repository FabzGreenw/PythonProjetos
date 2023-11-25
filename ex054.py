#Crie um programa que leia o ano de nascimento de sete pessoas.
#No Final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
#já são maiores
from datetime import date
maior = 0
menor = 0

for c in range (0,7):
    idade = int(input('Em que ano a {}ª pessoa nasceu? '.format(c+1)))
    if (date.today().year - idade) <21:
        menor = menor +1
    elif (date.today().year - idade ) >=21:
        maior = maior +1
print('Das sete pessoas\n{} são menores e {} são maiores'.format(menor,maior))