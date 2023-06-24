# A tarefa do problema "Minimum Absolute Difference in an Array" 
# no HackerRank é encontrar a diferença absoluta mínima entre 
# quaisquer dois elementos em um array de inteiros.

# A entrada consiste em um array de inteiros, e o objetivo é 
# encontrar o valor mínimo da diferença absoluta entre dois 
# elementos distintos do array. A diferença absoluta entre dois 
# elementos é calculada como o valor absoluto da diferença entre esses elementos.

# Por exemplo, dado o array [1, 2, 3, 4], a diferença absoluta 
# mínima ocorre entre os pares (1, 2) ou (3, 4), resultando em 
# uma diferença absoluta de 1.

# A tarefa é implementar uma função que receba o array de inteiros 
# como entrada e retorne o valor mínimo da diferença absoluta entre 
# quaisquer dois elementos distintos do array. O problema pode ser 
# resolvido através de iteração sobre o array e comparando todas as 
# possíveis diferenças absolutas entre os elementos.



# def minimumAbsoluteDifference(arr):
    
#     # Ordena o array em ordem crescente.
#     arr.sort()
    
#     # Inicializa uma lista chamada mins para armazenar as diferenças absolutas.
#     mins = []
    
#     # Itera pelo índice do array, excluindo o último elemento.
#     for x in range(0, len(arr) - 1):
        
#         # Calcula a diferença absoluta entre o elemento atual e o próximo elemento,
#         # e adiciona o resultado à lista mins.
#         mins.append(abs(arr[x] - arr[x + 1]))
        
#     # Retorna o valor mínimo da lista mins, 
#     # que representa a diferença absoluta mínima 
#     # entre quaisquer dois elementos distintos do array.
#     return min(mins)

# def minimumAbsoluteDifference(arr):
    
#     # Ordena o array em ordem crescente.
#     arr = sorted(arr)
    
#     # Inicializa a variável soma com a diferença absoluta 
#     # entre o primeiro e o segundo elemento do array.
#     soma = abs(arr[0] - arr[1])
    
#     # Itera pelos índices do array, excluindo o último elemento.
#     for i in range(len(arr) - 1):
        
#         # Verifica se a diferença absoluta entre o elemento atual 
#         # e o próximo elemento é menor do que a diferença absoluta atual.
#         if soma > abs(arr[i] - arr[i + 1]):
            
#             # Atualiza a variável soma com a nova diferença absoluta mínima.
#             soma = abs(arr[i] - arr[i + 1])
            
#     # Retorna o valor mínimo da diferença absoluta 
#     # entre quaisquer dois elementos distintos do array.
#     return soma