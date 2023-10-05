# O problema "Ice Cream Parlor" do HackerRank é o seguinte:

# Você possui um valor total de dinheiro que deseja gastar 
# na compra de sorvetes em uma sorveteria. Há uma lista de 
# preços de sorvetes disponíveis, cada um com um custo específico. 
# Você deve encontrar dois sabores de sorvete diferentes cuja soma
# dos custos seja igual ao valor total de dinheiro que você possui.

# A tarefa consiste em escrever uma função que, dado o valor total 
# de dinheiro e a lista de preços dos sorvetes, determine os índices 
# (baseados em 1) dos dois sabores que você deve comprar. É garantido 
# que sempre existe uma solução.

# def icecreamParlor(saldo, arr):
    
#     # Obtém o tamanho da lista de preços de sorvete
#     n = len(arr)
    
#     # Lista para armazenar os índices dos sabores 
#     # de sorvete encontrados
#     indice = []
    
#     # Variável de controle para indicar se os 
#     # sabores foram encontrados
#     encontrado = 0
    
#     # Percorre a lista de preços (exceto o último elemento)
#     for i in range(n - 1):
        
#         # Obtém o preço do sabor de sorvete na posição i
#         x = arr[i]
        
#         # Percorre os sabores restantes na lista a partir 
#         # da posição i + 1
#         for j in range(i + 1, n):
            
#             # Obtém o preço do sabor de sorvete na posição j
#             y = arr[j]
            
#             # Verifica se a soma dos preços é igual ao saldo desejado
#             if x + y == saldo:
                
#                 # Marca como encontrado
#                 encontrado = 1
                
#                 # Adiciona o índice do primeiro sabor de sorvete encontrado
#                 indice.append(i + 1)
                
#                 # Adiciona o índice do segundo sabor de sorvete encontrado
#                 indice.append(j + 1)
                
#                 # Sai do loop interno
#                 break 
            
#         # Se os sabores foram encontrados, sai do loop externo
#         if encontrado == 1:
            
#             break
        
#     # Retorna os índices dos sabores de sorvete encontrados que somam o saldo
#     return indice

# from collections import defaultdict

# def icecreamParlor(saldo, arr):
    
#     # Cria um dicionário com valores padrão sendo listas vazias
#     d = defaultdict(list)
    
#     # Percorre a lista de preços de sorvete, usando o enumerate para obter o índice e o valor
#     for indice, chave in enumerate(arr, start = 1):
        
#         # Adiciona o índice ao dicionário, usando o preço como chave
#         d[chave].append(indice)
        
#     # Percorre novamente a lista de preços de sorvete para encontrar os pares de sabores
#     for indice, chave in enumerate(arr, start = 1):
        
#         # Verifica se o complemento (saldo - preço) está no dicionário
#         if (saldo - chave) in d: 
            
#             # Verifica se o complemento é igual ao preço atual
#             if(saldo - chave) == chave:
            
#                 # Verifica se há mais de um índice associado a esse complemento
#                 if len(d[(saldo - chave)]) > 1:
                    
#                     # Retorna os índices dos sabores de sorvete encontrados
#                     return sorted([indice, d[(saldo - chave)][1]])
                
#                 else:
                    
#                     # Continua procurando se não houver par suficiente
#                     continue
                
#             else:
                
#                 # Retorna os índices dos sabores de sorvete encontrados
#                 return sorted([indice, d[(saldo - chave)][-1]])
        
        
# def icecreamParlor(saldo, arr):
    
#     # Classifica a lista de preços dos sorvetes em ordem crescente
#     arr_classificado = sorted(arr)
    
#     # Percorre a lista classificada com índices usando enumerate
#     for i, x in enumerate(arr_classificado):
        
#         # Percorre os elementos restantes da lista após a posição i
#         for y in arr_classificado[i + 1:]:
            
#             # Verifica se a soma dos preços é igual ao saldo desejado
#             if x + y == saldo:
                
#                 # Obtém os índices baseados em 1 dos sabores de 
#                 # sorvete encontrados
#                 a = arr.index(x) + 1
#                 b = arr.index(y) + 1
                
#                 # Verifica se os índices são iguais e 
#                 # ajusta o segundo índice
#                 if a == b:
                    
#                     b = arr.index(x, a) + 1
                
#                 # Retorna os índices dos sabores de sorvete encontrados    
#                 return sorted([a, b])
            
#             # Se a soma for maior que o saldo, interrompe o loop interno
#             elif x + y > saldo: 
                
#                 break


# def icecreamParlor(saldo, arr):
    
#     # Cria um conjunto vazio para rastrear 
#     # os preços de sorvetes já vistos
#     visto = set()
    
#     # Percorre a lista de preços de sorvetes com índices usando enumerate
#     for indice, preco in enumerate(arr):
        
#         # Verifica se o complemento (saldo - preco) está no conjunto de preços vistos
#         if saldo - preco in visto:
            
#             # Retorna os índices dos sabores de sorvete encontrados que somam o saldo
#             return sorted([arr.index(saldo - preco) + 1, indice + 1])
        
#         # Adiciona o preço atual ao conjunto de preços vistos
#         visto.add(preco)


# def icecreamParlor(saldo, arr):
    
#     # Percorre a lista de preços de sorvetes com índices usando um loop for
#     for i in range(len(arr)):
        
#         # Percorre os sabores de sorvetes restantes na lista, 
#         # começando a partir da próxima posição (i + 1)
#         for j in range(i + 1, len(arr)):
            
#             # Verifica se a soma dos preços dos sabores de 
#             # sorvetes é igual ao saldo desejado
#             if arr[i] + arr[j] == saldo:
                
#                 # Retorna os índices dos sabores de sorvetes 
#                 # encontrados que somam o saldo
#                 return [i + 1, j + 1]


# def icecreamParlor(saldo, arr):
    
#     # Percorre a lista de preços de sorvetes 
#     # com índices usando um loop for
#     for i in range(len(arr)):
        
#         # Calcula a diferença entre o saldo desejado 
#         # e o preço do sorvete atual
#         dif = saldo - arr[i]
        
#         # Verifica se a diferença está presente nos 
#         # sabores de sorvetes restantes na lista
#         if dif in arr[i + 1:]:
            
#             # Retorna os índices dos sabores de sorvetes encontrados que somam o saldo
#             # i + 1: índice do sabor atual, i + 1 + arr[i + 1:].index(dif) + 1: índice do segundo sabor
#             return [i + 1, i + 1 + arr[i + 1:].index(dif) + 1]
        
#     # Retorna uma lista vazia se não encontrar dois sabores que satisfaçam a condição
#     return []


def icecreamParlor(saldo, arr):
    
    # Lista para armazenar os índices dos sabores 
    # de sorvete encontrados
    resposta = []
    
    # Obtém o tamanho da lista de preços de sorvete
    n = len(arr)
    
    # Percorre a lista de preços de sorvetes com 
    # índices usando um loop for
    for i in range(n):
        
        # Percorre os sabores de sorvetes restantes na lista, 
        # começando a partir da próxima posição (i + 1)
        for j in range(i + 1, n):
            
            # Verifica se a soma dos preços dos sabores de 
            # sorvetes é igual ao saldo desejado
            if arr[i] + arr[j] == saldo:
                
                # Adiciona os índices dos sabores de sorvetes 
                # encontrados à lista de resposta
                resposta.append(i + 1)
                resposta.append(j + 1)
                
    # Retorna a lista de índices dos sabores de sorvetes encontrados
    return resposta