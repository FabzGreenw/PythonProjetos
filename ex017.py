#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento
#da hipotenusa
import math

catoposto = float (input('Digite o comprimento do cateto oposto: '))
cataadj = float (input ('Digite o comprimento do cateto adjacente: '))
#tradicional

hipotenusa = math.sqrt((math.pow(catoposto,2) + math.pow(cataadj,2)))

#com a biblioteca
# hipotenusa =math.hypot(catoposto,cataadj)

#outra forma
# hipotenusa = (catoposto ** 2 + cataadj **2) ** (1/2)


print('A Hipotenusa de um triangulo que possui o oposto de {} e adjacente de {} mede {:.2f}.'.format(catoposto,cataadj,hipotenusa));