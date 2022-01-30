"""
Tipo Float

-Também conhecido como Tipo Real ou Tipo Decimal

Cas as decimais

OBS: O separador de casas decimais na programação é um ponto e não uma vírgula
"""

# Errado do ponto de vista do float, mas gera uma dupla

valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista do float

valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j


