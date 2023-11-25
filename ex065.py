##Crie um programa que leia vários números digitados inteiros pelo teclado.
#No FInal da execução, msotre a média entre todos os valores e qual foi o maior
# e menor valores lidos.O programa deve perguntar ao usuário se ele quer ou não
#continuar a digitar valores.

count = 0
soma = 0
boll = ''
n = 0
maior = 0
menor = 0
while boll!='N':
    n = int(input('Digite um número: '))
    soma = soma + n
    count+=1
    if maior ==0 and menor ==0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    boll = input('Deseja continuar [S/N] ? ').upper()

print('A média entre todos os valores foi {}.'.format(soma/count))
print('O maior foi {} e o menor {}.'.format(maior,menor))

