# O problema "A Chessboard Game" no 
# HackerRank é um problema de teoria 
# dos jogos. A tarefa consiste em um 
# jogo em um tabuleiro de xadrez infinito, 
# onde duas pessoas jogam alternadamente. 
# Cada jogador pode mover uma peça de xadrez "cavalo" 
# para uma nova posição de acordo com as 
# regras do movimento de cavalo no xadrez. 
# O tabuleiro é numerado de forma que cada 
# célula tem coordenadas (i, j), onde i e j 
# são números inteiros não negativos.

# A posição inicial é definida como (0, 0). 
# O objetivo é determinar quem ganhará o jogo, 
# assumindo que ambos os jogadores jogam de forma otimizada.

# O jogador 1 começa o jogo. Em cada rodada, 
# um jogador move o cavalo da posição atual 
# para uma das posições possíveis de acordo 
# com as regras do movimento do cavalo. Se 
# um jogador não puder fazer um movimento 
# válido, ele perde o jogo. Os jogadores 
# jogam alternadamente até que alguém 
# não consiga fazer um movimento válido.

# A determinação do vencedor é feita da seguinte forma:

# Se um jogador chegar a uma posição com coordenadas (i, j) onde i e j são ambos pares, o jogador ganha.
# Se um jogador chegar a uma posição com coordenadas (i, j) onde i e j são ambos ímpares, o jogador ganha.
# Caso contrário, o jogo continua.


# # Função que determina o vencedor de um jogo de tabuleiro
# # onde os jogadores movem um cavalo de xadrez em um tabuleiro infinito.

# def chessboardGame(x, y):
    
#     # Se as coordenadas (x, y) estiverem em um dos seguintes casos:
#     # 1. x % 4 = 1 ou x % 4 = 2
#     # 2. y % 4 = 1 ou y % 4 = 2
#     # Então, o jogador atual (First) ganha o jogo.
#     # Caso contrário, o jogador oposto (Second) ganha o jogo
#     return 'Second' if 0 < x % 4 < 3 and 0 < y % 4 < 3 else 'First'


# # Função que determina o vencedor de um jogo de tabuleiro
# # onde os jogadores movem um cavalo de xadrez em um tabuleiro infinito.

# def chessboardGame(x, y):
    
#     # Reduz as coordenadas (x, y) para o intervalo [0, 3]
#     # usando o operador de módulo para simplificar a lógica.
#     x = x % 4
#     y = y % 4
    
#     # Se uma das coordenadas (x ou y) for igual a 3 ou 0,
#     # então o jogador atual (First) ganha o jogo.
#     # Caso contrário, o jogador oposto (Second) ganha o jogo.
#     return 'First' if x == 3 or x == 0 or y == 3 or y == 0 else 'Second'


# Função que determina o vencedor de um jogo de tabuleiro
# onde os jogadores movem um cavalo de xadrez em um tabuleiro infinito.

def chessboardGame(x, y):
     
    # Verifica se as coordenadas (x, y) estão em uma das seguintes situações:
    # 1. x % 4 é igual a 1 ou 2
    # 2. y % 4 é igual a 1 ou 2
    if ((x % 4 == 1 or x % 4 == 2) and (y  % 4 == 1 or y == 2)):
        
        # Se as coordenadas estiverem em uma dessas situações, 
        # o jogador atual (Second) ganha o jogo.
        return 'Second'
    
    else:
        
        # Caso contrário, 
        # o jogador oposto (First) ganha o jogo.
        return 'First'