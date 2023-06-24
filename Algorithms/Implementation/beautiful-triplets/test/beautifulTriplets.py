# A tarefa do problema "Beautiful Triplets" no HackerRank 
# é encontrar o número de sequências "bonitas" em uma lista 
# de inteiros. Uma sequência é considerada "bonita" se a diferença 
# entre seus elementos consecutivos for igual a um número fixo, 
# chamado de diferença. O problema solicita que você conte o número
# total de sequências "bonitas" possíveis na lista de entrada.

# def beautifulTriplets(d, arr):
    
#     # Variável para contar o número de sequências "bonitas"
#     contador = 0
    
#      # Percorre todos os elementos da lista
#     for i in arr:
        
#         # Verifica se existem dois elementos subsequentes 
#         # que formam uma sequência "bonita" com o elemento atual
#         if i + d in arr and i + 2 * d in arr:
            
#             # Se existir, incrementa o contador em 1
#             contador += 1
    
#     # Retorna o contador como resultado
#     return contador


# def beautifulTriplets(d, arr):
    
#     # Variável para contar o número de sequências "bonitas"
#     num = 0
    
#     # Converte a lista em um conjunto para pesquisa mais eficiente
#     s = set(arr)
    
#     # Percorre todos os elementos da lista
#     for i in arr:
        
#         # Verifica se existem dois elementos subsequentes 
#         # que formam uma sequência "bonita" com o elemento atual
#         if (i + d in s) and (i + 2 * d in s):
            
#             # Se existir, incrementa o contador em 1
#             num += 1
            
#     # Retorna o contador como resultado
#     return num



from collections import Counter


def beautifulTriplets(d, arr):
    
    # Variável para contar o número de sequências "bonitas"
    contar = 0
    
    # Cria um objeto Counter para contar a frequência de cada elemento na lista
    sequencia = Counter(arr)
    
    # Percorre todos os elementos únicos na lista
    for x in sequencia:
        
        # Verifica se existem outros dois elementos subsequentes 
        # que formam uma sequência "bonita" com o elemento atual
        if x + d in sequencia and x + d * 2 in sequencia:
            
            # Se existir, incrementa o contador multiplicando as frequências dos três elementos
            contar += sequencia[x] * sequencia[x + d] * sequencia[x + d * 2]
            
     # Retorna o contador como resultado
    return contar