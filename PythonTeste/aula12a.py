
nome = str(input('Qual é o seu nome? '))

if nome == 'Fabio':
    print('Que nome Bonito!')
elif nome == 'Gustavo' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome Feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
