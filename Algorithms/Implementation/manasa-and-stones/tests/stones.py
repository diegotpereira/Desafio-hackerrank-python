# Dado um número de etapas, a diferença entre 
# dois tipos de pedras e o número de pedras
# disponíveis de cada tipo, você deve determinar 
# todas as possíveis quantidades de distâncias 
# que podem ser obtidas somando um certo número 
# de pedras de cada tipo. Você precisa listar 
# essas quantidades de distâncias em ordem crescente.

# Basicamente, você está tentando encontrar 
# todas as possíveis somas de pedras dos dois 
# tipos após um certo número de etapas. A 
# tarefa é gerar uma lista de distâncias 
# possíveis em ordem crescente.


# # Função que calcula as diferentes somas possíveis de pedras após um número de etapas

# def stones(n, a, b):
    
#     # Lista para armazenar as diferentes somas possíveis
#     mapa = []
    
#     # Loop que percorre o número de etapas
#     for i in range(0, n):
        
#         # Variável para armazenar a soma das pedras nesta etapa
#         soma_pedras = 0
        
#         # Calcula a soma das pedras com base nas quantidades e tipos de pedras
#         soma_pedras = soma_pedras + (i * a) + ((n - 1 - i) * b)
        
#         # Adiciona a soma calculada à lista mapa
#         mapa.append(soma_pedras)
        
#         # Cria um conjunto invertendo a ordem dos valores na lista mapa
#         l = set(mapa[::-1])
        
#         # Ordena o conjunto de somas possíveis em ordem crescente
#         resultado = sorted(l)
    
#     # Retorna a lista de somas possíveis em ordem crescente
#     return resultado

# Função que calcula as diferentes somas possíveis de pedras após um número de etapas

# def stones(n, a, b):
    
#     # Se os tipos de pedras forem iguais
#     if a == b:
        
#         # Retorna uma lista com a soma única possível (n - 1) * a
#         return [(n - 1) * a]
    
#     # Calcula a diferença entre os tipos de pedras
#     diferente = abs(a - b)
    
#     # Calcula a soma inicial possível
#     inicial = min(a, b) * (n - 1)
    
#     # Calcula a soma final possível
#     final = max(a, b) * (n - 1)
    
#     # Lista para armazenar as diferentes somas possíveis
#     resposta = []
    
#     # Loop que percorre as somas possíveis no intervalo
#     for i in range(inicial, final + 1, diferente):
        
#         # Adiciona a soma atual à lista de respostas
#         resposta.append(i)
        
#     # Retorna a lista de somas possíveis
#     return resposta

# Função que calcula as diferentes somas possíveis de pedras após um número de etapas

def stones(n, a, b):
    
    # Conjunto para armazenar as diferentes somas possíveis
    res = set()
    
    # Loop que percorre as etapas
    for i in range(n):
        
        # Inicializa o valor de i com n - 1
        i = n - 1 
        
        # Loop while que percorre os valores de i em ordem decrescente
        while (i >= 0):
            
            # Calcula a soma das pedras com base nas quantidades e tipos de pedras
            p = a * i + b * (n - i - 1)
            
            # Adiciona a soma ao conjunto res
            res.add(p)
            
            # Decrementa o valor de i
            i -= 1
            
    # Retorna a lista de somas possíveis ordenada em ordem crescente
    return sorted(list(res))