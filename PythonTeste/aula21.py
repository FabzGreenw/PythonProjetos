# def contador(i,f,p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: sem retorno
#     Funçáo criada por Fabio
#     """
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c += p
#     print('Fim!')
# contador(0,100,10)
# help(contador)
#
# def somar(a=0,b=0,c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: o primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3,5)

# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1}')
#
# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}')
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n%2==0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')