#Escreva um programa que leia um número inteiro qulquer e epça para o usuário
#escolher qual será a base de conversão.

# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Digite um número inteiro: '))

print('Escolha uma opção:\n 1 - Para Binário\n 2 - Para Octal\n 3 - Para Hexadecimal')
escolha = int(input('Qual deseja? '))

if escolha == 1:
    print("O número {} em Binário possui o valor {}.".format(n, bin(n)))
elif escolha == 2:
    print('O número {} em Octal possui o valor {}.'.format(n, oct(n)))
else:
    print('O número {} em Hexadecimal possui o valor {}.'.format(n, hex(n)))
