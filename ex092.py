#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#cadastre-os com idade) em um dicionário se for acaso a CTPS for diferente
#de zero. O dicionário receberá também o ano de contratação e o salário.
#Cálcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
import datetime
from datetime import date
dados = {}

dados['nome']=str(input('Nome:'))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = (date.today().year)-nascimento
print(dados['idade'])
dados['CDT'] = int(input('Carteira de trabalho: (0 não tem)'))

if dados['CDT']!=0:
    dados['contrato']=int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade']+((dados['contrato'] +35) - date.today().year)

    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')


