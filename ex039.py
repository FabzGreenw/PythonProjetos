#Faça um programa que leia o ano de nascimento de um jovem e informe, de
#acordo com sua idade
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))

alistar = (date.today().year) - nascimento

if alistar <18:
   print('Faltam {} anos para se alistar.'.format(18-alistar))
elif alistar == 18:
    print('Ja é hora de se alistar!')
else:
    print('Ja passou da hora de se alistar, você está atrasado {} anos!'.format(alistar-18))