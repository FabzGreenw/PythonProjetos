#Listas podem ser modificadas

#lanche.insert(0,'Cachorro-Quente')

#del lanche[3]
#lanche.pop(3) geralmente usado para remover o ultimo elemento
#lanche.remove('pizza') remove pelo conteudo

# valores = list(range(4,11)) #de 4 até 10
#
# print(valores)

# valores = [8,2,5,4,9,3,0]

# valores.sort() #ordena de forma normal
# valores.sort(reverse = True) #ordena de forma reversa
# print(len(valores))

# num = [2,5,9,1]
# num [2] = 3
# num.append(7)
# num.sort(reverse= True)
# num.insert(2,2)
# # num.pop()
# # num.pop(2)
# # num.remove(2) #só elimina o primeiro valor
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 5')
# print(num)
# print(f'Esssa lista tem {len(num)} elementos')

# valores = list()
#
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista')

# a = [2,3,4,7]
# #b = a #Quando atribuimos uma lista a outra o python cria uma ligação entre elas
# b = a[:] #Dessa forma ele n cria uma ligação
# b[2]=8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')

