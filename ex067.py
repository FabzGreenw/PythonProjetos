#Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido
#quando o núimero solicitado for negativo

n = 0
m = 0

while True:
    n = int(input('Digite um valor: '))
    if n>0:
        print('----Tabuada----')
        for c in range (1,11):
            m = n*c
            print(f'{n} X {c} = {m}')
    else:
        break
print('Programa TABUADA ENCERRADO. Volte Sempre! ')