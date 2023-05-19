# int p: o preço do primeiro jogo
# int d: o desconto do preço do jogo anterior
# int m: o custo mínimo de um jogo
# int s: o orçamento inicial


# def howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial):
    
#     # Inicializa uma variável n_jogos para contar o número de jogos comprados
#     n_jogos = 0
    
#     # Enquanto o saldo disponível for maior ou igual ao preço do primeiro jogo:
#     while orcamento_inicial >= preco_primeiro_jogo:
        
#         # Subtrai o preço do primeiro jogo do saldo disponível
#         orcamento_inicial = orcamento_inicial - preco_primeiro_jogo
        
#         # Incrementa o número de jogos comprados
#         n_jogos += 1
        
#         # Atualiza o preço do primeiro jogo para o valor máximo entre o preço mínimo permitido
#         # e o resultado da subtração do desconto do preço do jogo anterior
#         preco_primeiro_jogo = max(custo_minimo_jogo, preco_primeiro_jogo - desconto_jogo_anterior)
        
#     # Retorna o número total de jogos comprados
#     return n_jogos


def howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial):
    
    # Inicializa uma variável contador para contar o número de jogos comprados
    contador = 0
    
    # Inicializa uma variável custo para controlar o custo total dos jogos
    custo = 0
    
    # Enquanto o custo total for menor ou igual ao saldo disponível:
    while custo <= orcamento_inicial:
        
        # Incrementa o contador de jogos
        contador += 1
        
        # Se o preço do primeiro jogo for menor do que o preço mínimo permitido:
        if preco_primeiro_jogo < custo_minimo_jogo:
            
            # Adiciona o preço mínimo permitido ao custo total
            custo += custo_minimo_jogo
            
        # Caso contrário:
        else:
            
            # Adiciona o preço do primeiro jogo ao custo total
            custo += preco_primeiro_jogo
            
            # Atualiza o preço do primeiro jogo subtraindo o desconto
            preco_primeiro_jogo = preco_primeiro_jogo - desconto_jogo_anterior
            
    # Retorna o número total de jogos comprados, 
    # subtraindo 1 para excluir o último jogo que excedeu o saldo disponível
    return contador - 1
    