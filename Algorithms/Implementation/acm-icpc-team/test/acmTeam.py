# O problema "ACM ICPC Team" no HackerRank é um desafio de 
# programação que envolve o cálculo do número máximo de tópicos 
# que uma equipe pode conhecer em uma competição ACM ICPC.

# A tarefa do problema é a seguinte:

# Dada uma lista de N pessoas, onde cada pessoa é representada 
# por uma sequência binária de tamanho M, você deve encontrar o 
# número máximo de tópicos que uma equipe formada por duas pessoas 
# conhece. Além disso, você também deve determinar quantas equipes 
# diferentes podem ter o conhecimento máximo de tópicos.

# Em outras palavras, você precisa encontrar o número máximo de "1"s 
# que podem ser encontrados em qualquer par de sequências e contar 
# quantos pares têm esse número máximo de "1"s.

# A entrada do problema consiste em N linhas, representando as sequências 
# binárias das pessoas. A saída esperada é composta por dois números: o número 
# máximo de tópicos que uma equipe conhece e o número de equipes diferentes 
# que podem ter esse conhecimento máximo.

# Para resolver o problema, você precisará escrever um código em Java que faça 
# a leitura dos dados de entrada, realize os cálculos necessários e imprima a 
# saída conforme o formato especificado.


# def acmTeam(topico):
    
#     # Variáveis para armazenar o número máximo de tópicos e o número de equipes
#     max_topico = 0
#     max_time = 0

#     # Loop para percorrer todas as combinações possíveis de pares de tópicos    
#     for i in range(len(topico)):
        
#         for j in range(i + 1, len(topico)):
            
#             # Calcula o número de tópicos em comum entre os dois tópicos atuais
#             atual_topico = bin(int(topico[i], 2) | int(topico[j], 2)).count('1')
            
#             # Verifica se o número de tópicos atual é maior que o máximo encontrado até agora
#             # Se for maior, 
#             if atual_topico > max_topico:
                
#                 # atualiza o máximo de tópicos 
#                 max_topico = atual_topico
                
#                 # e redefine o número de equipes
#                 max_time = 1
            
#             # Verifica se o número de tópicos atual é igual ao máximo encontrado até agora
#             # Se for igual, 
#             elif atual_topico == max_topico:
                
#                 # incrementa o número de equipes
#                 max_time += 1
                
#     # Retorna o máximo de tópicos e o número de equipes
#     return max_topico, max_time


# def acmTeam(topico):
    
#     # Variáveis para armazenar o número máximo de tópicos e o número de times
#     max_topico = 0
#     num_times = 0
    
#     # Obtém o número de pessoas (n) 
#     n = len(topico)
    
#     # e o número de tópicos (m)
#     m = len(topico[0])
    
#     # Loop para percorrer todas as combinações possíveis de pares de pessoas
#     for i in range(n):
        
#         for j in range(i + 1, n):
            
#             # Variável para contar o número de tópicos em comum entre as duas pessoas
#             contar = 0
            
#             # Loop para percorrer todos os tópicos
#             for k in range(m):
                
#                 # Verifica se pelo menos uma das pessoas tem conhecimento no tópico atual
#                 if topico[i][k] == '1' or topico[j][k] == '1':
                    
#                     # Incrementa o contador de tópicos em comum
#                     contar += 1
                    
#                 # Verifica se o número de tópicos em comum atual é maior que o máximo encontrado até agora
#                 # Se for maior, 
#                 if contar > max_topico:
                    
#                     # atualiza o máximo de tópicos 
#                     max_topico = contar
                    
#                     # e redefine o número de times
#                     num_times = 1
                    
#                 # Verifica se o número de tópicos em comum atual é igual ao máximo encontrado até agora
#                 elif contar == max_topico:
                    
#                     # Se for igual, incrementa o número de times
#                     num_times += 1
                    
#     # Retorna o máximo de tópicos em comum e o número de times
#     return max_topico, num_times



def acmTeam(topico):
    
    # Lista para armazenar as combinações de tópicos
    n = []
    
    # Loop para percorrer todas as combinações possíveis de pares de tópicos
    for i in range(len(topico) - 1):
        
        for j in  range(i + 1, len(topico)):
            
            # Calcula a combinação bit a bit dos tópicos e converte para binário
            n.append(bin(int(topico[i], 2) | int(topico[j], 2)))
           
    # Lista para armazenar a contagem de tópicos em comum  
    t = []
    
    # Loop para contar o número de tópicos em comum para cada combinação
    for i in n:
        
        # Conta o número de '1' no valor binário e adiciona à lista t
        t.append(i.count("1"))
        
    # Encontra o valor máximo na lista t (número máximo de tópicos em comum)
    m = max(t)
    
     # Conta quantas vezes o valor máximo ocorre na lista t (número de times)
    f = t.count(m)
    
    # Cria uma tupla com o número máximo de tópicos em comum e o número de times
    novo = (m, f)
    
    # novo = []
    # novo.append(m)
    # novo.append(f)
    
    # retorna o resultado
    return novo