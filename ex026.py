# Faça um programa que leia uma frase pelo teclado e mostre:

# > Quantas vezes aparece a letra 'A'.
# > Em que posição ela aparece a primeira vez
# > Em que posição ela aparece a ultima vez.

frase = input('Digite uma frase: ').upper().strip()

print("A quantidade de vezes que aparece a letra: A é {}.".format(frase.count('A')))
print('A posição que ela aparece a primeira vez é: {}.'.format(frase.find('A')+1))
print('A posição que ela aparece a ultima vez é : {}.'.format(frase.rfind('A')+1))
