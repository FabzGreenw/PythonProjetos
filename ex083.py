#Crie um programa onde o usuário digite uma expressão qualquer que use
#parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
#parenteses abertos e fechados na ordem correta.

var = str(input('Digite a expressão: '))

lista = list()
for c in var:
    if c =='(':
        lista.append('(')

    elif c == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista)== 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')