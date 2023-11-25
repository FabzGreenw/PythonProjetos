#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No Final do programa, mostre:

#A média de idade do grupo.
#Qual é nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.
s = 0
maisvelho = ''
velho = 0
conta = 0
for c in range (1,5):
    print('----{}ªPessoa-----'.format(c))
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo com F ou M: ')).strip().upper()
    s = s + idade
    if idade > velho and sexo == 'M':
        velho = idade
        maisvelho = nome

    if sexo == 'F' and idade <20:
        conta = conta +1

print('A média de idade do grupo é {}.'.format(s/4))
print('O nome do homem mais velho tem {} anos e se chama {}.'.format(velho, maisvelho))
print('A quantidade de mulheres que tem menos de 20 anos é {}.'.format(conta))