#  tarefa do problema "Non-Divisible Subset" no HackerRank é encontrar 
# o tamanho máximo de um subconjunto que não contenha pares de elementos 
# cuja soma seja divisível por um número específico k.

# Você recebe um array de números inteiros e um número inteiro k. A 
# tarefa é determinar o tamanho máximo de um subconjunto que satisfaça 
# a seguinte condição: a soma de quaisquer dois elementos do subconjunto 
# não é divisível por k.

# O problema geralmente é resolvido em várias etapas:

# Entrada:

# Leia o número de elementos no array (n) e o valor de k.
# Leia os elementos do array.
# Contagem de Restos:

# Calcule os restos da divisão de cada elemento pelo valor de k.
# Mantenha uma contagem de quantos elementos têm cada resto.
# Construção do Subconjunto:

# Inicialize a variável max_size para 0 (o tamanho do subconjunto 
# máximo inicialmente é 0).
# Para cada resto de 1 a (k // 2), faça o seguinte:
# Se o resto é 0, adicione 1 ao max_size se houver pelo menos um 
# elemento com resto 0 (pois um número divisível por k pode ser 
# incluído apenas uma vez no subconjunto).
# Caso contrário, adicione o máximo entre a contagem de elementos 
# com o resto atual e o resto complementar (k - resto) ao max_size.
# Lidar com Resto Médio (opcional):

# Se k for par, considere também o elemento que tem o resto k // 2 
# (já que o complemento desse número é ele mesmo).
# Adicione 1 ao max_size se houver pelo menos um elemento com o 
# resto k // 2.

# Saída:

# Imprima o valor de max_size.
# O objetivo é encontrar o tamanho máximo de um subconjunto que atenda 
# às condições dadas. Essa tarefa requer uma abordagem cuidadosa para 
# contar e combinar os elementos corretos para criar um subconjunto 
# que satisfaça as condições estabelecidas.

from collections import Counter

# def nonDivisibleSubset(divisor, matriz):
#     # Calcula os restos da divisão de cada elemento pelo divisor
#     matriz = list(map(lambda x: x % divisor, matriz))
#     # Conta a ocorrência de cada resto usando o módulo 'collections.Counter'
#     contador = Counter(matriz)
#     a = 0
    
#     # Verifica se o divisor é par
#     if divisor % 2 == 0:
#         # Loop através dos contadores
#         for i in contador:
#             # Verifica se o resto é 0 ou o complemento do divisor dividido por 2
#             if i == 0 or i == divisor // 2:
#                 a += 1  # Incrementa 'a' se a condição for atendida
#             # Verifica se o contador atual é maior do que o contador complementar
#             elif contador[i] > contador.get(divisor - i, 0):
#                 a += contador[i]  # Incrementa 'a' com o contador atual
        
#         return a  # Retorna 'a' como resultado
    
#     else:
#         # Loop através dos contadores
#         for i in contador:
#             # Verifica se o resto é 0
#             if i == 0:
#                 a += 1  # Incrementa 'a' se a condição for atendida
#             # Verifica se o contador atual é maior do que o contador complementar
#             elif contador[i] > contador.get(divisor - i, 0):
#                 a += contador[i]  # Incrementa 'a' com o contador atual
    
#     return a  # Retorna 'a' como resultado


# def nonDivisibleSubset(divisor, matriz):
    
#     # Inicializa um contador de ocorrências para cada resto
#     contador = [0] * divisor
    
#     # Conta as ocorrências de cada resto
#     for num in matriz:
        
#         contador[num % divisor] += 1
        
#      # Define o resultado inicial como a ocorrência do resto 0 ou 1
#     resultado = min(contador[0], 1)
    
#     # Itera através dos restos de 1 a divisor // 2
#     for i in range(1, divisor // 2 + 1):
        
#         # Verifica se os restos i e divisor - i não são iguais
#         if i != divisor - i:
            
#             # Adiciona ao resultado o máximo entre as ocorrências dos restos i e divisor - i
#             resultado += max(contador[i], contador[divisor - i])
            
#     # Se o divisor for par, adiciona 1 ao resultado
#     if divisor % 2 == 0: 
        
#         resultado += 1 
        
#     # Retorna o resultado final
#     return resultado

from collections import defaultdict

def nonDivisibleSubset(divisor, matriz):
    
    # Verifica se o divisor é igual a 1,
    # neste caso, o subconjunto só pode conter um elemento
    if divisor == 1:
        
        # Retorna 1 pois o subconjunto tem apenas um elemento
        return 1
    
    # Cria um defaultdict para contar as ocorrências de cada resto
    dicionario = defaultdict(int)
    
    # Preenche o dicionário com as contagens de restos
    for i in matriz:
        
        # Obtém o valor atual do dicionário e incrementa a contagem
        dicionario[i % divisor] = dicionario.get(i % divisor, 0) + 1
        
    resposta = 0
    
    # Itera até divisor // 2 para verificar restos até a metade do divisor
    for i in range(divisor // 2):
        
        # Verifica o caso especial do resto 0
        if i == 0:
            
            # Se houver elementos com resto 0, aumenta a resposta
            if dicionario.get(0, 0) != 0: 
                
                resposta += 1
                
            else:
                
                # Se não houver, adiciona o máximo entre os restos i e divisor - i à resposta
                resposta += (max(dicionario.get(i, 0), dicionario.get(divisor - i, 0)))
                
    # Verifica se o divisor é ímpar
    if divisor % 2:
        
        # Adiciona o máximo entre os restos divisor // 2 e divisor - divisor // 2 à resposta
        resposta += max(dicionario.get(divisor // 2, 0), dicionario.get(divisor - divisor // 2, 0))
        
    else:
        
        # Verifica se há elementos com resto divisor // 2, e adiciona 1 à resposta se houver
        if dicionario.get(divisor // 2, 0) != 0:
            
            resposta += 1 
            
     # Retorna a resposta final
    return resposta