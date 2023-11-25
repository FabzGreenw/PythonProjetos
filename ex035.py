#Desenvolva um programa que leia o comprimento de três retas e diga ao
#usuário se elas podem ou não formar um triangulo.

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            print('Podem sim formar um triangulo!')
        else:
            print('Não podem formar um triangulo!')
    else:
        print('Não podem formar um triangulo!')
else:
    print('Não podem formar um triângulo!')
