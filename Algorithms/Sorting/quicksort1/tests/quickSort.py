# Você recebe um array de inteiros e um 
# elemento de pivô. Sua tarefa é reorganizar 
# os elementos do array de modo que todos 
# os elementos menores que o elemento de 
# pivô apareçam antes dele, seguidos pelo 
# próprio elemento de pivô e, em seguida, 
# todos os elementos maiores que o elemento de pivô.

# O algoritmo de particionamento é parte 
# essencial do algoritmo de ordenação 
# rápida (quicksort). A saída esperada 
# é o array particionado.

# def quickSort(arr):
    
#     # Inicialize duas listas vazias, 
#     # 'esquerda' e 'direita', para 
#     # armazenar elementos menores 
#     # e maiores que o elemento de pivô
#     esquerda, direita = [], []
    
#     # Percorra os elementos do array, 
#     # começando do segundo elemento (índice 1)
#     for i in range(1, len(arr)):
        
#         # Verifique se o elemento atual (arr[0]) 
#         # é maior que o elemento em arr[i]
#         if arr[0] > arr[i]:
            
#             # Se for menor, adicione-o à lista 'esquerda'
#             esquerda.append(arr[i])
            
#         else:
            
#             # Caso contrário, adicione-o à lista 'direita'
#             direita.append(arr[i])
            
#     # Adicione o elemento de pivô (arr[0]) à lista 'esquerda'
#     esquerda.append(arr[0])
    
#     # Combine as listas 'esquerda' e 'direita' para obter o array particionado
#     return esquerda + direita

def quickSort(arr):
    
    # Escolha o elemento de pivô, que é o primeiro elemento do array
    pivo = arr[0]
    
    # Inicialize três listas vazias: 'esquerda', 'direita' e 'igual' 
    # para armazenar elementos menores, maiores e iguais ao pivô
    esquerda, direita, igual = [], [], []
    
    # Inicialize uma lista vazia 'a' que será usada para construir o array particionado
    a = []
    
    # Percorra todos os elementos do array
    for i in arr:
        
        # Verifique se o elemento é igual ao pivô
        if i == pivo:
            
            # Se for igual, adicione-o à lista 'igual'
            igual.append(i)
            
        # Verifique se o elemento é menor que o pivô
        elif i < pivo:
            
            # Se for menor, adicione-o à lista 'esquerda'
            esquerda.append(i)
            
        else:
            
            # Caso contrário (o elemento é maior que o pivô), 
            # adicione-o à lista 'direita'
            direita.append(i)
            
    # Copie os elementos de 'esquerda', 'igual' e 'direita' para a lista 'a' na ordem correta
    for i in esquerda:
        
        a.append(i)
        
    for i in igual:
        
        a.append(i)
        
    for i in direita:
        
        a.append(i)
        
    # Retorna a lista 'a', que contém o array particionado
    return a