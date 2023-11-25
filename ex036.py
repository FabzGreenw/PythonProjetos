#Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exercer 30%
# do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
comprador = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos ele vai pagar? '))

valor = casa/ (anos*12)
print('Para pagar uma casa de R${:.2F} em {} anos'.format(casa, anos), end='')

print(' a prestação será de R${:.2f} '.format(valor))

if valor <= comprador*0.3:
    print('Você conseguiu o emprestimo.')
else:
    print('Empréstimo negado.')