
frase ='Curso em vídeo Python'

# print(frase[15:])
# print(frase[9::3]) #comece no 9 vai até o final, mas pule de 3 em 3

#Análise

# print(len(frase)) #mostra o tamanho de caracteres
# print(frase.count('o')) #Conta quantas vezes a palavra o aparece
# print(frase.count('o',0,13)) #vai considerar do 0 até o 12
# print(frase.find('deo')) // vai mostrar em que momento começou
# print(frase.find('Android')) #retorna -1 pq não foi encontrada
# print('Curso' in frase) #Existe o curso em frase? Retorna true

#Transformação
#Não substitui diretamente na frase e sim de uma forma secundária
# print(frase.replace('Python', 'Android')) #onde tiver python vai substituir por android
# para substituir faça frase =
# frase.upper() #Coloca todos os caracteres em maiusculo.
# frase.lower() #Coloca todos os caracteres em minusculo.
# frase.capitalize() #Joga todos os caracteres pra minusculo e so o primeiro fica em maiusculo.
# frase.title() #vai analisar quantas palavras tem na string e ele vai fazer capitalize palavra por palavra
# frase.strip() #vai remover todos os espaços inuteis do inicio e fim
# frase.rstrip() #o Lado direito vai ser tratado ( os ultimos espaços)
# frase.lstrip() # vai remover os espaços da esquerda

#Divisão
#frase.slipt() #de forma normal vai dividir em espaços

#Junção
#'-'.join(frase) #vai juntar todos os elementos e colocar o separador -.

#Para printar frases longas em linhas diferentes utilize """
#exemplo
# print("""ola
# tudo
# bem""")

# dividido = frase.split()
# print(dividido[0])





