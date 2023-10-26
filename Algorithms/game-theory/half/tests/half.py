# Dado um array de inteiros, 
# você deve implementar uma 
# função para calcular o valor 
# que representa a "metade" 
# desse array. A metade de um 
# array é definida da seguinte forma:

# Se o array tiver um número 
# ímpar de elementos, a "metade" 
# será o elemento central desse array.

# Se o array tiver um número par 
# de elementos, a "metade" será a 
# média dos dois elementos centrais.

# Importa a função frexp do módulo math
from math import frexp


def half(n):
    # Verifica se n é ímpar
    if n & 1:
        
        # Se for ímpar, a "metade" é 1
        return 1
    
    # Calcula o valor de x com base na representação binária de n
    x = 1 ^ int(frexp(n)[1])
    
    # Calcula o valor de y com base na representação binária de x
    y = 1 << int(frexp(x)[1] - 1)
    
    # Calcula a "metade" com base nos valores de x e y
    return 1 << y - 2 if (x ^ y) + 1 == y else (1 << y - 1) - (1 << (x ^ y)) + 1







