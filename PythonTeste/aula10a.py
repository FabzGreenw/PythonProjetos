# tempo = int(input('Quantos anos tem seu carro?'))
# if tempo <=3:
#     print('Carro novo')
# else:
#     print('Carro velho')
#
# print('--FIM--')

#Condição simplificada (Python não tem operador ternario)
# tempo = int(input('Quantos anos tem seu carro?'))
# print('Carro novo' if tempo <=3 else 'Carro Velho')
# print('--FIM--')

# nome = str(input('Qual é seu nome? '))
# if nome =='Fabio':
#     print('Que nome lindo você tem')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))

# if m>=6.0:
#     print('Sua média foi boa! PARABÉNS!')
# else:
#     print('Sua média foi ruim! Estude MAIS!')
print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!')
