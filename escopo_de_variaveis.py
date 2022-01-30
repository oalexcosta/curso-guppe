"""
Escopo de Variáveis
- Pode-se dizer que é a limitação ou o que está dentro de um espaço

Dois casos de escopo:

1 - Variáveis globais:
  - variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa;

2 - Variáveis locias:
  - Variávies locias são reconhecidas apenas no bloco onde  foram declaradas,
  ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica, isso signifca que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C:
int numero = 42

Exemplo em Java:
int numero = 42
"""

numero = 42   # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = "oi"
print(nao_existo)

numero = 42
novo = 0

if numero > 10:
    novo = numero + 10   # A variável 'novo' está declarada localmente dentro do bloco do if, portanto é local
    print(novo)

print(novo)

