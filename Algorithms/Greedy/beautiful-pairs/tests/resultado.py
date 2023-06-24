# def beautifulPairs(A, B):
    
    
#     # Armazena o comprimento de B em uma variável separada para uso posterior
#     B_len = len(B)
    
#     # Verifica cada elemento em A
#     for i in A:
        
#         # Se o elemento estiver presente em B, 
#         if i in B:
            
#             # remove-o de B
#             B.remove(i)
            
#     # Verifica se todos os elementos de B foram removidos
#     if len(B) == 0:
        
#         # Se todos os elementos de B foram removidos, retorna B_len - 1
#         return B_len - 1
    
#     # Se ainda houver elementos em B, retorna B_len - len(B) + 1
#     return B_len - len(B) + 1


# def beautifulPairs(A, B):
    
#     # Lista para armazenar os pares bonitos
#     pares = []
    
#     # Iterar sobre os elementos de A junto com seus índices
#     for i, num in enumerate(A):
        
#         # Verificar se o elemento num está presente em B
#         if num in B:
            
#             # Obter o índice do primeiro elemento num em B
#             j = B.index(num)
            
#             # Adicionar o par (índice de A, índice de B) à lista de pares
#             pares.append((i, j))
            
#             # Marcar o elemento correspondente em B como -1 para evitar duplicatas
#             B[j] = -1
            
#     # Contar o número de pares bonitos        
#     contar = len(pares)
    
#     # Verificar se existem mais elementos não pareados em A ou B
#     if contar < len(A) and contar < len(B):
        
#         # Adicionar 1 ao número de pares bonitos
#         contar += 1
        
#     # Retornar o número de pares bonitos
#     return contar
    
    
    
from collections import Counter

def beautifulPairs(A, B):
    
    # Contar as ocorrências dos elementos em A e B
    contar_a, contar_b = Counter(A), Counter(B)
    
    # Contar as ocorrências dos elementos em A que não estão em B
    contar_elementos_em_A_que_nao_em_B = contar_a - contar_b
    
    # Contar as ocorrências dos elementos em A que também estão em B
    contar_A_que_estao_em_B = contar_b & contar_a

    # Verificar se há elementos em A que não estão em B
    if sum(contar_elementos_em_A_que_nao_em_B.values()) >= 1:
        
        # Retornar a soma das ocorrências dos elementos comuns entre A e B,
        # acrescida de 1 para representar o par adicional
        return sum(contar_A_que_estao_em_B.values()) + 1
    
    # Caso contrário, retornar a soma das ocorrências dos elementos comuns entre A e B,
    # subtraída de 1 para representar a exclusão de um par
    # return contar_A_que_estao_em_B - 1
    return sum(contar_elementos_em_A_que_nao_em_B.values()) - 1