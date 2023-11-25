matriz = ([0,0,0],[0,0,0],[0,0,0])
par = 0
terceira = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

    # A) A soma de todos os valores pares digitados
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range (0,3):
    if matriz[l][2]:
        terceira+= matriz[l][2]
for c in range (0,3):
    if matriz[1][c]:
        if maior==0 or matriz[1][c]>maior:
            maior=matriz[1][c]

print(f'A soma de todos os valores pares são {par}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')
