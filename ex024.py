# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo.

cidade = (input('Digite o nome da cidade: ')).strip()

div = cidade.split()

print('SANTO' in div[0].upper())

# Outra forma
print(cidade[:5].upper() == 'SANTO')
