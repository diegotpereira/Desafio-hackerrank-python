# A tarefa do problema "Two Arrays" no HackerRank envolve a seguinte situação:

# Você tem duas listas de números inteiros, A e B, ambas contendo N elementos. 
# Você também tem um valor inteiro K.

# A tarefa específica é determinar se é possível rearranjar os elementos de ambas 
# as listas de forma que, para cada elemento em A, exista um elemento correspondente
# em B, de modo que a soma dos elementos correspondentes em ambas as listas seja pelo menos igual a K.

# Em resumo, o problema "Two Arrays" requer que você verifique se é possível rearranjar 
# os elementos das duas listas de forma que a soma dos elementos correspondentes seja 
# pelo menos igual a um valor K especificado. Isso envolve a combinação de elementos 
# das duas listas em pares para atender ao requisito da soma mínima K.

# def twoArrays(k, A, B):
    
#     # Ordene a lista A em ordem crescente 
#     A.sort()
    
#     # Ordene a lista B em ordem decrescente
#     B.sort(reverse=True)
    
#     # Percorra os elementos das listas A e B em pares
#     for i in range(len(A)):
        
#         # Verifique se a soma dos elementos correspondentes é menor que k
#         if A[i] + B[i] < k:
            
#             # Se for, 
#             # retorne 'NO' indicando que não é possível rearranjar os elementos
#             return 'NO'
        
#     # Se não houver nenhum par de elementos cuja soma seja menor que k, 
#     # retorne 'YES'
#     return 'YES'


def twoArrays(k, A, B):

    # Verifique se a lista A, ordenada, é maior ou igual à lista B com cada elemento subtraído de k, ordenada
    # Se a condição for verdadeira, retorne 'YES', caso contrário, retorne 'NO'
    return 'YES' if (sorted(A) >= sorted([k - b for b in B])) else 'NO'