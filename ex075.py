#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No Final, mostre:
# A) Quantas vezes apareceu o valor 9.
# b) em que posição foi digitado o primeiro valor 3;
# c) Quais foram os números pares.

num = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))

print(f'o Numero 9 apareceu {num.count(9)} vezes ')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Numeros pares:', end = '')
for c in num:
    if c%2==0:
        print(f' {c}', end ='')

