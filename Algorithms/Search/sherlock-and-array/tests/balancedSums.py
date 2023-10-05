# O problema "Sherlock and Array" no HackerRank 
# é um problema de programação que envolve encontrar 
# um elemento em um array para o qual a soma dos 
# elementos à sua esquerda seja igual à soma dos 
# elementos à sua direita. O problema é assim descrito:

# Dado um array de números inteiros não negativos, 
# você precisa determinar se existe um elemento no 
# array tal que a soma dos elementos à sua esquerda 
# é igual à soma dos elementos à sua direita. Se houver, 
# você deve retornar "YES"; caso contrário, deve retornar "NO".

# Por exemplo, considere o array [1, 2, 3]. Neste caso, 
# não existe nenhum elemento que satisfaça a condição 
# mencionada, pois não é possível encontrar um índice 
# em que a soma dos elementos à esquerda seja igual à 
# soma dos elementos à direita.

# def balancedSums(arr):
    
#     # Inicializando uma variável para 
#     # guardar a soma total dos elementos no array
#     soma_total = 0
    
#     # Calculando a soma total de todos os 
#     # elementos no array
#     for i in arr:
        
#         soma_total += i 
        
#     # Inicializando uma variável para 
#     # acompanhar a soma dos elementos à esquerda.
#     esquerda = 0
    
#     # Percorrendo o array novamente para encontrar 
#     # o ponto de equilíbrio
#     for i in arr:
        
#         # Subtraindo o elemento atual da soma total 
#         # para obter a soma dos elementos à direita.
#         soma_total -= i 
        
#         # Verificando se a soma dos elementos à esquerda 
#         # é igual à soma dos elementos à direita.
#         if esquerda ==  soma_total:
            
#             # Se encontrarmos um ponto de equilíbrio, 
#             # retornamos "YES"
#             return "YES"
        
#         # Caso contrário, adicionamos o elemento atual à 
#         # variável "esquerda" para obter a soma dos elementos 
#         # à esquerda no próximo passo.
#         esquerda += i 
        
#     # Se o loop terminar e não encontrarmos um ponto 
#     # de equilíbrio, retornamos "NO".
#     return "NO"


# def balancedSums(arr):
    
#     # Inicializando uma variável para guardar 
#     # a soma dos elementos à esquerda.
#     soma_esquerda = 0
    
#     # Calculando a soma total de todos os elementos 
#     # no array e atribuindo-a à variável "soma_direita".
#     soma_direita = sum(arr)
    
#     # Percorrendo o array utilizando o índice do elemento
#     for i in range(len(arr)):
        
#         # Subtraindo o elemento atual da soma total (soma_direita) 
#         # para obter a soma dos elementos à direita.
#         soma_direita -= arr[i]
        
#         # Verificando se a soma dos elementos à esquerda é igual à soma 
#         # dos elementos à direita.
#         if soma_esquerda == soma_direita:
            
#             # Se encontrarmos um ponto de equilíbrio, 
#             # retornamos "YES"
#             return "YES"
        
#         # Caso contrário, adicionamos o elemento atual à variável "soma_esquerda" 
#         # para obter a soma dos elementos à esquerda no próximo passo
#         soma_esquerda += arr[i]
        
#     # Se o loop terminar e não encontrarmos um ponto de equilíbrio, 
#     # retornamos "NO"
#     return "NO"


# def balancedSums(arr):
    
#     # Obtendo o tamanho do array
#     n = len(arr)
    
#     # Inicializando duas listas, uma para guardar a 
#     # soma dos elementos à esquerda e outra para a 
#     # soma dos elementos à direita.
#     esquerda = [0] * (n)
#     direita = [0] * (n)
    
#     # Calculando a soma dos elementos à esquerda e 
#     # armazenando-os na lista "esquerda"
#     for i in range(1, len(arr)):
        
#         esquerda[i] =  esquerda[i - 1] + arr[i - 1]
        
#     # Calculando a soma dos elementos à direita e 
#     # armazenando-os na lista "direita"
#     for i in range(n - 2, -1, -1):
        
#         direita[i] = direita[i + 1] + arr[i + 1]
        
#     # Percorrendo as listas "esquerda" e "direita" 
#     # para encontrar um ponto de equilíbrio
#     for i in range(len(esquerda)):
        
#         if esquerda[i] == direita[i]:
            
#             # Se encontrarmos um ponto de equilíbrio, 
#             # retornamos "YES"
#             return "YES"
#             # break
        
#     # Se o loop terminar e não encontrarmos um ponto de equilíbrio, 
#     # retornamos "NO"
#     return "NO"

def balancedSums(arr):
    
    # Calculando a soma total 
    # de todos os elementos no 
    # array e atribuindo-a à variável "total"
    total = sum(arr)
    
    # Percorrendo cada elemento do array
    for elemento in arr:
        
        # Verificando se a soma total (total) 
        # é igual ao elemento atual (elemento)
        if total == elemento:
            
            # Se encontrarmos um ponto de equilíbrio, 
            # retornamos "YES"
            return "YES"
        
        # Caso contrário, subtraímos o dobro do elemento 
        # atual da soma total (total)
        total -= elemento * 2 
        
    # Se o loop terminar e não encontrarmos um ponto de equilíbrio, 
    # retornamos "NO"
    return "NO"