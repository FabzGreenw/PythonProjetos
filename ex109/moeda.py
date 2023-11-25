def metade(num=0, format=False):
    num/=2
    return num if format is False else moeda(num)

def dobro(num=0, format=False):
    num*=2
    return num

def diminuir(num=0, num2=0, format= False):

    num =num-(num*(num2/100))
    return num
def aumentar(num=0,num2=0, format=False):
    num = num+(num*(num2/100))
    return num if format is False else moeda(num)

def moeda(preco=0, moeda= 'R$'):
    return f'{moeda}{preco}'.replace('.',',')
