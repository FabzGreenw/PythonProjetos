#Faça um programa que leia o nome e peso de várias pessoas, guardando
#tudo em uma lista. No Final, mostre:



temp = []
princ = []
parador = ''
mai = men = 0
while parador!='N':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    parador = input('Quer continuar? [S/N] ').upper().strip()
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai} KG. Peso de ', end='')
for p in princ:
    if p[1]==mai:
        print(f'[{p[0]}] ', end ='')
print()
print(f'O menor peso foi de {men} KG. Peso de ', end='')
for p in princ:
    if p[1]==men:
        print(f'[{p[0]}] ', end='')