"""
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
 - A situação opcional
 Adicione também as docstrings da função.
"""

#Programa principal
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >=7:
            r['Situação'] = 'Boa'
        elif r['média'] >=5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r

resp = notas(5.5, 2.5,5.5, sit=True)
print(resp)