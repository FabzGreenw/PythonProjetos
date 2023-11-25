#Crie um programa onde o usuário possa digitar vários valores númericos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele
# não será adicionado. #No final serão exibidos todos os valores únicos
#digitados, em ordem crescente

parador = ''
lista = []
numero = 0
while parador!='N':
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('O número já existe, portanto, não será adicionado.')
    parador = str(input('Quer continuar? [S/N]')).upper().strip()

lista.sort()
print(f'Valores em ordem: {lista}')




