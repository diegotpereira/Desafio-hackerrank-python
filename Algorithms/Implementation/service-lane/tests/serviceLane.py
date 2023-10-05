# A tarefa do problema "Service Lane" no HackerRank é a seguinte:

# Dada uma largura fixa de pistas e uma série de segmentos em uma 
# estrada, onde cada segmento tem uma largura específica, a tarefa 
# é determinar a largura mínima permitida de veículo que pode 
# atravessar cada segmento, considerando as restrições da pista. 
# Em outras palavras, você recebe uma lista de larguras de segmentos 
# e uma lista de casos de teste, onde cada caso de teste consiste 
# em um intervalo de segmentos (entrada e saída) e você deve determinar 
# a largura mínima permitida para o veículo passar por todos os 
# segmentos dentro do intervalo especificado.

# def serviceLane(n, casos):
    
#     resultados = []
    
#     for caso in casos:
        
#         resultados.append(min(n[caso[0]:caso[1]+1]))
        
    
#     return resultados

# def serviceLane(n, cases):
#     result = []
#     for case in cases:
#         subarray = n[case[0]:case[1]+1]
#         min_w = min(subarray)
#         result.append(min_w)
    
#     return result

# def serviceLane(n, cases):
#     # Write your code here
#     val = []
#     for I in cases:
        
#         p = min(I)
#         q = max(I)
#         i = p
#         Min = n[i]
#         while i <= q:
#             if n[i]<Min:
#                 Min = n[i]
#             i += 1
        
#         val.append(Min)
        
    
#     return val

# def serviceLane(n, cases):
#     # Write your code here
#     ans = []
    
#     for i in cases:
#         entrada, saida = i 
        
#         min_width = min(width[entrada:saida+1])
        
#         ans.append(min_width)
        
#     return ans


def serviceLane(n, cases):
    # Write your code here
    largest_vehicle = []
    for case in cases:
        largest_vehicle.append(min(width[case[0]:case[1]+1]))
    return largest_vehicle