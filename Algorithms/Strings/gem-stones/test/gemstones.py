# A tarefa do problema disponível no link fornecido 
# é conhecida como "Gem Stones" no HackerRank. O objetivo 
# desse problema é determinar o número de gemas que são 
# comuns a todas as rochas fornecidas em uma lista.

# Dada uma lista de rochas, representadas como cadeias 
# de caracteres contendo letras minúsculas, o problema 
# solicita encontrar o número de caracteres que ocorrem 
# em todas as rochas. Em outras palavras, a tarefa é identificar 
# os caracteres que estão presentes em todas as rochas da lista.

# A solução para esse problema envolve a utilização de conjuntos 
# (sets) para rastrear os caracteres únicos em cada rocha e, 
# em seguida, encontrar a interseção (elementos comuns) entre 
# esses conjuntos. O tamanho da interseção é a resposta final, 
# indicando o número de gemas.


# def gemstones(arr):
    
#     # Inicializa o conjunto de gemas com 
#     # os caracteres da primeira rocha
#     gem = set(arr[0])
    
#     # Itera a partir da segunda rocha até a última
#     for i in range(1, len(arr)):
        
#         # Faz a interseção entre o conjunto de 
#         # gemas e o conjunto de caracteres da rocha atual
#         gem &= set(arr[i])
        
#     # Retorna o tamanho do conjunto de gemas comuns
#     return len(gem)


# def gemstones(arr):
    
#     # Inicializa o contador
#     contador = 0
    
#     # Inicializa a lista soma com os caracteres 
#     # únicos da primeira rocha
#     soma = list(set(arr[0]))
    
#     # Itera sobre os caracteres únicos da primeira rocha
#     for i in range(0, len(soma)):
        
#          # Itera sobre as rochas restantes
#         for j in range(1, len(arr)):
            
#             # Verifica se o caractere atual não 
#             # está presente em alguma rocha
#             if soma[i] not in arr[j]:
                
#                 # Incrementa o contador e sai do loop interno
#                 contador += 1
                
#                 break
            
#         # Imprime o caractere atual e o contador
#         print(soma[i], contador)

#     # Retorna o tamanho da lista soma subtraído do contador        
#     return len(soma) - contador
        
        
# def gemstones(arr):
    
#     # Inicializa o índice i como 0
#     i = 0
    
#     # Inicializa o conjunto s com os caracteres da primeira rocha
#     s = set(arr[0])
    
#     # Enquanto i não for o índice da última rocha
#     while i != len(arr) - 1:
        
#         # Faz a interseção entre o conjunto s 
#         # e o conjunto de caracteres da próxima rocha
#         s = set(s).intersection(set(arr[i + 1]))
        
#         # Incrementa o índice i
#         i += 1

#     # Retorna o tamanho do conjunto s
#     return len(s)
        
        
def gemstones(arr):
    
    # Inicializa o conjunto string1 com os caracteres da primeira rocha
    string1 = set(arr[0])
    
    # Itera sobre cada elemento (rocha) em arr
    for i in arr:
        
        string1 = string1 & set(i)
        
    return len(string1)