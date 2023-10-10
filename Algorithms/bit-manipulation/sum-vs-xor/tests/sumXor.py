# A tarefa do problema "Sum vs XOR" no HackerRank é a seguinte:

# Dado um número não negativo n, a tarefa é calcular e retornar 
# o número de valores inteiros não negativos x, onde 0 <= x <= n, 
# que satisfazem a seguinte condição:

# n + x = n XOR x

# Em outras palavras, você deve encontrar quantos valores inteiros 
# não negativos x podem ser adicionados a n para que o resultado 
# da soma seja igual ao resultado da operação XOR entre n e x.

# A operação XOR (ou exclusivo ou) retorna 1 quando exatamente um 
# dos bits de entrada é 1. Portanto, a tarefa é encontrar quantos 
# valores de x podem ser adicionados a n de forma que os bits 
# correspondentes de n e x sejam diferentes 
# (ou seja, um deles é 0 e o outro é 1) em todas as posições.


# # Importando o módulo 'math' para usar a função 'floor'.

# import math

# # Definindo a função 'sumXor' com um parâmetro 'n'.
# def sumXor(n):
    
#     # Inicializando uma variável 'contador' para contar os zeros finais em 'n'.
#     contador = 0
    
#     # Loop enquanto 'n' for maior que 0.
#     while n > 0:
        
#         # Verificando se o bit menos significativo de 'n' é 0 (par).
#         if n % 2 == 0:
            
#             # Incrementando o contador quando o bit é 0.
#             contador += 1
            
#         # Dividindo 'n' por 2 e arredondando para baixo para continuar verificando o próximo bit.
#         n = math.floor(n / 2)
    
#     # Calculando 2 elevado à potência do contador e retornando o resultado.
#     return 2 ** contador



def sumXor(n):
    
    # Verificando se 'n' é igual a 0.
    # Converte 'n' em sua representação binária como uma string, conta o número de dígitos '0' na string
    # e calcula 2 elevado à potência desse número de '0's.
    # Caso 'n' seja igual a 0, o resultado é 1.
    # Retorna o resultado final.
    return 2 ** format(n, 'b').count('0') if n else 1