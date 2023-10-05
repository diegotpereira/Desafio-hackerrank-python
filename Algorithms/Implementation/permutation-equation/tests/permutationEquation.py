# Dada uma sequência de números inteiros de 1 a N, 
# onde N é o tamanho da sequência, você deve calcular
# a função inversa da sequência dada. Em outras 
# palavras, para cada valor i na sequência, você 
# precisa encontrar o índice j tal que p(p(j)) = i, 
# onde p é a função inversa.

# A entrada consiste em duas linhas:

# A primeira linha contém um número inteiro N, 
# representando o tamanho da sequência.
# A segunda linha contém N inteiros separados 
# por espaço, representando a sequência.
# Você deve imprimir os valores de j, um por 
# linha, que satisfazem a condição p(p(j)) = i 
# para cada valor i de 1 a N.

# A saída, portanto, é uma lista de inteiros, 
# onde cada inteiro representa um índice j 
# correspondente ao valor i da sequência.


# def permutationEquation(p):
    
#      # Lista para armazenar os resultados
#     res = []
    
#     # Dicionário para mapear valores para suas localizações (índices + 1)
#     dicionario_locacao = {}
    
#     # Preenchendo o dicionário com valores e suas localizações
#     for i, num in enumerate(p):
        
#         # O valor é a chave, a localização é o valor + 1
#         dicionario_locacao[num] = i + 1
        
#     # Iterando através dos valores de 1 a N
#     for i in range(1, len(p) + 1):
        
#         # Encontrando a primeira localização usando o dicionário
#         primeiro = dicionario_locacao[i]
        
#         # Encontrando a segunda localização usando o dicionário
#         segundo = dicionario_locacao[primeiro]
        
#         # Adicionando o resultado à lista de resultados
#         res.append(segundo)
    
#     # Retornando a lista de resultados
#     return res


# def permutationEquation(p):
    
#     # Dicionário para armazenar o mapeamento de valor para índice
#     dicionario_indices = dict()
    
#     # Lista para armazenar os resultados
#     lista_resultados = list()
    
#     # Preenchendo o dicionário com mapeamento de valores para índices
#     for i in range(len(p)):
        
#          # A chave é o valor p[i], o valor é i + 1
#         dicionario_indices[p[i]] = i + 1
        
#     # Variável para armazenar o resultado intermediário
#     resultado_intermediario = int()
    
#     # Iterando através dos valores de 1 a N
#     for e in range(len(p)):
        
#         # Encontrando o valor de índice associado ao valor e + 1 usando o dicionário
#         resultado_intermediario = dicionario_indices[e + 1]
        
#         # Encontrando o valor de índice associado ao valor resultado_intermediario usando o dicionário novamente
#         resultado_intermediario = dicionario_indices[resultado_intermediario]
        
#         # Adicionando o valor de índice resultado_intermediario à lista de resultados
#         lista_resultados.append(resultado_intermediario) 
        
#     # Retornando a lista de resultados
#     return lista_resultados


def permutationEquation(p):
    
    # Lista para armazenar os resultados
    lista = []
    
    # Iterando através dos valores de 1 a N
    for i in range(1, len(p) + 1):
        
        # Encontrando o índice do valor i no array p (valor do índice + 1 é o valor desejado)
        # Em seguida, encontrando o índice do resultado anterior para obter j
        # Adicionando 1 para converter índice baseado em zero para índice baseado em um
        resultado = p.index(p.index(i) + 1) + 1
        
        # Adicionando o resultado à lista de resultados
        lista.append(resultado)
        
    # Retornando a lista de resultados
    return lista