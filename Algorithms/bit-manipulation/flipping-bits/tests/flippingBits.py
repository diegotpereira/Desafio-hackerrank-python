# Dado um array de números inteiros não negativos, 
# sua tarefa é inverter (trocar) todos os bits de 
# cada número e retornar o array resultante.

# Em outras palavras, para cada número no array, 
# você deve inverter todos os bits, transformando 
# todos os 0s em 1s e todos os 1s em 0s na representação binária desse número.

# Para resolver o problema, você deve implementar 
# uma função que receba um array de números inteiros, 
# inverta todos os bits de cada número e retorne o array resultante.

# A operação de inversão de bits é comum em programação 
# e é frequentemente usada em tarefas de manipulação 
# de bits e processamento de dados binários. O objetivo 
# deste problema é praticar essa operação e fornecer 
# o array de saída após a inversão de bits.


# # Definindo a função 'flippingBits' com um parâmetro 'n'.

# def flippingBits(n):
    
#      # Invertendo todos os bits de 'n' subtraindo-o de 4294967295.
#     # 4294967295 é o valor máximo que pode ser representado usando 32 bits (todos os bits definidos como 1).
#     resultado = 4294967295 - n
    
#     # Retorna o resultado da inversão de bits.
#     return resultado


def flippingBits(n):
    
    # Executando a operação XOR (^) entre 'n' e o resultado da expressão (1 << 32) - 1.
    # A expressão (1 << 32) - 1 gera um número binário com 32 bits, todos definidos como 1.
    n ^= (1 << 32) - 1
    
    # Retorna o resultado da inversão de bits.
    return n