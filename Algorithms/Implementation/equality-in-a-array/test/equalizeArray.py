# A tarefa do problema "Equality in a Array" é encontrar 
# o número mínimo de elementos que devem ser removidos de 
# um array de inteiros de forma a tornar todos os elementos 
# restantes iguais. O objetivo é determinar o número de 
# elementos que precisam ser removidos para que o array 
# contenha o maior número possível de elementos repetidos.

# O problema solicita a implementação da função equalizeArray, 
# que recebe como parâmetro um array de inteiros arr e retorna 
# um inteiro representando o número mínimo de remoções necessárias.

# Em resumo, a tarefa é determinar a quantidade mínima de elementos 
# que devem ser removidos para que haja o maior número de elementos 
# repetidos no array resultante.

# def equalizeArray(arr):
    
#     # Retorna o comprimento do array subtraído pelo valor máximo
#     # da contagem de ocorrências de cada elemento único do array.
#     return len(arr) - max([arr.count(a) for a in set(arr)])


# from collections import Counter


# def equalizeArray(arr):
    
#     # Calcula as contagens de ocorrências de cada elemento no array usando o Counter
#     contar = Counter(arr)
    
#     # Obtém a contagem mais comum usando most_common() e acessa o primeiro elemento [0][1]
#     contagem_mais_comum = contar.most_common()[0][1]
    
#     # Retorna o comprimento do array subtraído pela contagem mais comum
#     return len(arr) - contagem_mais_comum


# def equalizeArray(arr):
    
#     # Inicializa a contagem máxima como -1
#     maxI = -1
    
#     # Itera sobre os elementos do array
#     for i in arr:
        
#         # Conta quantas vezes o elemento atual aparece no array
#         contarI = arr.count(i)
        
#         # Atualiza a contagem máxima se a contagem atual for maior
#         maxI = contarI if contarI > maxI else maxI
        
#     # Retorna a diferença entre o comprimento do array 
#     # e a contagem máxima
#     return len(arr) - maxI


# def equalizeArray(arr):
    
#     # Converte o array em um conjunto para obter elementos únicos
#     setArr = [*set(arr)]
    
#     # Lista para armazenar a contagem de ocorrências de cada elemento
#     contarArr = []
    
#     # Itera sobre os elementos únicos do array
#     for a in setArr:
        
#         # Conta o número de ocorrências do elemento no array original
#         contarArr.append(arr.count(a))
        
#     # Remove a contagem máxima de ocorrências do elemento mais frequente
#     contarArr.remove(max(contarArr))
    
#     # Retorna a soma das contagens restantes
#     return sum(contarArr)


def equalizeArray(arr):
    
    # Dicionário para armazenar a contagem de ocorrências de cada elemento
    freq = {}
    
    # percorre cada elemento x no array arr
    for x in arr:
        
        # Se o elemento já estiver presente
        if x in freq:
            
            # significa que ele já foi encontrado anteriormente no array, 
            # então incrementamos a contagem em 1
            freq[x] += 1
            
        # Caso contrário
        else: 
            
            # elemento x é novo e ainda não foi encontrado antes. 
            # Portanto, adicionamos o elemento ao dicionário freq 
            # com uma contagem inicial de 1,
            freq[x] = 1
            
    # Lista ordenada das contagens de ocorrência
    lista_frequencia = sorted(list(freq.values()))
    
    # Retorna a soma de todas as contagens, exceto a maior
    return sum(lista_frequencia[0:-1])