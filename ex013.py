#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o salário do funcionário: '))

novo = salario + (salario* 15/100)

print('Um funcionário que ganhava {}, com um reajuste de 15% irá receber o novo salário de {:.2f} reais.'.format(salario, novo))
