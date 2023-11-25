#Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o prmeiro e o ultimo nome separadamente.

nome = input('Digite o seu nome completo: ')

div = nome.split()
var = len(div)

print('Primeiro nome é:{} .'.format(div[0]))
print('Ultimo nome é:{}'.format(div[var-1]))
