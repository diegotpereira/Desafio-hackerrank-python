# Flatland é uma região plana consistindo 
# de cidades e estradas. Cada cidade é 
# identificada por um número inteiro único de 0 a n-1, 
# onde n é o número de cidades. As estradas 
# conectam cidades de maneira bidirecional. Ou seja, 
# se há uma estrada da cidade a para a cidade b, 
# então também há uma estrada da cidade b para a cidade a.

# Um astronauta quer visitar todas as cidades. Ele 
# começa em uma cidade e quer viajar para todas as 
# outras cidades para visitar as estações espaciais. 
# No entanto, o astronauta só pode se mover entre as 
# cidades através das estradas existentes. Ele não
# pode viajar diretamente pelo espaço.

# Dadas as cidades e a localização das estações 
# espaciais, você precisa determinar a maior 
# distância que o astronauta precisa viajar 
# para visitar todas as cidades.

# import math

# # Definindo a função flatlandSpaceStations com os parâmetros n (número total de cidades) e c (lista de cidades com estações)
# def flatlandSpaceStations(numero_total_cidades, lista_cidades_com_estacoes):
    
#     # Ordenando a lista de cidades 
#     # com estações em ordem crescente
#     lista_cidades_com_estacoes.sort()
    
#     # Inicializando uma lista para 
#     # armazenar as distâncias entre as cidades
#     distancias = []
    
#     # Adicionando a primeira distância 
#     # entre a primeira cidade e a primeira cidade com estação
#     distancias.append(lista_cidades_com_estacoes[0])
    
#     # Iterando sobre as cidades com estações usando 
#     # enumerate para obter o índice e o valor
#     for i, cidade_com_espaço_estação_idx in enumerate(lista_cidades_com_estacoes):
        
#         # Verificando se estamos na última cidade com estação
#         if i == len(lista_cidades_com_estacoes) - 1:
            
#             # Encerrando o loop
#             break
        
#         # Obtendo o índice da próxima cidade com estação
#         próxima_cidade_idx = lista_cidades_com_estacoes[i + 1]
        
#         # Calculando a diferença entre as cidades para encontrar a distância entre elas
#         diferente = próxima_cidade_idx - cidade_com_espaço_estação_idx - 1
        
#         # Calculando a distância mínima considerando que o espaço 
#         # entre as cidades com estação pode ser usado
#         # por uma nova estação
#         distancias.append(math.ceil(diferente / 2))
        
#     # Adicionando a última distância entre a última 
#     # cidade com estação e a última cidade
#     distancias.append(numero_total_cidades - lista_cidades_com_estacoes[-1]-1)
        
#     # Retornando a maior distância encontrada
#     return max(distancias)


# def flatlandSpaceStations(numero_total_cidades, lista_cidades_com_estacoes):
    
#     # Ordenando a lista de cidades com estações em ordem crescente
#     lista_cidades_com_estacoes.sort()
    
#     # Calculando a distância máxima entre a primeira cidade e a primeira cidade com estação, e entre a última cidade e a última cidade com estação
#     max_indice = max(lista_cidades_com_estacoes[0] - 0, numero_total_cidades - lista_cidades_com_estacoes[-1] - 1)
    
#     # Iterando sobre a lista de cidades com estações, 
#     # começando a partir do segundo elemento
#     for i in range(1, len(lista_cidades_com_estacoes)):
        
#         # Calculando a distância máxima entre cidades com estação consecutivas e comparando com o valor atual
#         max_indice = max(max_indice, (lista_cidades_com_estacoes[i] - lista_cidades_com_estacoes[i - 1]) // 2)
    
#     # Retornando o valor máximo de distância encontrado
#     return max_indice

import math 

def flatlandSpaceStations(numero_total_cidades, lista_cidades_com_estacoes):
    
    # Ordenando a lista de cidades com estações em ordem crescente
    lista_cidades_com_estacoes.sort()
    
    # Inicializando a variável resposta com a maior distância possível entre a primeira cidade e a primeira cidade com estação,
    # e entre a última cidade e a última cidade com estação
    resposta = max(lista_cidades_com_estacoes[0] - 0, (numero_total_cidades - 1) - lista_cidades_com_estacoes[-1])
    
    # Iterando sobre a lista de cidades com estações, exceto a última cidade
    for i in range(len(lista_cidades_com_estacoes) - 1):
        
        # Calculando o ponto médio entre duas cidades com estação consecutivas
        meio = math.floor((lista_cidades_com_estacoes[i] + lista_cidades_com_estacoes[i + 1]) // 2)
        
        # Calculando a distância mínima entre o ponto médio e as duas cidades com estação consecutivas
        res = min(abs(lista_cidades_com_estacoes[i] - meio), abs(lista_cidades_com_estacoes[i + 1] - meio))
        
        # Atualizando a resposta com a maior distância encontrada até agora
        resposta = max(resposta, res)
        
    # Retornando a resposta final que representa a maior distância possível entre as cidades com estações
    return resposta
        