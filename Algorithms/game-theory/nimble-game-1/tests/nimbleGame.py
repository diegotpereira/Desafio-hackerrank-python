# O problema "Nimble Game" no HackerRank é um 
# desafio relacionado ao jogo Nimble, uma variação 
# do jogo de Nim. A tarefa é a seguinte:

# Você tem uma série de pilhas numeradas de 1 a n, 
# cada uma contendo um número diferente de pedras. 
# Em cada jogada, você pode escolher uma das pilhas 
# e mover todas as pedras daquela pilha para a direita, 
# saltando sobre qualquer número de pilhas vazias até 
# alcançar uma pilha com pedras ou sair do tabuleiro.

# O objetivo é determinar se o jogador que começa o 
# jogo pode ganhar sempre que ambos os jogadores 
# jogarem de forma ótima. Isso significa que você 
# deve escrever um programa que analise a configuração 
# atual das pilhas (ou seja, o número de pedras em cada pilha) 
# e decida se o jogador que começa pode ganhar o jogo 
# independentemente das ações do oponente.

# Esse problema envolve a aplicação de estratégias matemáticas 
# e de teoria dos jogos para determinar a estratégia 
# vencedora com base na configuração das pilhas e na 
# movimentação das pedras ao longo do tabuleiro.


# # Define a função nimbleGame que recebe uma lista chamada s como argumento

# def nimbleGame(s):
    
#     # Inicializa a variável x com zero
#     x = 0
    
#     # Itera sobre as pilhas, começando da segunda pilha (índice 1)
#     for i in range(1, len(s)):
        
#         # Verifica se o número de pedras na pilha atual (s[i]) é ímpar
#         if s[i] % 2:
            
#             # Se for ímpar, realiza a operação XOR com o índice i e atualiza o valor de x
#             x ^= i
    
#     # Retorna 'First' se x for diferente de zero, caso contrário, retorna 'Second'
#     return 'First' if x else 'Second'

# Importa a função 'reduce' do módulo 'functools'
from functools import reduce

# Define a função nimbleGame que recebe uma lista chamada s como argumento

def nimbleGame(s):
    
    # Usa a função 'reduce' para calcular o resultado da operação XOR (^)
    # sobre uma lista compreendida que contém índices i se s[i] for ímpar, caso contrário, 0.
    # A operação começa com um valor inicial de 0.
    resultado = reduce(lambda x, y: x ^ y, [i if s[i] % 2 else 0 for i in range(1, len(s))], 0)
    
    # Retorna 'First' se o resultado for diferente de zero, caso contrário, retorna 'Second'.
    return 'First' if resultado else 'Second'
