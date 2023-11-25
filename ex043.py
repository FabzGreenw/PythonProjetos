#Desenvolva uma lógica que leia o PESO e ALTURA de uma pessoa, calcule seu
#IMC e mostre seus status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
from math import pow

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura '))

IMC = peso/(pow(altura,2))

if IMC<18.5:
    print('Com um IMC de {:.2f}, você está abaixo do peso.'.format(IMC))
elif IMC >=18.5 and IMC<25:
    print('Com um IMC de {:.2f}, você está no peso ideal.'.format(IMC))
elif IMC>=25 and IMC <30:
    print('Com um IMC de {:.2f}, você está no Sobrepeso.'.format(IMC))
elif IMC >=30 and IMC <40:
    print('Com um IMC de {:.2f}, você está na Obesidade.'.format(IMC))
else:
    print('Com um IMC de {:.2f}, você está na Obesidade Mórbida.'.format(IMC))