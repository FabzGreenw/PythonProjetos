#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

# if n1>n2 and n1>n3:
#     print('O maior número é {}.'.format(n1))
#     if n2>n3:
#         print('O menor número é {}'.format(n3))
#     else:
#         print('O menor número é {}'.format(n2))
# elif n2>n1 and n2>n3:
#     print('O maior número é {}.'.format(n2))
#     if n1>n3:
#         print('O menor número é {}'.format(n3))
#     else:
#         print('O menor número é {}'.format(n1))
# elif n3>n1 and n3>n2:
#     print('O maior número é {}'.format(n3))
#     if n1>n2:
#         print('O menor número é {}'.format(n2))
#     else:
#         print('O menor número {}'.format(n1))

#Verificando quem é menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


