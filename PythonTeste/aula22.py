from aula22complemento import fatorial
from aula22complemento import dobro
# def fatorial(n):
#     f=1
#     for c in range(1,n+1):
#         f*=c
#     return f
#
# def dobro(n):
#     return n * 2
#
# def triplo(n):
#     return n *3

num = int(input('Digite um valor: '))
fat= fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')