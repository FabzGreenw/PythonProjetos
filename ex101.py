""" Crie um programa que tenha uma função chamada voto() que vai
receber como parametro o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU
OBRIGATÓRIO nas eleições
"""
from datetime import date

def voto(a):
    ano = date.today().year - a
    if ano >=16 and ano <18:
        return f'Com {ano} anos: VOTO OPCIONAL.'
    elif ano >=18 and ano <=65:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO.'
    elif ano >65:
        return f'Com {ano} anos: VOTO OPCIONAL.'
    else:
        return f'Com {ano} anos: VOTO NEGADO.'
print('-'*30)
a = int(input('Em que ano você nasceu? '))
print(voto(a))
