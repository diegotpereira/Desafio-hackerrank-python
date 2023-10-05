# Dado um array inicial de inteiros 
# e um array subsequente que é gerado 
# removendo alguns elementos do array 
# inicial e reorganizando os elementos 
# restantes, você precisa determinar os 
# elementos ausentes no array subsequente.

# def missingNumbers(arr, brr):
    
#     # Cria um dicionário para armazenar 
#     # a contagem de elementos do array 'arr'
#     d = dict()
    
#     # Percorre cada elemento no array 'arr'
#     for el in arr:
        
#         # Verifica se o elemento já 
#         # existe no dicionário
#         if el  in d: 
            
#             # Se existir, incrementa a contagem desse elemento
#             d[el] += 1
            
#         else:
            
#             # Se não existir, 
#             # adiciona o elemento ao dicionário com contagem 1
#             d[el] =  1
            
#     # Cria um conjunto para armazenar os elementos ausentes 
#     # no array subsequente
#     ausente = set()
    
#     # Percorre cada elemento no array subsequente 'brr'
#     for elemento in brr:
        
#         # Verifica se o elemento não está presente 
#         # no dicionário
#         if not elemento in d:
            
#             # Se estiver ausente, 
#             # adiciona ao conjunto 'ausente'
#             ausente.add(elemento)
            
#         else:
            
#             # Verifica se a contagem do elemento 
#             # é maior ou igual a 1 no dicionário
#             if d[elemento] >= 1:
                
#                 # Se for, 
#                 # decrementa a contagem do elemento
#                 d[elemento] -= 1
                
#             else:
                
#                 # Se a contagem já for 0, 
#                 # adiciona ao conjunto 'ausente'
#                 ausente.add(elemento)

#     # Retorna os elementos ausentes em ordem crescente
#     return sorted(list(ausente))


# def missingNumbers(arr, brr):
    
#     # Cria uma lista vazia para armazenar 
#     # a resposta dos números ausentes
#     resposta = []
    
#     # Itera sobre cada elemento único no array 'brr'
#     for i in set(brr):
        
#         # Verifica se o elemento 'i' está presente no array 'arr' e 
#         # se as contagens nos arrays 'arr' e 'brr' são diferentes
#         if i in arr and arr.count(i) != brr.count(i):
            
#             # Se as condições forem atendidas, 
#             # adiciona 'i' à lista de resposta.
#             resposta.append(i)
            
#         # Verifica se o elemento 'i' não está presente no array 'arr'
#         elif i not in arr:
            
#             # Se 'i' não estiver em 'arr', 
#             # também é adicionado à lista de resposta.
#             resposta.append(i)
            
#     # Retorna a lista de resposta contendo os números 
#     # ausentes em ordem crescente
#     return sorted(resposta)

# from collections import Counter

# def missingNumbers(arr, brr):
    
#     # Cria um contador para o array 'arr'
#     conta1 = Counter(arr)
    
#     # Cria um contador para o array 'brr'
#     conta2 = Counter(brr)
    
#     # Subtrai as contagens do contador 'conta2' do contador 'conta1'
#     conta1.subtract(conta2)
    
#     # Isso resulta em um contador com as diferenças de contagem entre os elementos
    
#     # Retorna uma lista ordenada dos elementos (chaves) do contador 'conta1' onde a contagem é menor que 0.
#     # Isso corresponde aos elementos ausentes em 'brr' em relação a 'arr'.
#     return sorted((k for k, v in conta1.items() if v < 0))


def missingNumbers(arr, brr):
    
    # Itera sobre cada elemento no array 'arr'
    for elemento in arr:
        
        # Remove o elemento do array 'brr', se estiver presente.
        # Isso resulta em 'brr' contendo somente os elementos ausentes em 'arr'
        brr.remove(elemento)
        
    # Converte o array 'brr' em um conjunto para remover duplicatas,
    # depois ordena os elementos restantes em ordem crescente e retorna o resultado
    return sorted(set(brr))