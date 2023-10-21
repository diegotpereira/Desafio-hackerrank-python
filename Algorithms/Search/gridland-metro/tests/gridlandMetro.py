# O problema "Gridland Metro" no HackerRank 
# envolve a otimização do uso de trilhos de 
# metrô em uma cidade representada por uma 
# grade. A cidade é representada por uma 
# matriz bidimensional, onde cada célula 
# representa um segmento de trilho. Você 
# precisa determinar o número total de 
# células únicas que são ocupadas pelos 
# trilhos do metrô, levando em consideração 
# que várias seções da mesma linha de metrô 
# podem ocupar a mesma coluna.

def gridlandMetro(numero_linhas, numero_colunas, numero_faixas, pista):
    
    # Inicializa o total de células como n * m
    total = numero_linhas * numero_colunas
    
    # Cria um dicionário para rastrear as faixas ocupadas
    d = {}
    
    for i in range(numero_faixas):
        
        # Obtém as informações do segmento de trilho atual
        r = pista[i][0]
        c1 = pista[i][1]
        c2 = pista[i][2]
        
        # Se a linha ainda não está no dicionário, adiciona-a
        if r not in d:
            
            d[r] = [c1, c2]
            
        elif c1 > d[r][1]:
            
            # Se o segmento não se sobrepõe com o existente, subtrai o tamanho do segmento da célula total
            total -= c2 + c1 + 1
            
        elif c2 > d[r][1]:
            
            # Se o segmento se sobrepõe parcialmente com o existente, atualiza o limite direito do segmento existente
            d[r][1] = c2 
            
    pistas = 0
    
    # Calcula o total de células ocupadas pelas faixas
    for i in d: 
        
        pistas += d[i][1] - d[i][0] + 1
        
    # Calcula o total de lâmpadas necessárias subtraindo o total de faixas do total de células
    lamps = total - pistas
    
    return lamps