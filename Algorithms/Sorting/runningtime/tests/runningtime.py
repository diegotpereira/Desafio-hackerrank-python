# A tarefa do problema "Running Time of Algorithms" no 
# HackerRank é calcular o número de movimentos ou trocas 
# necessárias para ordenar um array usando o algoritmo 
# de ordenação de inserção (Insertion Sort). O desafio 
# é determinar o número de deslocamentos que ocorrem 
# quando você insere um elemento em seu lugar apropriado 
# durante o processo de ordenação.

# Aqui está um resumo da tarefa:

# Você recebe um array de inteiros desordenados.
# Sua tarefa é implementar o algoritmo de ordenação de 
# inserção para ordenar o array.
# Enquanto você ordena o array, você deve contar o número 
# de movimentos ou deslocamentos realizados para inserir 
# um elemento em seu local apropriado.
# Imprima o número total de movimentos realizados 
# durante a ordenação.

# def runningtime(arr):
    
#     # Inicializa uma variável para contar o número de trocas
#     trocas = 0
    
#     # Loop através dos elementos do array, a partir do segundo elemento (índice 1)
#     for i in range(1, len(arr)):
        
#         # Loop através dos elementos anteriores a arr[i]
#         for j in range(i):
            
#             # Verifica se o elemento atual é menor que o elemento anterior
#             if arr[i - j] < arr[i - j - 1]:
                
#                 # Troca os elementos adjacentes para ordenar o array
#                 arr[i - j], arr[i - j - 1] = arr[i - j - 1], arr[i - j]
                
#                 # Incrementa o contador de trocas
#                 trocas += 1
    
#     # Retorna o número total de trocas realizadas durante a ordenação
#     return trocas

# def runningtime(arr):
    
#     # Inicializa uma variável para contar o número de trocas
#     trocas = 0
    
#     # Loop através dos elementos do array, a partir do segundo elemento (índice 1)
#     for i in range(1, len(arr)):
        
#         # Armazena o elemento atual em uma variável temporária
#         tmp = arr[i]
        
#         # Loop reverso através dos elementos anteriores a arr[i]
#         for j in range(i - 1, -1, -1):
            
#             # Verifica se o elemento atual é maior que o elemento temporário
#             if arr[j] > tmp:
                
#                 # Incrementa o contador de trocas
#                 trocas += 1
                
#                 # Move o elemento anterior uma posição à direita
#                 arr[j + 1] = arr[j]
                
#             else:
                
#                 # Insere o elemento temporário na posição correta e sai do loop
#                 arr[j + 1] = tmp
                
#                 break 
            
#         else:
            
#             # Se o loop for concluído sem encontrar um elemento maior, 
#             # insere o elemento temporário no início do array
#             arr[0] = tmp
            
#     # Retorna o número total de trocas realizadas durante a ordenação
#     return trocas

def runningtime(arr):
    
    # Obtém o tamanho do array
    tamanho_array = len(arr)
    
    # Inicializa uma variável para contar o número de trocas
    trocas = 0
    
    # Loop através dos elementos do array, a partir do segundo elemento (índice 1)
    for elemento in range(1, tamanho_array):
        
        # Inicializa um índice para comparar o elemento atual com os elementos anteriores
        comparador = elemento - 1
        
        # Armazena o elemento atual em uma variável 'tmp'
        tmp = arr[elemento]
        
        # Enquanto 'j' for maior ou igual a 0 e o elemento anterior for maior que a 'tmp'
        while comparador >= 0 and arr[comparador] > tmp:
            
            # Incrementa o contador de trocas
            trocas += 1
            
            # Move o elemento anterior uma posição à direita
            arr[comparador + 1] = arr[comparador]
            
            # Decrementa 'comparador' para verificar o próximo elemento à esquerda
            comparador -= 1
            
        # Insere a 'tmp' na posição correta no array
        arr[comparador + 1] = tmp
        
    # Retorna o número total de trocas realizadas durante a ordenação
    return trocas