def metade(num=0, format=False):
    num/=2
    return num if format is False else moeda(num)

def dobro(num=0, format=False):
    num*=2
    return num if format is False else moeda(num)

def diminuir(num=0, num2=0, format= False):

    num =num-(num*(num2/100))
    return num if format is False else moeda(num)
def aumentar(num=0,num2=0, format=False):
    num = num+(num*(num2/100))
    return num if format is False else moeda(num)

def moeda(preco=0, moeda= 'R$'):
    return f'{moeda}{preco}'.replace('.',',')

def resumo(preco=0, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisando: {moeda(preco)}')
    print(f'Dobro do preço:   {dobro(preco,True)}')
    print(f'Metade do preço:  {metade(preco, True)}')
    print(f'Aumentando 10%:   {aumentar(preco,taxa,True)}')
    print(f'Diminuindo 13%:   {diminuir(preco,13, True)}')
    print('-' * 30)
