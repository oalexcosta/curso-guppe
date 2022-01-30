"""
Tipo String

Em Python um dado é considerado do tipo string sempre que:

- estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- estiver entre aspas duplas triplas -> descrito abaixo pra nao dar erro
"""
# estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie' -> \n serve para separar por linhas(enter)
print(nome)
print(type(nome))

nome = 'Angelina \" Jolie' -> \ serve para manter as aspas
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) -> transforma em uma lisa de strings

print(nome[0:4])   # Slice de string

print(nome[5:15])  # Slice de string

# [  0,     1]
# ['Geek', 'Univerity']
print(nome.split()[0])

print(nome.split()[1])
"""
# [ 0 ,  1,   2,   3,   4,   5,   6,   7,   8,  9,   10,   11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'

"""
[::-1]  -> começe do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1])  # Inversão da String em Pythônico

print(nome.replace('e', 'i'))

print(type(nome))

texto = 'socorram me subino onibus marrocos' #palindromo
print(texto)

print(texto[::-1])

nome = 'ana'  #palindromo
print(nome)

print(nome[::-1])

