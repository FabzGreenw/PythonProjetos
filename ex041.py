#A Confederação Nacional de natação precisa de um programa que leia o
#ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade

# - Até 9 anos : MIRIM
# - Até 14 anos : INFANTIL
# - Até 19 anos : JUNIOR
# - Até 20 anos : SÊNIOR
# - Acima: MASTER

from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))

valor = date.today().year - nascimento

if valor <=9:
    print('Com a idade de {}, sua categoria é MIRIM.'.format(valor))
elif valor >9 and valor<=14:
    print('Com a idade de {}, sua categoria é INFANTIL.'.format(valor))
elif valor >14 and valor <=19:
    print('Com a idade de {}, sua categoria é JUNIOR.'.format(valor))
elif valor>19 and valor <=20:
    print('Com a idade de {}, sua categoria é SÊNIOR.'.format(valor))
else:
    print('Com a idade de {}, sua categoria é MASTER'.format(valor))
