# dados = list()
#
# dados.append('Pedro')
# dados.append(25)
# dados.append('Pedro')
# dados.append(25)
# dados.append('Pedro')
# dados.append(25)
# print(dados)
#
# pessoas = []
# pessoas.append(dados[:])
# print(pessoas)

#outra forma
# pessoas=[['Pedro',25],['Maria',19],['Joao',32]]
#
# print(pessoas)
# print(pessoas[0][0]) #Printa o nome Pedro
# print(pessoas[1][1]) #Printa 19
# print(pessoas[2][0]) #Printa João
# print(pessoas[1]) #Printa Maria 19
#

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0]='Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(teste)
# print(galera)

# galera =[['Joao',19],['Ana',33],['Joaquim',13],['Maria',45]]
#
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Sempre lembrar do [:] pois gera um copia
    dado.clear() #Apaga os dados cada vez que o laço roda

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
