#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 KM/H, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade >80:
    multa = (velocidade-80)*7
    print('Você foi multado, a multa vai custar R$ {}!'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')