#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200 km
# e R$0,45 para viagens mais longas

distancia = float(input('Digite a distância da viagem: '))

# if distancia <=200:
#     valor = distancia*0.5
#     print('O valor da viagem é R${}!'.format(valor))
# else:
#     valor = distancia*0.45
#     print('O valor da viagem é R${}!'.format(valor))

#simplificado
preco = distancia * 0.5 if distancia <=200 else distancia * 0.45

print('O valor da viagem é R${}!'.format(preco))