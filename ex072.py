#Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até
# Seu programa deverá ler um número pelo teclado(entre 0 e 20 e mostrá-lo. por extenso)

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
numero = int(input('Digite um número de 0 a 20: '))
for cont in range(0,len(tupla)):
    if cont==numero:
        print(f'O seu número por extenso é {tupla[cont]}. ')
