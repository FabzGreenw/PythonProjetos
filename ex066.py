#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a
#condição de parada. No Final, mostre quantos números foram digitados e qual
#foi a soma entre eles (desconsiderando o flag).
n = s = c = 0

while True:
    n = int(input('Digite um valor (999 para parar) :'))
    if n!=999:
        s += n
        c += 1
    else:
        break
print(f'Foram digitados {c} números e a soma entre eles é igual a {s}.')

