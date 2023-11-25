#Elabore um programa que calcule o valor a ser pago por um produto,
#Considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À  vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o preço do produto: '))

print('Escolha a opção de pagamento\n 1 - À vista\n 2 - À vista no cartão\n 3 - Em até 2x no cartão\n 4 - 3x ou mais no cartão ')
escolha = int(input('Digite a opção desejada: '))


if escolha == 1:
    print('O valor a ser pago é R${:.2f}.'.format(produto - produto*0.10))
elif escolha == 2:
    print('O valor a ser pago é R${:.2f}.'.format(produto - produto*0.05))
elif escolha == 3:
    print('O valor parcelado em 2x é R${:.2f}'.format(produto/2))
    print('O valor a ser pago é R${:.2f}.'.format(produto))
elif escolha ==4:
    parcelas = int(input('Quantas parcelas?'))
    print('O valor parcelado será R${:.2f}'.format((produto+produto*0.2)/parcelas))
    print('O valor a ser pago é R${:.2f}.'.format(produto+produto*0.2))
else:
    total = produto
    print('Opção INVÁLIDA de pagamento. Tente novamente!')