#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float (input('Digite o preço do produto: '))

novo = preco - (preco *5/100)

print('O produto que custava {}, o novo preço do produto com 5% de desconto é {:.2f} reais'.format(preco,novo))
