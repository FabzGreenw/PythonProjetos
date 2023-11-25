#Crie um programa aonde o usuário possa digitar sete valores númericos
#e cadastre-os em uma lista única que mantenha separados os valores pares
#e impares. No Final, mostre os valores pares e impares em ordem crescente.

lista= ([], [])

for c in range (0,7):
    n = int(input(f'Digite o {c+1}º número: '))

    if n%2==0:
        lista[0].append(n)
    elif n%2==1:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')

