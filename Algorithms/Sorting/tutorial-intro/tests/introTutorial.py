# O problema "Tutorial Intro" em HackerRank 
# é um desafio de programação que envolve a 
# busca por um elemento específico em um array 
# ordenado. A tarefa consiste em realizar as seguintes ações:

# Você recebe um número inteiro V que é o 
# valor que você precisa encontrar em um array 
# ordenado arr de números inteiros. Sua tarefa 
# é determinar o índice (a posição) em que o 
# valor V ocorre pela primeira vez no array arr.

# Para resolver o problema, você deve implementar 
# uma função chamada introTutorial que recebe o 
# valor V e o array arr como entrada e retorna o 
# índice da primeira ocorrência de V no array arr.

# A tarefa envolve a busca eficiente pelo valor V 
# no array arr, aproveitando o fato de que o array 
# está ordenado. Você deve encontrar o índice da 
# primeira ocorrência de V e retorná-lo como resultado.


# Função para encontrar o índice da primeira ocorrência do valor 'V' no array 'arr'

# def introTutorial(V, arr):
    
#     # Percorre o array 'arr' usando um loop for
#     for i in range(len(arr)):
        
#         # Verifica se o elemento em 'arr' na posição 'i' é igual a 'V'
#         if arr[i] == V:
            
#             # Se encontrado, retorna o índice 'i'
#             return i
        
#     # Se o valor 'V' não for encontrado no array, retorna -1
#     return -1
    

# # Função para encontrar o índice da primeira ocorrência do valor 'V' no array 'arr'

# def introTutorial(V, arr):
    
#     # Usando o método index() do Python para encontrar o índice da primeira ocorrência de 'V' em 'arr'
#     return arr.index(V)


# Função para encontrar o índice da primeira ocorrência do valor 'V' no array 'arr'

def introTutorial(V, arr):
    
    # Usando uma compreensão de lista para encontrar o índice da primeira ocorrência de 'V' em 'arr'
    # A compreensão de lista cria uma lista de índices onde 'valor' é igual a 'V'
    # Em seguida, o [0] final retorna o primeiro elemento dessa lista, que é o índice desejado
    return [i for i, valor in enumerate(arr) if valor == V][0]