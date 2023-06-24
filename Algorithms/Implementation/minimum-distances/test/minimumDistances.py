# A tarefa do problema "Minimum Distances" no HackerRank é encontrar a 
# menor distância entre dois elementos repetidos em uma lista. O problema 
# fornece uma lista de números inteiros e requer que você encontre a menor 
# distância entre dois elementos iguais. A distância entre dois elementos é 
# definida como a diferença entre suas posições na lista. Se não houver elementos 
# repetidos na lista, o resultado esperado é -1.

# Em resumo, você precisa implementar a função minimumDistances(a) que recebe uma 
# lista de inteiros a e retorna a menor distância entre dois elementos repetidos. 
# Se não houver elementos repetidos, deve-se retornar -1.

# A solução envolve percorrer a lista e verificar se cada elemento aparece novamente 
# posteriormente. Caso encontre uma repetição, você deve calcular a distância entre 
# as posições desses elementos e manter um registro da menor distância encontrada.

# Ao resolver o problema, é necessário considerar a eficiência do algoritmo, já que 
# a lista pode conter até 10^3 elementos.


# def minimumDistances(a):
    
#     # Lista para armazenar as distâncias encontradas
#     l = []
    
#     for i in range(len(a)):
        
#         # Verifica se o elemento atual aparece novamente na lista
#         if a[i] in a[i + 1:]:
            
#             # Procura a próxima ocorrência do elemento
#             for j in range(i + 1, len(a)):
                
#                 # Se encontrou uma ocorrência
#                 if a[i] == a[j]:
                    
#                     # Calcula a distância entre as ocorrências e adiciona à lista
#                     l.append(j - i)
               
#     # Se encontrou distâncias na lista                    
#     if len(l) > 0:
        
#         # Retorna a menor distância encontrada
#         return min(l)
    
#     else:
        
#          # Caso contrário, retorna -1
#         return -1


# def minimumDistances(a):
    
#     # Conjunto para armazenar os elementos repetidos
#     pares = set()
    
#     # Percorre os elementos da lista
#     for i in a:
        
#         #  Verifica se o elemento ocorre exatamente duas vezes
#         if a.count(i) == 2:
            
#             # Adiciona o elemento ao conjunto de elementos repetidos
#             pares.add(i)
            
#     # Se não houver elementos repetidos
#     if not pares:
        
#         # Retorna -1
#         return -1
    
#     # Lista para armazenar as distâncias
#     distancias = []
    
#     # Percorre os elementos repetidos
#     for val in pares:
        
#         # Lista para armazenar as posições do elemento
#         indices = []
        
#         # Percorre a lista com índices
#         for i, v in enumerate(a):
            
#              # Se encontrar uma ocorrência do elemento repetido
#             if v == val:
                
#                 # Adiciona a posição à lista de índices
#                 indices.append(i)
                
#         # Calcula a distância entre as posições e adiciona à lista de distâncias
#         distancias.append(indices[-1] - indices[0])
        
#     # Retorna a menor distância encontrada
#     return min(distancias)




def minimumDistances(a):
    
    
    
    # b = [abs(i - j) for i in range(0, len(a) - 1) for j in range(i + 1, len(a)) if (a[i] == a[j])]
    
    # Cria uma lista chamada 'b' que contém a diferença absoluta entre os elementos de 'a'.
    b = [
    abs(i - j)
    
    # O primeiro loop 'for' itera pelos índices dos elementos de 'a', excluindo o último.
    for i in range(0, len(a) - 1)
    
    # O segundo loop 'for' itera pelos índices dos elementos de 'a' a 
    # partir do próximo índice do primeiro loop.
    for j in range(i + 1, len(a))
    
    # A condição 'if' verifica se os elementos correspondentes em 'a' são iguais.
    if (a[i] == a[j])
]
    
    # Retorna o valor mínimo em 'b' se 'b' tiver elementos, caso contrário, retorna -1.
    return min(b) if len(b) > 0 else -1