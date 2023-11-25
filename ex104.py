"""
Crie um programa que tenha a função leiaint(), que vai funcionar de forma
semelhante à função input() do python, só que fazendo a validação para
aceitar apenas um valor númerico.
"""

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')