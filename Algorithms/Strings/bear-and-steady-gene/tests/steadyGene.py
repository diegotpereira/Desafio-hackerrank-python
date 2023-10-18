# Dado uma sequência de letras que representam 
# genes, a tarefa é encontrar o menor tamanho 
# de uma subsequência contígua que, quando 
# removida da sequência original, torna a 
# frequência de cada gene (letra) dentro da 
# sequência restante igual a um valor específico 
# (chamado de valor de frequência alvo). O objetivo 
# é ajustar a sequência original de modo que 
# ela tenha uma distribuição igual de cada gene.

# Em outras palavras, você precisa encontrar o 
# tamanho mínimo de uma janela (subsequência contígua) 
# que, quando removida da sequência original, faz com 
# que a frequência de cada gene na sequência resultante 
# seja igual ao valor de frequência alvo.


# # Define a função steadyGene que recebe uma string s como entrada.

# def steadyGene(gene):
    
#     # Inicializa um dicionário 'freqs' para contar a frequência de cada gene (A, C, G, T).
#     freqs = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
#     # Loop para percorrer a string s e atualizar a contagem de frequência de cada gene.
#     for ch in gene:
        
#         freqs[ch] += 1
        
#     # Inicializa os índices i e j para controlar a janela deslizante e a variável 'min_tamanho'.
#     i = 0
#     j = 0
    
#     # Inicializa 'min_tamanho' com um valor infinito.
#     min_tamanho = float('inf')
    
#     # Calcula o valor alvo de frequência (1/4 do comprimento da string).
#     l4 = len(gene) // 4
    
#     # Loop para ajustar a janela deslizante e encontrar o menor tamanho da subsequência.
#     while i < len(gene) and j < len(gene):
        
#         # Verifica se a frequência de algum gene (A, C, G, T) é maior que o valor alvo.
#         if any(freqs[ch] > l4 for ch in 'ACGT'):
            
#             # Reduz a contagem de frequência do gene no final da janela.
#             freqs[gene[j]] -= 1
#             j += 1
            
#         else:
            
#             # Calcula o tamanho da janela atual e atualiza 'min_tamanho' se necessário.
#             min_tamanho = min(min_tamanho, j - i)
            
#             # Aumenta a contagem de frequência do gene no início da janela.
#             freqs[gene[i]] += 1
#             i += 1
    
#     # Retorna o tamanho mínimo da subsequência que atende às condições especificadas.
#     return min_tamanho


# Importa a classe Counter do módulo collections para contar as ocorrências de caracteres.
from collections import Counter

# Define a função smallest_substring que recebe uma string a como entrada.
def steadyGene(a):
    # Usa o Counter para contar as ocorrências de cada caractere na string a.
    c = Counter(a)
    
    # Inicializa variáveis para contar as ocorrências de cada gene (A, C, T, G).
    if 'A' in c:
        s1 = c['A']
    else:
        s1 = 0
    if 'C' in c:
        s2 = c['C']
    else:
        s2 = 0
    if 'T' in c:
        s3 = c['T']
    else:
        s3 = 0
    if 'G' in c:
        s4 = c['G']
    else:
        s4 = 0

    # Inicializa variáveis Min e Max para controlar os índices da menor substring.
    Min = -1
    Max = -1

    # Inicializa uma variável count para rastrear o tamanho mínimo da substring.
    count = 0

    # Calcula o valor alvo n (1/4 do comprimento da string a).
    n = len(a) // 4

    # Verifica se a string a já atende aos critérios de frequência.
    if s1 == n and s2 == n and s3 == n and s4 == n:
        return 0

    # Inicializa um dicionário tmp para rastrear os índices de excesso de caracteres.
    tmp = {}
    key = False

    # Verifica quais genes (A, C, T, G) têm ocorrências em excesso e rastreia seus índices.
    if s1 > n:
        tmp['A'] = [-1] * (s1 - n)
    if s2 > n:
        tmp['C'] = [-1] * (s2 - n)
    if s3 > n:
        tmp['T'] = [-1] * (s3 - n)
    if s4 > n:
        tmp['G'] = [-1] * (s4 - n)

    # Loop para percorrer a string a.
    for i in range(len(a)):
        # Verifica se o caractere a[i] está em tmp (representando um gene com excesso de ocorrências).
        if a[i] in tmp:
            if key:
                Max = i
                tmp[a[i]].append(i)
                # Verifica se o primeiro índice na lista é igual a Min.
                if tmp[a[i]][0] == Min:
                    # Remove o primeiro índice da lista.
                    del tmp[a[i]][0]

                    # Calcula o novo valor de Min como o mínimo entre o primeiro índice de todos os genes em tmp.
                    Min = min([Tmp[0] for Tmp in tmp.values()])

                    # Atualiza count se a diferença entre Max e Min for menor que o valor atual de count.
                    if Max - Min < count:
                        count = Max - Min
                else:
                    # Remove o primeiro índice da lista.
                    del tmp[a[i]][0]

                    # Atualiza count se a diferença entre Max e Min for menor que o valor atual de count.
                    if Max - Min < count:
                        count = Max - Min
            else:
                Max = i
                tmp[a[i]].append(i)
                # Remove o primeiro índice da lista.
                del tmp[a[i]][0]

                # Calcula o novo valor de Min como o mínimo entre o primeiro índice de todos os genes em tmp.
                Min = min([Tmp[0] for Tmp in tmp.values()])

                # Verifica se o valor de Min é maior ou igual a 0.
                if Min >= 0:
                    # Atualiza count como a diferença entre Max e Min.
                    count = Max - Min
                    key = True

    # Retorna count + 1, que representa o tamanho mínimo da substring que atende aos critérios especificados.
    return count + 1
