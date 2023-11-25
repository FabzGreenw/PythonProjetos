#Crie um programa onde o usuário possa digitar cinco valores númericos e
#cadastre-os em uma lista, ja na posição correta de inserção(sem usar o sort()).

#No final, mostre a lista ordenada na tela.

lista = list()
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c==0 or n > lista[-1]: #Se n for o primeiro ou maior que o ultimo elemento
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): #Enquanto pos for menor que a quantidade de elementos na lista faça
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}')


