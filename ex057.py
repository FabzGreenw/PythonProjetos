#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
# if correto:
#
sexo = ''
while sexo!='F' and sexo!='M':
    sexo = str (input('Digite o seu sexo [M/F]: '))
    if sexo!='F' and sexo!='M':
        print('Valor invalido, por favor digite novamente!')
