# dados = dict()
# dados = {'Nome': 'Pedro', 'Idade': 25}
#
# print(dados['Nome'])
# print(dados['Idade'])
#
# dados['Sexo']='M'
#
# print(dados)
# #dicionário para remover você usa o comando del
# del dados['Idade']
#
# print(dados)

# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'}
#
# print(filme.values()) #pega os valores
# print(filme.keys()) #pega as chaves
# print(filme.items()) #pega os dois
#
# for k, v in filme.items():
#     print(f'O {k} é {v}')
#
# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
# pessoas['peso']= '98.5'
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.items())
# for k in pessoas.values(): #Pode ser values e Keys
#     print(k)

# for k, v in pessoas.items(): #usado com o items
#     print(f'{k} = {v}')

#dicionario dentro de uma lista
# brasil = []
# estado = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'uf':'São Paulo', 'sigla':'SP'}
# brasil.append(estado)
# brasil.append(estado2)
# print(brasil[0]['uf'])

#Outra coisa
estado = dict()
brasil = list()

for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
   for v in e.values():
       print(v, end ='')
   print()
       # print(f'O campo {k} tem valor {v}')
