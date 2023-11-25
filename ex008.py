#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n = float(input('Digite o valor em metros: '))
quilometro=n/1000
hectometro = n/100
decametro = n/10
decimetro = n*10
centimetros = n * 100
milimetros = n * 1000

print('Quilometro: {} \nHectometro: {} \nDecametro: {} \nDecimetro:{} \nCentimetros: {} \nMilimetros : {}'.format(quilometro, hectometro, decametro, decimetro, centimetros, milimetros))
