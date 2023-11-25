#Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite o seu nome completo: ')).strip()

#O nome com todas as letras maiúsculas
print(nome.upper())
#O nome com todas minúsculas.
print(nome.lower())
#Quantas letras ao todo sem considerar espaços
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#Quantas letras tem o primeiro nome.
divide = nome.split()
print(len(divide[0]))
#Quantas letras tem seu primeiro nome outra forma

print(nome.find(' '))





