#ANSI
#Escape sequence
#\033[0:33:44m
#Style 0 None, 1 Bold, 4 underline, 7 Negative
#text 30~37
#Teste \033[0;0;41m vermelho de fundo e cor branca
#Teste \033[4:33;44m azul de fundo e cor amarela e sublinhado
#Teste \033[1:35;43m amarelho de fundo e cor roxa
#Teste \033[30;42m cor de fundo verde e letra branca
#Teste \033[m Fundo preto e cor branca
#Teste \033[7;30m Fundo branco e cor preta

a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}'.format(a,b))

# print('\033[7;33;44mOlá, Mundo!\033[m')

