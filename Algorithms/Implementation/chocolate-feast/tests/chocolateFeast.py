# Little Bobby adora chocolates. 
# Ele gosta muito deles e sempre 
# quer comer quantos puder. Certa 
# vez, ele foi a uma loja que 
# vende chocolates por um preço 
# específico. Bobby teve um certo 
# dinheiro e queria gastá-lo 
# inteiramente para comprar chocolates.

# O preço de cada chocolate é C 
# reais. A loja também tem uma promoção: 
# por M embalagens vazias de chocolate, 
# Bobby pode obter um chocolate 
# adicional gratuitamente.

# Bobby tem N reais e deseja gastar 
# todo esse dinheiro para comprar 
# chocolates. Ele quer saber quantos 
# chocolates pode comprar, tomando 
# em consideração a promoção da loja.

# Escreva uma função que, dada a 
# quantidade de dinheiro que Bobby 
# tem, o preço de cada chocolate, 
# e o número de embalagens vazias 
# necessárias para obter um chocolate 
# adicional, determine quantos 
# chocolates Bobby pode comprar.

# def chocolateFeast(quantia_dinheiro, preco_chocolate, numero_embalagens_vazias):
    
#     # Calculando o número inicial de chocolates que Bobby pode comprar
#     embrulhado = quantia_dinheiro // preco_chocolate
#     chocolate = embrulhado
    
#     # Inicialização da variável de controle do loop
#     flag = True 
    
#     # Loop para usar as embalagens vazias e obter chocolates adicionais
#     while flag:
        
#         # Verificando se Bobby tem embalagens suficientes para a oferta
#         if embrulhado >= numero_embalagens_vazias:
            
#             # Calculando quantos chocolates Bobby pode obter com as embalagens vazias
#             validação_oferta = embrulhado // numero_embalagens_vazias
            
#             # Atualizando o total de chocolates e embalagens vazias restantes
#             chocolate = chocolate + validação_oferta
#             embrulhado = validação_oferta + (embrulhado % numero_embalagens_vazias)
            
#         else:
            
#             # Se Bobby não tiver embalagens suficientes, encerra o loop
#             flag = False
            
#     # Retorna o total de chocolates que Bobby pode comprar
#     return chocolate


def chocolateFeast(quantia_dinheiro, preco_chocolate, numero_embalagens_vazias):
    
    # Calculando o número inicial de chocolates que Bobby pode comprar
    chocolate = quantia_dinheiro // preco_chocolate
    
    # Copiando o valor inicial de chocolates para outra variável
    a = chocolate
    
    # Loop para usar as embalagens vazias e obter chocolates adicionais
    while a >= numero_embalagens_vazias:
        
        # Reduzindo a quantidade de embalagens vazias 
        # e adicionando um chocolate
        a = a - numero_embalagens_vazias + 1
        chocolate += 1
        
    # Retorna o total de chocolates que Bobby pode comprar
    return chocolate