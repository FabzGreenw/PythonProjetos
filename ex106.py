"""
Faça um mini-sistema que utilize o interactive Help do Python. O Usuário vai
digitar o comando e o manual vai aparacer. Quando o usuário digitar a
palavra 'Fim' o programa se encerrará.
OBS: use cores
"""
c = ('\033[m',  #0 - sem cores
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;42m', #2 - verde
     '\033[0;30;43m', #3 - amarelo
     '\033[0;30;44m', #4 - azul
     '\033[0;30;45m', #5 - roxo
     '\033[7;30m', #6 - Branco
     );
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[0], end='')
    help(com)
    print(c[0], end='')
def titulo(msg,cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~' *tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
comando =''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('FUNÇÃO OU BIBLIOTECA > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)