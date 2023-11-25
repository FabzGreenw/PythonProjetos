#Escreva um programa que pergunte o salário de um funcionário e calcule
#o valor do seu aumento
#Para salários superiores a R$1250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))

if salario>1250:
    print('O seu salário com o novo aumento é R$ {}.'.format(salario*1.10))
else:
    print('O seu salário com o novo aumento é R$ {}.'.format(salario*1.15))
