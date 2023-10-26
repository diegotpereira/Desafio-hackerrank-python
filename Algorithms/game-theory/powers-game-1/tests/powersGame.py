# O problema "Powers Game 1" no HackerRank envolve o seguinte cenário:

# Há dois jogadores, A e B, e um único número inteiro positivo, n. Eles 
# jogam um jogo em turnos. No início, n é dado.

# Em cada rodada, o jogador atual escolhe um número inteiro x (1 <= x < n) 
# e diminui n por x, ou seja, n = n - x. O jogador que não pode fazer uma jogada válida perde o jogo.

# A tarefa é determinar quem ganhará o jogo, A ou B, se ambos jogarem de forma otimizada.

# Para resolver o problema, você precisa implementar uma função que determine o vencedor com base no valor inicial de n.

def powersGame(n):
    
    # Verifica se n é múltiplo de 8. Se for, o segundo jogador ganha.
    if n % 8 == 0:
        
        return 'Second'
    
    # Caso contrário, o primeiro jogador ganha.
    else:
        
        return 'First'
    



