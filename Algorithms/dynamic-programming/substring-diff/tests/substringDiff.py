# Neste problema, você é desafiado a encontrar o comprimento 
# máximo de uma substring que pode ser formada em duas strings 
# dadas, S1 e S2, de modo que o número máximo de caracteres 
# diferentes entre as duas substrings seja no máximo igual a K.

# Aqui está uma visão geral da tarefa:

# Você recebe duas strings, S1 e S2, bem como um valor inteiro K.

# Sua tarefa é encontrar o comprimento máximo de uma substring 
# que pode ser formada em ambas as strings, S1 e S2, de modo 
# que o número máximo de caracteres diferentes entre as duas 
# substrings seja no máximo igual a K.

# Um caractere é considerado diferente se as substrings 
# nas posições correspondentes de S1 e S2 forem diferentes.

# Você deve retornar o comprimento máximo dessa substring 
# que atende a essa condição.

# # Importa a classe 'deque' da biblioteca 'collections'
# from collections import deque

# def substringDiff(k, s1, s2):
    
#     # Inicializa a variável 'mais_longo' para rastrear o comprimento máximo de uma substring
#     mais_longo = 0
    
#     # Loop principal que itera por possíveis deslocamentos (d) entre s1 e s2
#     for d in range(-len(s1) + 1, len(s2)):
        
#         # Calcula o índice de início em s1
#         i = max(-d, 0) + d
        
#         # Calcula o índice de início em s2
#         j = max(-d, 0)
        
#         # Inicializa um deque (fila) com tamanho máximo 'k' para armazenar índices de caracteres diferentes
#         q = deque(maxlen = k)
        
#         # Inicializa uma variável 's' para rastrear o início da substring atual
#         s = 0
        
#         # Loop que itera pelos caracteres de s1 e s2
#         for p in range(0, min(len(s2) - i, len(s1) - j)):
            
#             # Verifica se os caracteres em s1 e s2 são diferentes
#             if s1[i + p] != s2[j + p]:
                
#                 # Se o número máximo de caracteres diferentes permitidos (k) for maior que zero
#                 if k > 0:
                    
#                     # Se a fila 'q' atingir o tamanho máximo 'k', remove o elemento mais antigo
#                     if len(q) == k:
                        
#                         # Atualiza 's' para o próximo índice de início válido
#                         s = q[-1] + 1
                        
#                     # Adiciona o índice 'p' à fila 'q' para rastrear os caracteres diferentes
#                     q.append(p)
                    
#                 else:
                    
#                      # Se k for zero, atualiza 's' para o próximo índice de início válido
#                     s = p + 1 
                    
#             # Calcula o comprimento da substring atual e a compara com 'mais_longo'
#             if p + 1 - s > mais_longo:
                
#                 # Atualiza 'mais_longo' se a substring atual for mais longa
#                 mais_longo = p + 1 - s 
            
#     # Retorna o comprimento máximo da substring que atende às condições
#     return mais_longo
    
def substringDiff(k, s1, s2):
    
    return