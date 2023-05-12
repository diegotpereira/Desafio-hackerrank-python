# A tarefa do problema "Jumping on the Clouds" 
# é determinar o número mínimo de saltos necessários 
# para chegar à última nuvem em um jogo. O jogador 
# começa na primeira nuvem e pode pular para a próxima 
# nuvem adjacente (índice +1) ou para a nuvem após a 
# próxima (índice +2), desde que essas nuvens sejam 
# seguras (marcadas como 0). Algumas nuvens são perigosas 
# (marcadas como 1) e não devem ser puladas. O objetivo 
# é encontrar a quantidade mínima de saltos necessários 
# para chegar à última nuvem.

# O problema fornece uma matriz que representa as nuvens, 
# onde cada elemento da matriz é 0 ou 1, indicando se a 
# nuvem é segura ou perigosa, respectivamente. O jogador 
# começa na primeira nuvem (índice 0) e deve chegar à 
# última nuvem (índice final da matriz). A tarefa é implementar 
# uma função que retorne o número mínimo de saltos necessários.

# def jumpingOnClouds(c):
    
#     # Variável para contar o número de pulos
#     pulos = 0
    
#     # Variável para armazenar o índice atual da nuvem
#     i = 0
    
#     # Iterar enquanto o índice atual for menor que o 
#     # tamanho da sequência de nuvens
#     while i < len(c):
        
#         # Verificar se é possível pular 2 nuvens à frente 
#         # e se a próxima nuvem é segura (0)
#         if i + 2 < len(c) and c[i + 2] == 0 :
            
#             # Saltar 2 nuvens à frente
#             i += 2
            
#         else:
            
#             # Caso contrário, saltar apenas 1 nuvem à frente
#             i += 1
            
#         # Incrementar o contador de pulos
#         pulos += 1
        
#     # Retornar o número de pulos, 
#     # subtraindo 1 para descontar o último salto desnecessário
#     return pulos - 1


def jumpingOnClouds(c):
    
    # Variável para armazenar a posição atual do jogador
    posicao = 0
    
    # Variável para contar o número de pulos
    contador = 0
    
    # Laço principal para realizar os pulos
    while True:
        
        # Verificar se a próxima nuvem 
        # é a última do percurso ao pular uma nuvem à frente
        if posicao + 1 == len(c) - 1:
            
            # Incrementar o contador 
            contador += 1
            
            # e encerrar o loop
            break
        
        # Verificar se a próxima nuvem é a última 
        # do percurso ao pular duas nuvens à frente
        elif posicao + 2 == len(c) - 1:
            
            # Incrementar o contador 
            contador += 1 
            
            # e encerrar o loop
            break
        
        # Verificar se é possível pular duas nuvens à frente 
        # e se a próxima nuvem é segura (0)
        if c[posicao + 2] == 0:
            
            # Atualizar a posição para pular duas nuvens à frente
            posicao += 2
            
            # Incrementar o contador de pulos
            contador += 1
            
        else:
            
            # Atualizar a posição para pular uma nuvem à frente
            posicao += 1
            
            # Incrementar o contador de pulos
            contador += 1
            
    # Retornar o número de pulos
    return contador