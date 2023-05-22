# A tarefa do problema "The Love-Letter Mystery" no HackerRank 
# é determinar o número mínimo de operações necessárias para 
# transformar uma string em um palíndromo. Um palíndromo é uma 
# sequência de caracteres que permanece a mesma quando lida de trás para frente.

# Dada uma string composta por letras minúsculas do alfabeto, o 
# objetivo é reduzir o valor numérico de cada caractere para que a 
# string resultante seja um palíndromo. As operações permitidas são 
# reduzir o valor de um caractere em 1, ou seja, 
# transformar 'd' em 'c', 'c' em 'b', e assim por diante.

# O problema solicita que você determine o número mínimo de 
# operações necessárias para transformar a string em um palíndromo. 
# Você deve escrever uma função chamada "theLoveLetterMystery" que 
# receba a string como entrada e retorne o número mínimo de operações.


# def theLoveLetterMystery(s):
    
#     # Inicializa um contador para armazenar o 
#     # número de operações realizadas
#     contador = 0
    
#     # Verifica se a string já é um palíndromo
#     if s == s[::-1]:
        
#         # Se for um palíndromo, não é necessário fazer nenhuma operação
#         return 0 
    
#     else:
        
#         # Percorre a metade da string a partir das extremidades
#         for i in range(len(s) // 2):
            
#             # Calcula a diferença entre os valores numéricos dos caracteres simétricos
#             # na posição atual e atualiza o contador
#             contador += abs(ord(s[i]) - ord(s[::-1][i]))
            
#         # Retorna o número total de operações realizadas
#         return contador



def theLoveLetterMystery(s):
    
    # String contendo o alfabeto em ordem
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    # Calcula o valor de n que representa a metade do tamanho da string s
    n = len(s) // 2
    
    # Inicializa o contador para armazenar o número de operações realizadas
    contador = 0
    
    # Percorre a metade da string s
    for i in range(n):
        
        # Calcula a diferença entre as posições dos caracteres simétricos no alfabeto
        # e adiciona essa diferença ao contador
        contador += abs(alfabeto.index(s[-(i + 1)]) - alfabeto.index(s[i]))

    # Retorna o número total de operações realizadas        
    return contador