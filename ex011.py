#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintála, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

parede = largura * altura

print('Sua parede tem a dimensão de {} X {}'.format(largura,altura))
print('Para pintar uma parede de {} m², será necessário {} litros de tinta.'.format(parede, parede/2))
