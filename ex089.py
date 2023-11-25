#Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No Final, motre um boletim, contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente


lista = list()

parador = ''

while parador!='N':
    nome = str(input('Nome: '))
    Nota1 =float(input('Nota 1: '))
    Nota2 = float(input('Nota 2: '))
    media = (Nota1+Nota2)/2
    lista.append([nome, [Nota1, Nota2], media])
    parador = input('Quer continuar? [S/N] ').strip().upper()


print('-='*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    if opc ==999:
        print('FINALIZANDO...')
        break
    if opc<=len(lista)-1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')

print('<<<VOLTE SEMPRE >>>')