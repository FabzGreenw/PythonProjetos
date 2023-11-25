#Crie um programa que leia a idade e o sexo de várias pessoas. A cada
#Pessoa cadastrada o programa deverá perguntar se o usuário quer ou nõa
#continuar. No Final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

p = 0
h = 0
m = 0

while True:
    idade = int(input('Idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        p+=1
    if sexo =='M':
        h+=1
    if sexo =='F' and idade<20:
        m+=1

    resp =' '
    while resp not in 'SN':
        resp = str (input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp =='N':
        break
print(f'Total de pessoas com mais de 18 anos: {p}')
print(f'Total de homens cadastrados: {h}')
print(f'Total de mulheres com menos de 20 anos: {m}')



