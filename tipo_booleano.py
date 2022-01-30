"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constantes: verdadeiro ou falso

True -> verdadeiro
False -> falso

OBS: Sempre com a inicial maiúscula

Errado: true, false
Certo: True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma ação binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiro.

True and True -> True
Ture and False -> False
False and True -> False
False and False -> False
"""

