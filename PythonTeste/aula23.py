
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'infelizmente tivemos um problema que foi {erro.__class__}')
else:
    print(f'O Resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')