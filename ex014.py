#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
celsius = float(input('Informe a temperatura em ºC: '))

fahrenheit = (celsius*1.8) + 32
kelvin = celsius+273.15

print("A temperatura de {}º Celsius em Fahrenheit é {}º e em Kelvin é {}º".format(celsius,fahrenheit,kelvin))
