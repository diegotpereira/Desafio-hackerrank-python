# O problema "Nim Game" no HackerRank é um desafio relacionado ao 
# jogo de Nim, um jogo de estratégia matemática. A tarefa é a seguinte:

# Você recebe várias pilhas de pedras, cada uma com um número 
# diferente de pedras. Em cada turno, um jogador pode escolher 
# uma das pilhas e remover qualquer número de pedras dessa pilha 
# (pelo menos uma pedra deve ser removida).

# O jogador que remove a última pedra das pilhas ganha o jogo.

# A tarefa específica deste problema é determinar se o jogador que 
# começa o jogo pode ganhar sempre que ambos os jogadores jogarem de 
# forma ótima. Você deve escrever um programa que analise a configuração 
# atual das pilhas (ou seja, o número de pedras em cada pilha) e decida 
# se o jogador que começa pode ganhar o jogo, independentemente das ações do oponente.


# # Define a função nimGame que recebe uma lista chamada pilha como argumento

# def nimGame(pilha):
    
#     # Itera sobre as pilhas a partir do segundo elemento (índice 1)
#     for i in range(1,len(pilha)):
        
#         # Realiza a operação XOR com o primeiro 
#         # elemento (índice 0) e a pilha atual (índice i)
#         pilha[0] ^= pilha[i]
    
#     # Verifica se o valor resultante no primeiro 
#     # elemento (índice 0) da pilha é igual a zero
#     if pilha[0] == 0:
        
#         # Se for igual a zero, o segundo jogador ganha
#         return "Second"
        
#     else:
        
#        # Se for diferente de zero, o primeiro jogador ganha
#        return "First"
    

# Define a função nimGame que recebe uma lista chamada pilha como argumento
       
def nimGame(pilha):
    
    # Inicializa a variável minima_maxima com o valor da primeira pilha
    minima_maxima = pilha[0]
    
    # Itera sobre as demais pilhas,
    for i in range(1, len(pilha)):
        
        # calculando a operação XOR com minima_maxima
        minima_maxima ^= pilha[i]
        
    # Verifica se o valor resultante de minima_maxima é igual a zero
    if minima_maxima == 0: 
        
        # Se minima_maxima for igual a zero, 
        # o segundo jogador ganha
        return "Second"
    
    else: 
        
        # Se minima_maxima for diferente de zero, 
        # o primeiro jogador ganha
        return "First"