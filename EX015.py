#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o Preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

dias = int (input('Quantidade de dias alugados?'))
kmrodados = float (input('Quantos KM foram percorridos?'))


kmpreco = kmrodados*0.15
diaspreco = dias*60

total = kmpreco+diaspreco

print('O carro rodou {} KM, você terá que pagar {} R$.'.format(kmrodados,kmpreco))
print('A quantidade de dias alugado foi de {}, você terá que pagar {} R$.'.format(dias,diaspreco))
print('O valor total a ser pago é de {} R$.'.format(total))
