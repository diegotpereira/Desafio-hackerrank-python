# A tarefa do problema "Minimum Loss" no HackerRank é a seguinte:

# Dado um array de preços de casas à venda em diferentes anos, 
# a tarefa é encontrar a menor perda possível que um investidor 
# teria ao comprar uma casa em um ano e vendê-la em um ano posterior. 
# A perda é calculada subtraindo-se o preço de compra do preço de venda.

# No entanto, há uma restrição adicional: o investidor deve vender 
# a casa em um ano posterior ao ano de compra, e a perda deve ser 
# a menor entre todas as possíveis combinações de compra e venda 
# que atendem a essa condição.

# A entrada para o problema consiste em um único array de inteiros, 
# onde cada elemento representa o preço da casa em um determinado ano. 
# O objetivo é determinar a menor perda possível que um investidor 
# pode sofrer ao comprar e vender uma casa, seguindo as regras 
# mencionadas acima.

# A saída esperada é um único número inteiro representando a menor perda.

# def minimumLoss(preco):
    
#     # Cria uma lista de índices ordenados dos preços em ordem decrescente
#     r_indice = sorted(range(len(preco)), key=lambda x: preco[x], reverse=True)
    
#     # Lista para armazenar as perdas
#     perda = []
    
#     # Loop através dos índices ordenados, exceto o último
#     for i in range(len(r_indice) - 1):
        
#         # Inicializa um índice para o próximo valor na lista
#         j = i + 1
        
#         # Encontra um índice posterior onde o ano de venda seja anterior ao ano de compra
#         while j < len(preco) and r_indice[j] < r_indice[i]:
            
#             # Avança para o próximo índice
#             j += 1
            
#         # Se um índice válido foi encontrado
#         if j < len(preco):
            
#             # Calcula a perda entre os preços de compra e venda 
#             # e a adiciona à lista de perdas
#             perda.append(preco[r_indice[i]] - preco[r_indice[j]])
            
#     # Retorna a menor perda encontrada
#     return min(perda)

# import math

# def minimumLoss(preco):
    
#     # Cria um dicionário para mapear valores de preço para seus índices
#     indice_valores = { val: i for i, val in enumerate(preco)}
    
#     # Ordena a lista de preços em ordem decrescente
#     ordem_precos = sorted(preco, reverse=True)
    
#     # Inicializa a variável 'minima_perda' com infinito negativo
#     minima_perda = -math.inf
    
#     # Loop através dos índices da lista ordenada de preços, 
#     # exceto o último
#     for j in range(len(ordem_precos) - 1):
        
#         # Calcula a diferença entre o preço atual e o próximo preço na lista
#         dif = ordem_precos[j + 1] - ordem_precos[j]
        
#         # Verifica se o ano do próximo preço é maior que o ano do preço atual
#         if indice_valores[ordem_precos[j + 1]] > indice_valores[ordem_precos[j]]:
            
#             # Atualiza o valor de 'minima_perda' para o máximo entre o valor atual e a diferença
#             minima_perda = max(minima_perda, dif)
            
#     # Retorna o valor absoluto de 'minima_perda' como a menor perda possível
#     return abs(minima_perda)

# from itertools import tee
# from operator import itemgetter

# def minimumLoss(preco):
    
#     # Enumera os preços para criar pares de (índice, preço)
#     preco = enumerate(preco)
    
#      # Ordena os pares pelo preço (segundo elemento)
#     preco = sorted(preco, key=itemgetter(1))
    
#     # Cria duas iterações independentes da lista de preços
#     a, b = tee(preco)
    
#     # Avança a segunda iteração 'b' para o próximo elemento
#     next(b)
    
#     # Cria pares consecutivos usando as iterações 'a' e 'b'
#     pares = zip(a, b)
    
#     # Retorna a menor perda entre os pares de preços onde o 
#     # índice de compra é maior que o índice de venda
#     return min(b[1] - a[1] for a,b in pares if a[0] > b[0])

# import math
# from collections import defaultdict

# def minimumLoss(preco):
    
#     # Cria um dicionário que mapeia preço para lista de índices
#     lista_precos = defaultdict(list)
    
#     # Loop para mapear cada preço para seus índices
#     for indice, p in enumerate(preco):
        
#         # Adiciona o índice à lista de índices do preço
#         lista_precos[p].append(indice)
        
#         # Se mais de um índice estiver associado ao mesmo preço, 
#         # a perda é zero
#         if len(lista_precos[p]) > 1:
            
#             # Retorna 0 imediatamente
#             return 0
        
#     # Obtém o número de preços
#     n = len(preco)
    
#     # Inicializa a resposta com infinito positivo
#     resposta = math.inf
    
#     # Ordena a lista de preços em ordem decrescente
#     preco.sort(reverse=True)
    
#     # Loop para comparar preços consecutivos
#     for i in range(1, n):
        
