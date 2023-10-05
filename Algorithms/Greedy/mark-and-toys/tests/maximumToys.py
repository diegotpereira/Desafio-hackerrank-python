# Mark gosta muito de brinquedos, 
# por isso ele quer comprar alguns 
# para seus filhos. No entanto, 
# ele está um pouco apertado de 
# dinheiro e quer minimizar os 
# custos. Há uma variedade de 
# brinquedos com diferentes preços. 
# Dado um valor inteiro k que 
# representa a quantia de dinheiro 
# que Mark tem, ele quer maximizar 
# a quantidade de brinquedos que 
# ele pode comprar.

# Dado um array de inteiros que 
# representa os preços dos brinquedos 
# e o valor k, você deve determinar 
# o máximo de brinquedos que Mark pode comprar.

# def maximumToys(precos, orcamento):
    
#     # Ordenar os preços dos brinquedos 
#     # em ordem crescente
#     precos.sort()
    
#     # Inicializar variáveis para acompanhar 
#     # o gasto total e o contador de brinquedos
#     gasto = 0
#     contador = 0
    
#     # Percorrer a lista de preços
#     for i in precos:
        
#         # Verificar se o gasto total mais o 
#         # preço atual não ultrapassa o orçamento
#         if gasto + i <= orcamento:
            
#             # Se não ultrapassar, 
#             # adicionar o preço ao gasto total
#             gasto += i 
            
#             # Incrementar o contador de brinquedos
#             contador += 1 
            
#         else:
            
#             # Se ultrapassar, sair do loop, 
#             # pois não é possível comprar mais brinquedos
#             break 
    
    
#     # Retornar o contador de brinquedos comprados
#     return contador


# def maximumToys(precos, orcamento):
    
#     # Ordenar a lista de preços dos brinquedos em ordem crescente
#     precos.sort()
    
#     # Inicializar o contador de brinquedos comprados
#     contador = 0
    
#     # Percorrer a lista de preços dos brinquedos
#     for comprado in precos:
        
#         # Subtrair o preço do brinquedo atual do orçamento
#         orcamento -= comprado
        
#         # Verificar se ainda há orçamento 
#         # para comprar mais brinquedos
#         if orcamento > 0 :
            
#             # Se ainda houver orçamento, 
#             # incrementar o contador de brinquedos comprados
#             contador += 1
            
#         else: 
            
#             # Se o orçamento estiver esgotado, 
#             # sair do loop
#             break 
        
#     # Retornar o contador de brinquedos comprados
#     return contador


# def maximumToys(precos, orcamento):
    
#     # Ordenar a lista de preços dos brinquedos em ordem crescente
#     precos.sort()
    
#     # Inicializar uma lista vazia para armazenar os brinquedos comprados
#     lista1 = []
    
#     # Percorrer a lista de preços dos brinquedos
#     for i in precos:
        
#         # Verificar se a soma dos preços dos brinquedos 
#         # na lista mais o preço atual não excede o orçamento
#         if sum(lista1) + i < orcamento:
            
#             # Se não exceder o orçamento, 
#             # adicionar o preço do brinquedo à lista de brinquedos comprados
#             lista1.append(i)
            
#     # Retornar o tamanho da lista de brinquedos comprados, 
#     # ou seja, 
#     # o número máximo de brinquedos que podem ser comprados
#     return len(lista1)


def maximumToys(precos, orcamento):
    
    # Ordenar a lista de preços dos brinquedos em ordem crescente
    classificar_precos = sorted(precos)
    
    # Inicializar o contador de brinquedos comprados
    contador = 0
    
    # Continuar enquanto houver orçamento para o brinquedo mais barato
    while orcamento >= classificar_precos[0]:
        
        # Subtrair o preço do brinquedo mais barato do orçamento
        orcamento -= classificar_precos[0]
        
        # Remover o brinquedo mais barato da lista de preços
        classificar_precos.pop(0)
        
        # Incrementar o contador de brinquedos comprados
        contador += 1
        
    # Retornar o contador de brinquedos comprados
    return contador