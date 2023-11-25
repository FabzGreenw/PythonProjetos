#Refaça o DESAFIO 035 dos triângulos acrescentnado o recurso de mostrar
# que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            print('Podem sim formar um triangulo!')
            if r1 == r2 and r1 == r3:
                print('O triângulo a ser formado é Equilátero!')
            elif r1 == r2 or r1 == r3 or r2 == r3:
                print("O triângulo a ser formado é o Isósceles!")
            else:
                print('O triãngulo a ser formado é o Escaleno!')
        else:
            print('Não podem formar um triangulo!')
    else:
        print('Não podem formar um triangulo!')
else:
    print('Não podem formar um triângulo!')