#         # Se o índice de compra é maior que o índice de venda
#         if lista_precos[preco[i]] > lista_precos[preco[i - 1]]:
            
#             # Atualiza a resposta com a menor perda encontrada
#             resposta = min(resposta, preco[i - 1] - preco[i])
            
#     # Retorna a menor perda possível
#     return resposta


# def minimumLoss(preco):
    
#     # Ordena a lista de preços em ordem crescente
#     arr = sorted(preco)
    
#     # Calcula a soma de todos os preços (para inicializar 'somas_precos')
#     somas_precos = sum(arr)
    
#     # Dicionário para mapear preços para seus índices
#     dicionario_precos = {}
    
#     for i in range(len(preco)):
        
#         # Mapeia o preço para o índice correspondente
#         dicionario_precos[preco[i]] = i
        
#     # Cria uma lista temporária para armazenar índices
#     temp = [0] * len(preco)
    
#     for i in range(len(preco)):
        
#         # Preenche 'temp' com os índices correspondentes aos preços
#         temp[i] = dicionario_precos[arr[i]]

#     # Inicializa o índice 'i'
#     i = 0
    
#     # Inicializa o índice 'j'
#     j = 1
    
#     # Loop para comparar os índices
#     while i < len(preco) and j < len(preco):
        
#         # Se o índice de compra é menor que o índice de venda
#         if temp[i] < temp[j]:
            
#             # Avança o índice 'i'
#             i += 1
            
#             # Avança o índice 'j'
#             j += 1
            
#         # Caso contrário, 
#         # se o índice de venda é menor ou igual ao índice de compra
#         else:
            
#             # Se a diferença entre os preços for menor que 'somas_precos'
#             if somas_precos > arr[j] - arr[i]:
                
#                 # Atualiza o valor de 'somas_precos' com a menor diferença
#                 somas_precos = arr[j] - arr[i]
                
#             # Avança o índice 'i'
#             i += 1
            
#             # Avança o índice 'j'
#             j += 1
    
#     # Retorna a menor perda possível
#     return somas_precos


# def minimumLoss(preco):
    
#     # Inicializa a variável 'minima_perda' com infinito positivo
#     minima_perda = float('inf')
    
#      # Loop externo para iterar sobre os preços
#     for i in range(0, len(preco)):
        
#         # Loop interno para comparar os preços em pares
#         for j in range(i + 1, len(preco)):
            
#             # Calcula a diferença entre os preços
#             dif = preco[i] - preco[j]
            
#             # Se a diferença for positiva (perda)
#             if dif > 0:
                
#                 # Atualiza a 'minima_perda' com a menor diferença encontrada
#                 minima_perda = min(minima_perda, dif)
                
#     # Retorna a menor perda possível
#     return minima_perda


# def minimumLoss(preco):
    
#     # Cria um dicionário para mapear preços para seus índices
#     dicionario = {}
    
#     # mapeia cada elemento da lista de preços
#     for i in range(len(preco)):
        
#         # Associa cada preço ao seu índice no dicionário
#         dicionario[preco[i]] = i 
        
#     # Ordena a lista de preços em ordem decrescente
#     preco = sorted(preco, reverse=True)
    
#     # Inicializa 'minimo_perdida' com o maior preço
#     minimo_perdida = max(preco)
    
#     # Loop para comparar os preços em pares
#     for i in range(1, len(preco)):
        
#         # Verifica se o índice de compra é menor que o índice de venda
#         # e se a diferença entre os preços é menor que 'minimo_perdida'
#         if dicionario[preco[i - 1]] < dicionario[preco[i]] and preco[i - 1] - preco[i] < minimo_perdida:
            
#             # Atualiza 'minimo_perdida' com a menor diferença encontrada
#             minimo_perdida = preco[i - 1] - preco[i]
            
#     # Retorna a menor perda possível
#     return minimo_perdida

def minimumLoss(preco): 
    
    # Obtém o número de elementos na lista de preços
    numero_elementos = len(preco)
    
    # Inicializa a variável 'm' com um valor alto inicial
    minima_perda = 9999999
    
    # Ordena a lista de preços em ordem crescente
    lista_precos = sorted(preco)
    
     # Loop para percorrer os elementos da lista de preços, 
     # exceto o último
    for i in range(numero_elementos - 1):
        
        # Calcula a diferença entre elementos adjacentes
        diferenca_lementos = lista_precos[i + 1] - lista_precos[i]
        
        # Verifica se a diferença é menor que 'minima_perda' e se o índice de compra é maior que o índice de venda
        if diferenca_lementos < minima_perda and preco.index(lista_precos[i]) > preco.index(lista_precos[i + 1]):
            
            # Atualiza 'minima_perda' com a menor diferença encontrada
            minima_perda = diferenca_lementos 
        
    # Retorna a menor perda possível
    return minima_perda