#Crie uma tupla preenchida com os 20 primeiros colocados da tabelado do
# campeonato brasileiro de futebol. Depois mostre:
#
# a) APENAS OS 5 primeiros colocados
# b) os últimos 4 colocados da tabela
# c0 uma lista com os times em ordem alfabética
# d) em que posição na tabela está o time do chapecoense

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'América-MG', 'Sport', 'Vitória', 'Paraná')

print(times[0:5])
print(times[16:20])
print(sorted(times))

for cont in range (0, len(times)):
    if times[cont]=='Chapecoense':
        print(f'Chapecoense está na posição {cont+1}')
    