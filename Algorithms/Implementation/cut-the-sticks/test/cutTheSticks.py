
# O problema "Cut the Sticks" (Cortar os Pedaços) do HackerRank 
# é uma tarefa que envolve manipulação de arrays. A tarefa consiste 
# em cortar os pedaços de uma série de bastões até que todos tenham 
# um comprimento igual a zero.

# A entrada do problema consiste em um array de inteiros representando 
# os comprimentos iniciais dos bastões. Em cada iteração, deve-se determinar 
# o menor comprimento entre os bastões restantes, cortar esse valor de todos 
# os bastões e contar quantos bastões foram cortados. Esse processo se repete 
# até que todos os bastões tenham um comprimento igual a zero.

# A saída esperada é um array que contém o número de bastões cortados em cada iteração.

# Em resumo, o objetivo é implementar uma função que receba um array de comprimentos 
# de bastões e retorne um array com o número de bastões cortados em cada iteração até 
# que todos os bastões tenham sido reduzidos a zero.

# def cutTheSticks(arr):
   
#     # Inicializa a lista 'contar' com o tamanho inicial do array 'arr' 
#     contar = [len(arr)]
    
#     # Enquanto o tamanho do array 'arr' for maior que 1
#     while len(arr) > 1:
        
#         # Encontra o valor mínimo no array 'arr'
#         minimo = min(arr)
        
#         # Filtra os elementos maiores que o mínimo e atualiza o array 'arr'
#         arr = list(filter(lambda y: (y > minimo), arr))
#         arr = list(map(lambda x : x - minimo, arr))
        
#         # Adiciona o tamanho atual do array 'arr' à lista 'contar'
#         contar.append(len(arr))
        
#     # Filtra os elementos diferentes de zero na lista 'contar'
#     contar = list(filter(lambda z : (z != 0), contar))
    
#     # Retorna a lista 'contar'
#     return contar


def cutTheSticks(arr):
    
    # Inicializa uma lista vazia para armazenar os resultados
    res = []
    
    # Loop infinito até quebrar a condição
    while True:
        
        # Encontra o valor mínimo no array 'arr'
        b = min(arr)
        
        # Adiciona o tamanho atual do array 'arr' à lista 'res'
        res.append(len(arr))
        
        # Filtra os elementos diferentes do valor mínimo e atualiza o array 'arr'
        arr = [i for i in arr if i != b]
        
        # Subtrai o valor mínimo de cada elemento do array 'arr'
        arr = [x - b for x in arr]
        
        # Verifica se o array 'arr' está vazio
        if len(arr) == 0:
            
            # Se estiver vazio, encerra o loop
            break
        
    # Retorna a lista 'res' com os resultados
    return res