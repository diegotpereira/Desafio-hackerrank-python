# Dado duas strings, a tarefa é encontrar o tamanho da sequência comum mais longa (comprimento da substring mais longa) que pode ser formada a partir das duas strings, mantendo a ordem dos caracteres. Em outras palavras, você precisa encontrar a subsequência compartilhada mais longa entre as duas strings, onde a ordem dos caracteres é preservada.

# Por exemplo, se você tem as duas strings "ABCD" e "ACDF", a sequência comum mais longa é "ACD", e seu comprimento é 3.

# O desafio consiste em implementar uma função que calcule o tamanho da sequência comum mais longa entre duas strings.


# # Define a função commonChild que recebe duas strings s1 e s2 como entrada.
# def commonChild(s1, s2):
    
#     # Obtém o comprimento das strings s1 e s2.
#     m = len(s1)
#     n = len(s2)
    
#     # Inicializa uma matriz 'resultado' de (m+1) x (n+1) preenchida com zeros.
#     resultado = [[0] * (m + 1) for _ in range(m + 1)]
    
#     # Loop externo: itera através dos caracteres da string s1.
#     for i in range(len(s1)):
        
#         # Loop interno: itera através dos caracteres da string s2.
#         for j in range(len(s2)):
            
#             # Verifica se os caracteres s1[i] e s2[j] são iguais.
#             if s1[i] == s2[j]:
                
#                 # Se forem iguais, incrementa o valor na matriz resultado[i+1][j+1] usando resultado[i][j] + 1.
#                 resultado[i + 1][j + 1] = resultado[i][j] + 1
                
#             else:
                
#                 # Se os caracteres não forem iguais, atualiza resultado[i+1][j+1] com o máximo valor entre resultado[i][j+1] e resultado[i+1][j].
#                 resultado[i + 1][j + 1] = max(resultado[i][j + 1], resultado[i + 1][j])
    
#     # Retorna o valor encontrado na última posição da matriz resultado, que representa o tamanho da sequência comum mais longa.
#     return resultado[m][n]


# # Define a função commonChild que recebe duas strings s1 e s2 como entrada.
# def commonChild(s1, s2):
    
#     # Verifica se alguma das strings é vazia ou se não há interseção entre os caracteres das duas strings.
#     if not s1 or not s2 or not set(s1).intersection(s2):
#         # Se alguma dessas condições for verdadeira, retorna 0, pois não há sequência comum.
#         return 0

#     # Obtém o comprimento das strings s1 e s2.
#     len1 = len(s1)
#     len2 = len(s2)
    
#     # Inicializa uma matriz 'dp' de (len1+1) x (len2+1) preenchida com zeros.
#     dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
#     # Loop externo: itera pelas linhas da matriz 'dp'.
#     for linha in range(1, len1 + 1):
        
#         # Loop interno: itera pelas colunas da matriz 'dp'.
#         for coluna in range(1, len2 + 1):
            
#             # Verifica se os caracteres s1[linha-1] e s2[coluna-1] são iguais.
#             if s1[linha - 1] == s2[coluna - 1]:
                
#                 # Se forem iguais, incrementa o valor na matriz 'dp[linha][coluna]' usando 'dp[linha-1][coluna-1] + 1'.
#                 dp[linha][coluna] = dp[linha - 1][coluna - 1] + 1
                
#             else:
                
#                 # Se os caracteres não forem iguais, atualiza 'dp[linha][coluna]' com o máximo valor entre 'dp[linha-1][coluna]' e 'dp[linha][coluna-1]'.
#                 dp[linha][coluna] = max(dp[linha - 1][coluna], dp[linha][coluna - 1])

#     # Retorna o valor encontrado na última posição da matriz 'dp', que representa o tamanho da subsequência comum mais longa.
#     return dp[len1][len2]

# Define a função commonChild que recebe duas strings s1 e s2 como entrada.

def commonChild(s1, s2):
    
    # Inicializa uma lista 'atual_linha' preenchida com zeros. O tamanho da lista é len(s2) + 1.
    atual_linha = [0] * (len(s2) + 1)
    
     # Loop externo: itera pelos caracteres da string s1.
    for i in range(len(s1)):
        
        # Copia a lista 'atual_linha' anterior para 'anterior_linha'.
        anterior_linha = atual_linha[:]
        
        # Loop interno: itera pelos caracteres da string s2.
        for j in range(len(s2)):
            
            # Verifica se os caracteres s1[i] e s2[j] são iguais.
            if s1[i] == s2[j]:
                
                # Se forem iguais, incrementa o valor na lista 'atual_linha[j+1]' usando '1 + anterior_linha[j]'.
                atual_linha[j + 1] = 1 + anterior_linha[j]
                
            else:
                
                # Se os caracteres não forem iguais, atualiza 'atual_linha[j+1]' com o máximo valor entre 'atual_linha[j]' e 'anterior_linha[j+1]'.
                atual_linha[j + 1] = max(atual_linha[j], anterior_linha[j + 1])
        
    # Retorna o valor encontrado na última posição da lista 'atual_linha', que representa o tamanho da subsequência comum mais longa.
    return atual_linha[len(s2)]