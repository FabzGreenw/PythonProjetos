#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))

dobro = n*2
triplo = n*3
raiz = n**(1/2)


print('O dobro é {}\nO triplo é {}\nA raiz é {:.2f}'.format(dobro,triplo, raiz))

n1= pow(n,(1/2)) #Outra forma de fazer a raiz

print('A raiz é {:.2f}'.format(n1));