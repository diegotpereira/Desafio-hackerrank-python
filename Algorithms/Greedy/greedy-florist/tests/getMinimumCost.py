# O problema "Greedy Florist" envolve um cenário 
# em que um grupo de amigos deseja comprar flores 
# de uma floricultura. Cada flor tem um preço diferente, 
# e a floricultura oferece um desconto especial para 
# grupos de amigos. A tarefa é determinar a maneira 
# mais eficiente de os amigos comprarem as flores 
# para minimizar o custo total.

# Detalhes da Tarefa:

# Aqui estão os detalhes da tarefa:

# Existem N flores disponíveis para compra, 
# numeradas de 1 a N.
# Cada flor tem um preço diferente, e os preços 
# das flores são dados em uma matriz de tamanho N.
# Os amigos desejam comprar K flores, onde K é 
# menor ou igual a N.
# A floricultura oferece um desconto especial: 
# se um amigo comprou uma flor na sua última 
# compra, na próxima compra ele deve comprar 
# a flor com o preço mais alto entre 
# as flores disponíveis.
# A tarefa é determinar o custo mínimo 
# total que os amigos terão que pagar para comprar K flores.


# # Função para calcular o custo mínimo total da compra de flores por um grupo de amigos

# def getMinimumCost(numero_amigos, preco_original):
    
#     # Ordena os preços das flores em ordem 
#     # decrescente para que os amigos comprem as mais caras primeiro
#     preco_original.sort(reverse=True)
    
#     # Inicializa o custo total
#     custo_total = 0
    
#     # Inicializa o índice do cliente para 
#     # rastrear qual amigo está comprando
#     indice_do_cliente = 0
    
#     # Itera sobre os preços das flores
#     for preco in preco_original:
        
#         # Calcula o custo para a próxima flor com base no preço atual e no índice do cliente
#         custo = preco * ((indice_do_cliente // numero_amigos) + 1)
        
#         # Adiciona o custo ao custo total
#         custo_total += custo 
        
#         # Incrementa o índice do cliente para o próximo amigo
#         indice_do_cliente += 1
    
#     # Retorna o custo total mínimo
#     return custo_total


# # Função para calcular o custo mínimo total da compra 
# # de flores por um grupo de amigos

# def getMinimumCost(numero_amigos, preco_original):
    
#     # Obtém o número de flores disponíveis
#     n = len(preco_original)
    
#     # Ordena os preços das flores em ordem decrescente 
#     # para que os amigos comprem as mais caras primeiro
#     preco_original.sort(reverse=True)
    
#     # Inicializa o custo total
#     preco = 0
    
#     # Itera sobre os preços das flores
#     for i in range(n):
        
#         # Calcula o custo para a próxima flor com base no preço atual e no índice do amigo que está comprando.
#         # A divisão inteira (i // numero_amigos) determina qual amigo está comprando a flor.
#         # O +1 garante que o primeiro amigo compre a flor pelo preço original, o segundo pelo dobro do preço, e assim por diante
#         preco += (i // numero_amigos + 1) * preco_original[i]
        
#     # Retorna o custo total mínimo
#     return preco