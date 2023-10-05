# O Nim é um jogo de estratégia jogado entre dois jogadores, 
# onde há várias pilhas de pedras e, em cada turno, um jogador 
# pode remover qualquer número de pedras de uma única pilha. 
# O jogador que não consegue fazer um movimento perde o jogo.

# No "Poker Nim", o jogo tem algumas diferenças:

# Existem várias pilhas de pedras.
# Cada pilha tem um número inicial de pedras.
# Em cada turno, um jogador pode escolher uma das 
# pilhas e remover qualquer número de pedras dela, 
# mas ele deve remover pelo menos uma pedra.
# A tarefa é determinar quem ganhará o jogo se ambos 
# os jogadores jogarem de forma ótima (ou seja, 
# tentando maximizar suas chances de ganhar e 
# minimizar as chances do oponente). Você recebe 
# como entrada o número de pilhas, o número 
# inicial de pedras em cada pilha e o jogador que começa.


# # Define uma função chamada pokerNim que recebe duas 
# # listas como argumentos: k (número de pilhas) 
# # e c (número de pedras em cada pilha).

# def pokerNim(k, c):
    
#     # Inicializa uma variável 'a' para armazenar um valor acumulado.
#     a = 0
    
#     # Itera sobre a lista 'c' que contém o número de pedras em cada pilha.
#     for i in c:
        
#         # Usa a operação XOR bit a bit para acumular os valores.
#         a ^= i
        
#     # Verifica se o valor acumulado 'a' é diferente de zero.
#     if a:
        
#         # Se 'a' não for zero, o primeiro jogador ganha ('First').
#         return 'First'
    
#     # Se 'a' for zero, o segundo jogador ganha ('Second').
#     return 'Second'


from functools import reduce

def pokerNim(k, c):
    
    return 'First' if reduce(lambda x, y: x ^ y, c) else 'Second'