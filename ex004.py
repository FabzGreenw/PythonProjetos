vare: str = (input('Digite algo: ')) #Não funciona em outros tipos além de string

print('O tipo primitivo desse valor é : ', type(vare))

print('Só tem espaços ? {}'.format(vare.isspace()))
print('É um número? ', vare.isnumeric())
print('É alfabético? ', vare.isalpha())
print('É alfanumérico?', vare.isalnum())
print('Esta em maiúsculas?', vare.isupper())
print('Esta minúsculas?', vare.islower())
print('Está capitalizada?', vare.istitle())