# Dada uma grade bidimensional que 
# representa um mapa de cavidades, 
# você deve determinar quais células são cavidades. Uma célula é considerada uma cavidade se e somente se todas as células adjacentes a ela (acima, abaixo, à esquerda e à direita) forem estritamente menores que ela. Você deve substituir todas as células das cavidades por a letra 'X' e imprimir o mapa resultante.

# Em resumo, o problema solicita que você identifique as células que formam cavidades na grade, onde uma cavidade é uma célula cercada por células menores em todas as direções e, em seguida, substitua essas células por 'X' no mapa. O objetivo é fornecer a saída correta com as células de cavidades substituídas.


# # Função que identifica e marca as células de cavidade em um mapa
# def cavityMap(grade):
    
#     # Loop que percorre as linhas do mapa, exceto as bordas
#     for linha in range(1, len(grade) - 1):
        
#         # Loop que percorre as colunas do mapa, exceto as bordas
#         for coluna in range(1, len(grade) - 1):
            
#             # Verifica se a célula atual é maior do que todas as células adjacentes
#             if grade[linha][coluna] > max(grade[linha - 1][coluna], grade[linha + 1][coluna], grade[linha][coluna -1], grade[linha][coluna + 1]):
                
#                 # Substitui a célula atual pela letra 'X'
#                 grade[linha] = grade[linha][:coluna] + "X" + grade[linha][coluna + 1:]
    
#     # Retorna o mapa com as células de cavidade marcadas
#     return grade


# Função que identifica e marca as células de cavidade em um mapa

def cavityMap(grade):
    
    # Converte cada linha do mapa em uma lista de caracteres
    grade = [list(linha) for linha in grade]
    
    # Loop que percorre as linhas internas do mapa, excluindo as bordas
    for linha in range(1, len(grade) - 1):
        
        # Loop que percorre as colunas internas do mapa, excluindo as bordas
        for coluna in range(1, len(grade) - 1):
            
            # Verifica se a célula atual é maior do que todas as células adjacentes
            if grade[linha][coluna] > max(grade[linha - 1][coluna], grade[linha + 1][coluna], grade[linha][coluna - 1], grade[linha][coluna + 1]):
                
                # Substitui a célula atual pela letra 'X'
                grade[linha][coluna] = 'X'
                
    # Converte cada lista de caracteres de volta para uma linha e retorna o mapa modificado
    return [''.join(linha) for linha in grade]