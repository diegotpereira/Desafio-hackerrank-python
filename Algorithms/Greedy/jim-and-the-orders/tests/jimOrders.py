# A tarefa do problema "Jim and the Orders" no 
# HackerRank envolve a seguinte situação:

# Jim é um entregador de comida e está responsável 
# por entregar pedidos para os clientes. Cada pedido 
# é composto por dois valores: o tempo em que o pedido 
# foi feito (tempo de chegada) e o tempo necessário 
# para preparar o pedido (tempo de preparo).

# A tarefa específica é determinar a ordem em que 
# Jim deve entregar os pedidos, de modo que ele 
# possa minimizar o tempo total gasto nas entregas. 
# O objetivo é encontrar a sequência de pedidos que 
# minimize o tempo total, considerando tanto o tempo 
# de chegada quanto o tempo de preparo.

# Em resumo, o problema "Jim and the Orders" requer 
# que você escreva um programa que ordene os pedidos 
# de entrega de Jim de acordo com um critério específico, 
# de modo que o tempo total gasto nas entregas seja minimizado. 
# Isso envolve a consideração do tempo de chegada e do tempo 
# de preparo de cada pedido.

# def jimOrders(pedidos):
    
#     # Crie uma lista chamada 'enumerar_pedidos' contendo índices e a soma dos tempos de chegada e preparo de cada pedido
#     enumerar_pedidos = [[i + 1, sum(pedido)] for i, pedido in enumerate(pedidos)]
    
#     # Ordene a lista 'enumerar_pedidos' com base na soma dos tempos usando uma função lambda como critério de ordenação
#     pedidos_indice = [pedido[0] for pedido in sorted(enumerar_pedidos, key= lambda x : x[1])]
    
#     # Retorne a lista de índices dos pedidos ordenados
#     return pedidos_indice


# def jimOrders(pedidos):
    
#     # Percorra os pedidos 
#     for i, pedido in enumerate(pedidos):
        
#         # e adicione um índice único a cada pedido
#         pedido.append(i + 1)
        
#     # Ordene os pedidos com base na soma dos tempos de 
#     # chegada e preparo usando uma função lambda como critério de ordenação
#     pedidos.sort(key=lambda x: x[0] + x[1])
    
#     # Crie uma lista com os índices dos pedidos ordenados
#     return [pedido[2] for pedido in pedidos]


def jimOrders(pedidos):
    
    # Crie uma lista 'resposta' contendo a soma dos tempos de chegada e preparo de cada pedido
    resposta = [sum(i) for i in pedidos]
    
    # Crie uma lista 'indice' contendo os índices dos pedidos de 1 a N
    indice = list(range(1, len(pedidos) + 1))
    
    # Use a função 'zip' para combinar as listas 'resposta' e 'indice', depois ordene-as e retorne apenas os índices ordenados
    return [j for i, j in sorted(zip(resposta, indice))]