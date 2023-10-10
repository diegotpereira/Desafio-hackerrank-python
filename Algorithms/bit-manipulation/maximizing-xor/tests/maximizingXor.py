
# Você recebe dois números inteiros, L e R. A tarefa 
# é encontrar o valor máximo de XOR (ou exclusivo ou) 
# entre dois números inteiros, A e B, onde L <= A <= B <= R.

# Em outras palavras, você precisa encontrar dois números 
# inteiros, A e B, dentro do intervalo [L, R], de modo que 
# o resultado de A XOR B seja o maior possível.

# Definindo a função maximizingXor com dois parâmetros, l e r.

# def maximizingXor(l, r):
    
#     # Inicializando a variável maximo com 0 
#     # para rastrear o valor máximo encontrado.
#     maximo = 0
    
#     # Iterando sobre todos os valores de i no intervalo de l a r (inclusive).
#     for i in range(l, r + 1):
        
#         # Iterando sobre todos os valores de j no intervalo de i a r (inclusive).
#         for j in range(i, r + 1):
            
#             # Calculando o XOR (ou exclusivo ou) entre i e j e atualizando maximo se o resultado for maior.
#             maximo = max(maximo, i ^ j)
            
#     # Retornando o valor máximo encontrado após as iterações.
#     return maximo


# # Importando a função 'combinations' do módulo 'itertools'.
# from itertools import combinations

# # Definindo a função 'maximizingXor' com dois parâmetros, 'l' e 'r'.
# def maximizingXor(l, r):
    
#     # Inicializando a variável 'axb' para rastrear o valor máximo de A XOR B encontrado.
#     axb = 0
    
#     # Iterando através de todas as combinações possíveis de dois números no intervalo [l, r].
#     for i in combinations(range(l, r + 1), 2):
        
#         # Calculando o XOR entre os dois números na combinação atual e atualizando 'axb' se o resultado for maior.
#         axb = max(axb, i[0] ^ i[1])
        
#     # Retornando o valor máximo de A XOR B encontrado.
#     return axb

# Definindo a função 'maximizingXor' com dois parâmetros, 'l' e 'r'.

def maximizingXor(l, r):
    
    # Inicializando uma lista 'res' para armazenar os resultados de A XOR B.
    res = []
    
    # Loop para iterar por todos os valores de 'a' no intervalo [l, r].
    for a in range(l, r + 1):
        
        # Loop aninhado para iterar por todos os valores de 'b' no intervalo [l, r].
        for b in range(l, r + 1):
            
            # Calculando o resultado de 'a' XOR 'b' e adicionando-o à lista 'res'.
            res.append(a ^ b)
            
    # Retornando o valor máximo encontrado na lista 'res'.
    return max(res)