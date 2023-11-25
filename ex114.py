"""
Crie um código em Python que teste se o site Pudim está acessivel pelo
computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except:
    print('Deu erro')
else:
    print(f'Consegui acessar {site} ')