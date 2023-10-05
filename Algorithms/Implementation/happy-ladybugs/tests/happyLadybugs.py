# Dado um tabuleiro de Ladybug (joaninhas) 
# representado como uma string, você deve determinar 
# se é possível tornar as joaninhas felizes. Um 
# tabuleiro é considerado feliz quando todas as 
# joaninhas estão em posições adjacentes e cada 
# joaninha tem pelo menos uma joaninha vizinha 
# com a qual ela pode ser combinada.

# Aqui estão as regras específicas do problema:

# Um tabuleiro é representado como uma string 
# que contém joaninhas ('A' a 'Z') e espaços vazios ('_').
# Se todas as joaninhas já estiverem em posições 
# adjacentes e não houver espaços vazios, 
# o tabuleiro já é feliz.
# Se houver pelo menos uma joaninha sem 
# uma joaninha vizinha com a qual ela possa 
# ser combinada, o tabuleiro não pode ser tornado feliz.
# Se houver pelo menos um espaço vazio, 
# você pode mover qualquer joaninha para esse espaço.

# # # Função que verifica se o tabuleiro de joaninhas pode ser tornado feliz

# def happyLadybugs(b):
    
#     # Se o comprimento do tabuleiro for 1:
#     if len(b) == 1:
        
#         # Se a única célula contiver um espaço vazio '_':
#         if b == '_':
            
#             # Apenas o espaço vazio, portanto, 
#             # já é considerado feliz.
#             return 'YES'
        
#         else: 
            
#             # Se contiver uma joaninha única, não pode ser tornado feliz
#             return 'NO'
        
#     # Se houver pelo menos um espaço vazio no tabuleiro
#     if '_' in b:
        
#         # Se todos os caracteres forem espaços vazios:
#         if b.count('_') == len(b):
            
#             # Todos os espaços vazios permitem que as joaninhas estejam adjacentes, 
#             # então é feliz
#             return 'YES'
        
#         else: 
            
#             # Para cada caractere no tabuleiro:
#             for i in b:
                
#                 # Se o caractere não for um espaço vazio:
#                 if i != '_':
                    
#                     # Se houver apenas uma ocorrência dessa joaninha no tabuleiro:
#                     if b.count(i) == 1:
                        
#                         # Uma joaninha solitária não pode ser combinada, 
#                         # então o tabuleiro não é feliz
#                         return 'NO'
                    
#             # Se todas as joaninhas tiverem pelo menos uma parceira adjacente, é feliz
#             return 'YES'
        
#     else: 
        
#         # Se não houver espaços vazios, 
#         # verifica a configuração das joaninhas
#         for i in range(len(b)):
            
#             # Para o primeiro caractere no tabuleiro:
#             if i == 0:
                
#                 # Se não houver joaninha adjacente à esquerda:
#                 if b[i] != b[i + 1]:
                    
#                      # Não pode ser feliz
#                     return 'NO'
                
#             # Para o último caractere no tabuleiro:
#             elif i == len(b) - 1:
                
#                 # Se não houver joaninha adjacente à direita:
#                 if b[i] != b[i - 1]:
                    
#                     # Não pode ser feliz
#                     return 'NO'
                
#             else:
                
#                 # Se não houver joaninhas adjacentes à esquerda e à direita:
#                 if (b[i] != b[i - 1]) and (b[i] != b[i + 1]):
                    
#                     # Não pode ser feliz
#                     return 'NO'
    
#     # Se todas as condições anteriores não forem atendidas, 
#     # o tabuleiro é feliz.
#     return 'YES'


# # Função para determinar se os ladybugs podem ser tornados felizes

# def happyLadybugs(b):
    
#     # Itera sobre cada caractere no tabuleiro
#     for i in b:
        
#         # Se o caractere não for vazio '_' e aparecer apenas uma vez no tabuleiro
#         if i != '_' and b.find(i) == b.rfind(i):
            
#             # Não é possível tornar os ladybugs felizes
#             return 'NO'
        
#         # Conta quantas vezes o caractere atual aparece no tabuleiro
#         contador = b.count(i)
        
#         # Se o índice do primeiro caractere atual + a contagem do caractere - 1 for menor que o índice do último caractere atual
#         # e não houver nenhum espaço vazio '_', e.g., "AB__A"
#         if (((b.find(i) + contador) - 1) < b.rfind(i)) and b.count('_') == 0:
            
#             # Não é possível tornar os ladybugs felizes
#             return 'NO'
        
#     # Se as condições anteriores não forem atendidas, os ladybugs podem ser tornados felizes
#     return 'YES'

# # Função para determinar se os ladybugs podem ser tornados felizes

# def happyLadybugs(b):
    
#     # Lista auxiliar para armazenar diferenças entre posições de ladybugs
#     aux_dif = []
    
#     # Itera por cada caractere único no tabuleiro (conjunto para evitar repetições)
#     for i in set(b):
        
#         # Se um caractere não for vazio '_' e aparecer apenas uma vez no tabuleiro
#         if i != '_' and b.count(i) == 1:
            
#             # Não é possível tornar os ladybugs felizes
#             return 'NO'
        
#         # Se o caractere não for vazio '_':
#         if i != '_':
            
#             # Lista de índices onde o caractere aparece
#             aux = [idx for idx, valor in enumerate(b) if valor == i]
            
#             # Calcula as diferenças entre os índices
#             dif = [aux[idx + 1] - valor for idx, valor in enumerate(aux) if idx + 1 < len(aux)]
            
#             # Adiciona True se as diferenças forem todas iguais a 1
#             aux_dif.append(dif == [1] * len(dif))
            
#     # Se houver pelo menos uma verificação e todas forem True:
#     if len(aux_dif) > 0 and False not in aux_dif:
        
#         # Os ladybugs podem ser tornados felizes
#         return 'YES'
    
#     # Se não houver espaços vazios '_':
#     if '_' not in b:
        
#         # Não é possível tornar os ladybugs felizes
#         return 'NO'
    
#     else:
        
#         # Caso contrário, os ladybugs podem ser tornados felizes.
#         return 'YES'

# Função para determinar se os ladybugs podem ser tornados felizes

def happyLadybugs(b):
    
    # Itera por cada caractere único no tabuleiro (conjunto para evitar repetições)
    for i in set(b):
        
        # Se não houver espaços vazios no tabuleiro:
        if b.count('_') == 0:
            
            # Se o índice atual não for o último índice e o caractere atual não for igual ao próximo
            # OU se o caractere atual aparecer apenas uma vez no tabuleiro
            if b.index(i) !=  len(b) - 1 and i != b[b.index(i) + 1] or b.count(i) == 1:
                
                # Não é possível tornar os ladybugs felizes
                return 'NO'
        
        # Se houver pelo menos um espaço vazio '_' no tabuleiro:
        elif (b.count(i) == 1 and i != '_'):
            
            # Não é possível tornar os ladybugs felizes
            return 'NO'
            
    # Se nenhuma das condições anteriores for atendida, 
    # os ladybugs podem ser tornados felizes
    return 'YES'