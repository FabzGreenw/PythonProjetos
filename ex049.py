#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
#escolher, só que agora utilizando um laço for

print('-=-'*20)
print('                     Tabuada')
print('-=-'*20)

n = int(input('Digite o número desejado: '))

for c in range (1,11):
    print('  {} x {} = {}'.format(n, c, n * c))
print('-=-'*20)