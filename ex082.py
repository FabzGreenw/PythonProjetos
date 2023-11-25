#Crie um programa que vailer vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores
#pares e os impares digitados, respectivamente.
#Ao final mostre o conteúdo das três listas gerados.

lista = []
listp = []
listi= []
parador =''
while parador!='N':
    lista.append(int(input('Digite um valor: ')))
    parador = input('Quer continuar? [S/N] ').strip().upper()

for c in lista:
    if c%2==0:
        listp.append(c)
    elif c%2==1:
        listi.append(c)
print(f'Lista comum {lista}')
print(f'Lista par {listp}')
print(f'Lista impar{listi}')