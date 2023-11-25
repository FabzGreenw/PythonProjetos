#Crie um programa que leia vários números inteiros pelo teclado.O programa
#só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles

n=0
count =0
soma = 0
while n!=999:
    n = int(input('Digite números inteiros: '))
    if n!=999:
        count+=1
        soma = soma + n

print('A quantidade de numeros digitados foi {}.'.format(count))
print('A soma entre eles foi {}.'.format(soma))

