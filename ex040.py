#Crie um programa que leia duas notas de um aluno e calcule sua mensagem
#no final, de acordo com a média atingida

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5 e 6.9 : RECUPERACAO
# - Média 7.0 ou superior: APROVADO


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media<5:
    print('Sua nota foi {}, você foi REPROVADO.'.format(media))
elif media >=5 and media<=6.9:
    print('Sua nota foi {}, você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua nota foi {}, você foi APROVADO.'.format(media))
