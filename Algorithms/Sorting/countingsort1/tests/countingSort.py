# A tarefa do problema "Counting Sort 1" no HackerRank 
# é implementar o algoritmo de ordenação chamado "Counting Sort" 
# para contar a frequência de ocorrência de cada elemento 
# em um array de entrada e, em seguida, retornar uma 
# lista que representa o número de ocorrências de cada elemento em ordem.

# Aqui está um resumo da tarefa:

# Você recebe um array de inteiros não ordenado.
# Sua tarefa é contar a frequência de ocorrência 
# de cada elemento no array.
# Crie uma nova lista onde cada elemento 
# representa o número de ocorrências do valor correspondente no array de entrada.

# def countingSort(arr):
    
#     # Crie uma lista chamada 'indice_classificado' 
#     # com 100 elementos inicializados com zero
#     indice_classificado = [0] * 100
    
#     # Percorra os elementos do array 'arr'
#     for i in arr:
        
#         # Aumente o valor no índice correspondente em 'indice_classificado' 
#         # para contar a frequência de ocorrência de 'i'
#         indice_classificado[i] += 1
    
#     # Retorne a lista 'indice_classificado', 
#     # que contém a contagem de ocorrências de cada elemento
#     return indice_classificado

# def countingSort(arr):
    
#     # Crie uma lista chamada 'resposta' com 100 elementos inicializados com zero
#     resposta = [0 for i in range(100)]
    
#     # Percorra os elementos do array 'arr'
#     for i in arr:
        
#         # Incremente o valor no índice correspondente em 'resposta' 
#         # para contar a frequência de ocorrência de 'i'
#         resposta[i] += 1
        
#     # Retorne a lista 'resposta', 
#     # que contém a contagem de ocorrências de cada elemento
#     return resposta

