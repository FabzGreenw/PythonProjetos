#Faça um programa que leia o nome e média de um aluno, guardando também a
#situação em um dicionário. No Final, mostre o conteudo da estrutura na tela.
boletim = dict()

boletim['nome'] = str(input('Nome: '))
boletim['media']= float(input('Média: '))

if boletim['media']<6:
    boletim['situacao'] = 'Reprovado'
else:
    boletim['situacao'] = 'Aprovado'

for k,v in boletim.items():
    print(f'{k} é igual a {v}')