# Neste problema, você recebe uma pilha 
# de pedras numeradas. Dois jogadores 
# jogam um jogo alternadamente. Em cada 
# turno, um jogador pode remover 2, 3 ou 5 
# pedras da pilha. O jogador que não consegue 
# fazer um movimento perde o jogo.

# A tarefa é determinar quem ganhará o jogo 
# se ambos os jogadores jogarem de forma 
# ótima (ou seja, tentando maximizar suas 
# chances de ganhar e minimizar as chances 
# do oponente). Você deve escrever uma 
# função ou programa que, dado o número 
# inicial de pedras na pilha, determine 
# se o primeiro jogador (jogador 1) ou 
# o segundo jogador (jogador 2) ganhará 
# o jogo se ambos jogarem de forma ótima.


# # Define uma função chamada gameOfStones que recebe um argumento n.
# def gameOfStones(n):
    
#     # Usa uma expressão ternária para retornar "Second" se a condição n % 7 < 2 for verdadeira,
#     # caso contrário, retorna "First".
#     return "Second" if n % 7 < 2 else "First"


# Define uma função chamada gameOfStones que recebe um argumento n.

def gameOfStones(n):
    
    # Verifica se o resultado da divisão de n por 7 é igual a 0 ou 1.
    if n % 7 == 0 or n % 7 == 1:
        
        # Se a condição for verdadeira, retorna "Second" (Segundo jogador)
        return "Second"
    
    # Se a condição não for atendida, retorna "First" (Primeiro jogador).
    return "First"