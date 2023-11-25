"""
Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido.
Aproveite e crite também uma função leiafloat() com a mesma funcionalidade
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n

num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um valor real: ')
print(f'O valor digitado foi {num1} e {num2}')