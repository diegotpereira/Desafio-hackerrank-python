# Dada uma matriz de números inteiros e 
# um número inteiro k, determine a maior 
# permutação possível da matriz após no 
# máximo k trocas.

# Uma permutação da matriz é uma reordenação 
# dos elementos. Por exemplo, a matriz [1, 2, 3] 
# após uma permutação pode se tornar [2, 1, 3].

# def largestPermutation(k, arr):
    
#     # Obtém o tamanho da matriz
#     n = len(arr)
    
#     # Cria um dicionário para armazenar o índice de cada elemento na matriz
#     d = {arr[i] : i for i in range(n)}
    
#     # Percorre a matriz
#     for i in range(n):
        
#         # Verifica se o número máximo de trocas já foi alcançado
#         if k == 0:
            
#             break 
        
#         # Verifica se o elemento atual já está na posição correta
#         if arr[i] == n - i:
            
#             continue 
        
#         # Obtém o índice do elemento que deve estar na posição atual
#         j = d[n - i]
        
#         # Troca os elementos nas posições i e j
#         arr[i], arr[j] = arr[j], arr[i]
        
#         # Atualiza os índices dos elementos trocados no dicionário
#         d[arr[i]], d[arr[j]] = i, j
        
#         # Decrementa o contador de trocas restantes
#         k -= 1
    
#     # Retorna a matriz após as trocas
#     return arr


# # Definindo uma função chamada largestPermutation 
# # que recebe dois parâmetros: k e arr

# def largestPermutation(k, arr):
    
#     # Criando uma lista rev_arr que é uma 
#     # versão ordenada em ordem decrescente da lista arr
#     rev_arr = sorted(arr, reverse=True)
    
#     # Verificando se k é maior ou igual 
#     # ao tamanho de arr ou se arr é igual a rev_arr
#     if k >= len(arr) or arr == rev_arr:
        
#         # Se qualquer uma das condições acima for verdadeira, 
#         # retornamos a lista rev_arr
#         return rev_arr
    
#     # Criando um dicionário dic_idx onde as chaves 
#     # são os valores em arr e os valores são os índices correspondentes
#     dic_idx = { v: k for k, v in enumerate(arr)}
    
#     # Inicializando as variáveis i e contador com 0
#     i, contador = 0, 0
    
#     # Iniciando um loop while que continuará 
#     # até i ser menor que o tamanho de arr
#     while i < len(arr):
        
#         # Verificando se o valor em rev_arr na 
#         # posição i não é igual ao valor em arr na posição i
#         if rev_arr[i] != arr[i]:
            
#             # Se forem diferentes, obtenha a posição do 
#             # valor rev_arr[i] no dicionário dic_idx
#             pos = dic_idx.get(rev_arr[i])
            
#             # Atualize o dicionário dic_idx para refletir 
#             # a nova posição dos valores envolvidos na troca
#             dic_idx[arr[i]] = pos 
#             dic_idx[arr[pos]] = i 
            
#             # Realize a troca dos valores em arr nas posições i e pos
#             arr[i], arr[pos] = arr[pos], arr[i]
            
#             # Incrementando o contador de trocas
#             contador += 1
            
#             # Verificando se o contador de trocas 
#             # atingiu ou ultrapassou o valor de k
#             if contador >= k:
                
#                 # Se sim, saia do loop
#                 break 
            
#         # Incrementando o valor de i para 
#         # continuar para a próxima posição em arr.
#         i += 1
        
#     # Retornando a lista arr após todas as trocas
#     return arr
    

# Definindo uma função chamada largestPermutation que 
# recebe dois parâmetros: numero_maximos_trocas e arr

def largestPermutation(numero_maximos_trocas, arr):
    
    # Inicializando a variável 
    # trocas com 0 para contar as trocas
    trocas = 0
    
    # Inicializando a variável i 
    # com 0 para rastrear a posição atual no array
    i = 0
    
    # Obtendo o tamanho da lista arr 
    # e armazenando-o na variável n
    n = len(arr)
    
    # Iniciando um loop while que continuará 
    # até o número de trocas atingir o limite máximo
    while trocas < numero_maximos_trocas:
        
        # Verificando se i alcançou o tamanho da lista n, 
        # o que significa que todas as posições foram percorridas
        if i == n:
            
            # Se todas as posições foram percorridas, 
            # retornamos a lista arr
            return arr
        
        # Encontrando a posição do valor máximo 
        # na lista arr a partir da posição i em diante
        j = arr.index(max(arr[i:]))
        
        # Verificando se o valor em arr na posição i 
        # é diferente do valor em arr na posição j
        if arr[i] != arr[j]:
            
            # Se os valores forem diferentes, 
            # realizamos a troca entre os valores em arr nas posições i e j
            arr[i], arr[j] = arr[j], arr[i]
            
            # Incrementando o contador de trocas
            trocas += 1 
            
        # Incrementando o valor de i 
        # para continuar para a próxima posição em arr
        i += 1
        
    # Retornando a lista arr após todas as trocas
    return arr
        