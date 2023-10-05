# O problema "The Grid Search" 
# envolve a busca de um padrão 
# em uma matriz 2D. A tarefa 
# consiste em determinar se uma 
# matriz menor, chamada de matriz 
# de padrão, está contida dentro 
# de uma matriz maior, chamada de 
# matriz de grade. O objetivo é 
# descobrir se a matriz de padrão 
# aparece como uma submatriz contígua 
# em algum lugar da matriz de grade.

# Função que realiza uma busca em uma grade 2D.

# def gridSearch(G, P):
    
#     # Loop pelas linhas da grade principal onde o padrão poderia ser encontrado.
#     for linha in range(len(G) - len(P) + 1):
        
#         # Loop pelas colunas da grade principal onde o padrão poderia ser encontrado.
#         for coluna in range(len(G[0]) - len(P[0]) + 1):
            
#             # Loop pelas linhas do padrão.
#             for i in range(len(P)):
                
#                 # Verifica se a subgrade atual não corresponde ao padrão.
#                 if P[i] != G[linha + i][coluna : coluna + len(P[0])]:
                    
#                     # Se a correspondência não for encontrada, 
#                     # definimos 'NO'.
#                     encontrado = 'NO'
                    
#                     # Saímos do loop, 
#                     # já que não é necessário continuar verificando.
#                     break 
                
#                 else:
                    
#                     # Se a correspondência for encontrada, 
#                     # definimos 'YES'.
#                     encontrado = 'YES'
                    
#             # Se o padrão for encontrado na subgrade atual,
#             if encontrado == 'YES':
                
#                 # retornamos 'YES' imediatamente.
#                 return encontrado

#     # Retornamos o resultado (pode ser 'YES' ou 'NO') após percorrer toda a grade.
#     return encontrado

# Função que realiza uma busca de padrão em uma matriz G.

def gridSearch(G, P):
    
    # Loop para percorrer as linhas onde o padrão pode começar
    for i in range(len(G) - len(P) + 1):
        
        # Loop para percorrer as colunas onde o padrão pode começar
        for j in range(len(G[0]) - len(P[0]) + 1):
            
            # Encontra a posição inicial do primeiro elemento do padrão na linha atual
            posicao_inicial = str(G[i][j:]).find(str(P[0]))
            
            # Se a posição inicial for encontrada (diferente de -1), 
            # o padrão pode estar presente
            if posicao_inicial > - 1:
                
                # Variável para acompanhar se o padrão fecha
                fechou = 'YES'
                
                # Loop para verificar os elementos restantes do padrão
                for k in range(1, len(P)):
                    
                    # Verifica se os elementos restantes do padrão correspondem às linhas consecutivas na matriz G
                    if G[i + k][(j + posicao_inicial) : (j + posicao_inicial + len(P[0]))] != P[k]:
                        
                        # Se a correspondência não for encontrada, o padrão não fecha
                        fechou = 'NO'
                        
                        # Sai do loop interno, pois não há mais correspondência para verificar
                        break 
                    
                # Se todas as verificações foram bem-sucedidas e o padrão fecha
                if fechou == 'YES':
                    
                    # Retorna 'YES', indicando que o padrão foi encontrado e fecha
                    return fechou
    
    # Se nenhum padrão for encontrado, retorna 'NO'
    return 'NO'