# O problema "Misère Nim" no HackerRank é uma variação 
# do jogo Nim, um jogo de estratégia matemática. A tarefa é a seguinte:

# Você tem várias pilhas de pedras. Cada pilha tem um 
# número diferente de pedras. Em cada turno, um jogador 
# pode escolher uma das pilhas e remover qualquer número 
# de pedras dessa pilha (pelo menos uma pedra deve ser removida).

# O jogador que remove a última pedra das pilhas ganha o jogo.

# No entanto, a reviravolta neste problema é que ele é 
# jogado de acordo com as regras do "Misère Nim". No Nim 
# tradicional, o jogador que remove a última pedra ganha. 
# No Misère Nim, o jogador que remove a última pedra perde.

# Você deve escrever um programa que determine quem ganha o 
# jogo de acordo com as regras do Misère Nim, considerando 
# a configuração atual das pilhas.

# O programa receberá as informações sobre o número de 
# pilhas e o número de pedras em cada pilha e deverá 
# decidir se o jogador que começa ganha ou perde o jogo, 
# supondo que ambos os jogadores joguem de forma ótima.

# Define a função misereNim que recebe uma lista s como argumento

from functools import reduce

def misereNim(s):
    
    # Calcula o número de pilhas (comprimento da lista s) e atribui a n
    n = len(s)
    
    # Verifica se o conjunto s contém apenas o número 1 e se n é ímpar
    if (set(s) == { 1 }) and n % 2 == 1:
        
        # Se as condições acima forem atendidas, o segundo jogador ganha
        return 'Second'
    
    # Verifica se o conjunto s contém apenas o número 1 e se n é par
    elif (set(s) == { 1}) and n % 2 == 0:
        
        # Se as condições acima forem atendidas, o primeiro jogador ganha
        return 'First'
    
    # Verifica se a operação XOR (ou exclusivo) entre todos os 
    # elementos da lista s é diferente de zero
    elif reduce((lambda x, y: x ^ y), s):
        
        # Se a condição acima for atendida, 
        # o primeiro jogador ganha
        return 'First'
    
    else:
        
        # Se nenhuma das condições acima for atendida, 
        # o segundo jogador ganha
        return 'Second'