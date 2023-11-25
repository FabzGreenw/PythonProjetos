#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
#cosseno e tangente desse ângulo
from math import cos, tan , sin, radians
# A funções da biblioteca Math trabalham em radianos, portanto é preciso converter
angulo = float(input('Digite o angulo desejado: '))
angulorad = radians(angulo)

seno = sin(angulorad)
cosseno = cos(angulorad)
tangente = tan(angulorad)

print('O Ângulo {}º possui {:.2f} seno, {:.2f} cosseno e {:.2f} tangente'.format(angulo,seno,cosseno,tangente))
