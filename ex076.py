#Crie um programa que tenha uma Tupla única com nomes de produtos e seus
#respectivos preços na sequencia.
#No final, mostre uma listagem de preços, organizando os dados em forma
#tubular

listagem = ('Lápis', 1.75,
            'Borracha,2',2,
            'Caderno', 15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso', 9.9,
            'Mochila', 120.32,
            'Canetas',22.30,
            'Livro',34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for item in range (0, len(listagem)):
    if item%2==0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>1.2f}')
print('-'*40)