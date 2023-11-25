#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre: A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma Decrescente.
#C) Se o valor 5 foi digitadoe está ou não na lista.

parador = ''
lista = []

while parador!='N':
   lista.append(int(input('Digite um número: ')))
   parador = input('Quer continuar? [S/N]').strip().upper()

#A)
print(f'A quantidade de números digitados foram {len(lista)}')
#B)
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
#C)
if 5 in lista:
    print('O número 5 foi digitado e está na lista')
else:
    print('O número 5 não foi digitado e não está na lista')