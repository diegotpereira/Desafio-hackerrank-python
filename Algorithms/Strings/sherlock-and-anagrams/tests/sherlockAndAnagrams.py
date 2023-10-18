# Neste problema, a tarefa é determinar o número 
# de pares de substrings de uma string dada que 
# são anagramas entre si. Mais especificamente, 
# você precisa encontrar todos os pares de substrings 
# que têm os mesmos caracteres, mas podem estar em ordens diferentes.

# Por exemplo, considere a string "abba". Os pares 
# de substrings anagramas desta string são:

# "a" e "a"
# "b" e "b"
# "ab" e "ba"
# Note que "ab" e "ba" são considerados anagramas, 
# pois ambos consistem nas mesmas letras (a e b), 
# embora em ordens diferentes. Sua tarefa é contar 
# o número total de pares de substrings anagramas na string dada.

# # Define uma função chamada sherlockAndAnagrams que recebe uma string s como entrada.

# def sherlockAndAnagrams(s):
    
#     # Inicializa uma variável resultado para armazenar a contagem de anagramas.
#     resultado = 0
    
#     # Inicializa um dicionário substr para armazenar as substrings ordenadas e sua contagem.
#     substr = {}
    
#     # Loop externo: itera por todos os índices da string s.
#     for i in range(len(s)):
        
#         # Inicializa uma lista st para armazenar os caracteres da substring.
#         st = []
        
#         # Loop interno: itera por todos os índices de i até o final da string.
#         for j in range(i, len(s)):
            
#             # Adiciona o caractere atual à lista st.
#             st.append(str(s[j]))
            
#             # Ordena a lista st.
#             st.sort()
            
#             # Converte a lista st em uma string sr.
#             sr = ''.join(st)
            
#             # Verifica se sr não está no dicionário substr e inicializa a contagem para 0 se não estiver.
#             if (sr not in substr): substr[sr] = 0
            
#             # Incrementa a contagem da substring sr no dicionário substr.
#             substr[sr] += 1
            
#     # Loop para calcular o número de anagramas com base nas contagens das substrings.
#     for c in substr:
        
#         # Calcula o número de pares de anagramas usando a fórmula C(n, 2) = (n * (n - 1)) / 2.
#         resultado += int(((substr[c] - 1) * substr[c]) / 2)
    
#     # Retorna o resultado, que é a contagem total de pares de anagramas.
#     return resultado


# Importa a classe defaultdict do módulo collections.

# from collections import defaultdict

# # Define uma função chamada sherlockAndAnagrams que recebe uma string s como entrada.
# def sherlockAndAnagrams(s):
    
#     # Inicializa um defaultdict chamado 'anagrama' para armazenar listas de substrings ordenadas.
#     # Inicializa 'contador' para rastrear o número total de anagramas.
#     anagrama = defaultdict(list)
#     contador = 0
    
#     # Loop externo: itera por todos os índices iniciais da string s.
#     for inicial in range(len(s)):
        
#         # Loop interno: itera por todos os índices de 'inicial' até o final da string.
#         for fim in range(inicial, len(s)):
            
#             # Extrai a substring atual de 'inicial' a 'fim' da string s.
#             substr = s[inicial:fim + 1]
            
#             # Ordena os caracteres da substring e a converte em uma tupla.
#             substr_ordenada = tuple(sorted(substr))
            
#             # Adiciona a substring original à lista associada à chave 'substr_ordenada' no defaultdict 'anagrama'.
#             anagrama[substr_ordenada].append(substr)
            
#             # anagrama[tuple(sorted(substr))].append(substr)
            
#     # Loop para verificar a contagem de anagramas em cada conjunto de substrings.
#     for valor in anagrama.values():
        
#         # Se houver mais de uma substring com a mesma tupla ordenada de caracteres, há anagramas.
#         if len(valor) > 1:
            
#             # Calcula o número de anagramas usando a fórmula C(n, 2) = (n * (n - 1)) // 2.
#             atual = (len(valor) * (len(valor) - 1)) // 2
#             contador = contador + atual
            
#     # Retorna o contador, que é a contagem total de pares de anagramas.
#     return contador


# from collections import defaultdict

# # Define uma função chamada sherlockAndAnagrams que recebe uma string s como entrada.
# def sherlockAndAnagrams(s):
    
#     # Obtém o comprimento da string s.
#     n = len(s)
    
#     # Inicializa a variável 'saida' para armazenar a contagem de anagramas.
#     saida = 0
    
#     # Inicializa um defaultdict chamado 'mapa_hash' com uma função lambda que retorna 0 como valor padrão.
#     mapa_hash = defaultdict(lambda:0)
    
#     # Loop externo: itera por todos os índices i na string s.
#     for i in range(n):
        
#         # Loop interno: itera por todos os índices j a partir de i+1 até n.
#         for j in range(i + 1, n + 1):
            
#             # Cria uma substring s[i:j], ordena seus caracteres e a converte em uma string.
#             c = "".join(sorted(s[i:j]))
            
#             # Adiciona o valor atual mapeado em 'mapa_hash[c]' a 'saida'.
#             saida += mapa_hash[c]
            
#             # Incrementa o valor mapeado em 'mapa_hash[c]' em 1.
#             mapa_hash[c] += 1
            
#     # Retorna 'saida', que é a contagem total de pares de anagramas.
#     return saida


# Define uma função chamada sherlockAndAnagrams que recebe uma string s como entrada.

# def sherlockAndAnagrams(s):
    
#     # Inicializa uma variável numero_par para armazenar o número de pares de anagramas.
#     numero_par = 0
    
#     # Loop externo: itera por todos os índices, exceto o último, na string s.
#     # Este loop externo itera por todos os índices na string s, exceto o último. O motivo para 
#     # excluir o último índice é que, ao considerar substrings, precisamos de pelo menos dois 
#     # caracteres para formar um par.
#     for i in range(len(s) - 1):
        
#         # Loop intermediário: itera por todos os índices a partir de i+1 até o final da string s.
#         # O loop intermediário é aninhado dentro do loop externo. Ele itera por todos os índices 
#         # a partir do próximo índice após i até o final da string s. Isso nos permite criar todas 
#         # as possíveis combinações de substrings começando com o índice i.
#         for j in range(i + 1, len(s)):
            
#             # Loop interno: itera por todos os índices a partir de i+1 até o final da string,
#             # com um limite definido para evitar estourar o índice ao acessar s[i:j].
#             # O loop interno também é aninhado dentro do loop intermediário. Ele itera por todos 
#             # os índices a partir do próximo índice após i até um limite definido. O limite é 
#             # calculado como len(s) - len(s[i:j]) + 1 para evitar estouro de índice quando acessamos s[i:j]
#             for y in range(i + 1, len(s) - len(s[i:j]) + 1):
                
#                 # Compara se as substrings s[i:j] e s[y:(y + (j - i))] são anagramas.
#                 if sorted(s[i:j]) == sorted(s[y:(y + (j - i))]):
                    
#                     # Se as substrings forem anagramas, incrementa a contagem de pares.
#                     numero_par += 1
    
#     # Retorna o número total de pares de anagramas encontrados
#     return numero_par


def sherlockAndAnagrams(s):
    
    # Inicializa a contagem total de pares de anagramas.
    contador = 0
    
    # Cria um dicionário para rastrear as substrings ordenadas e o número de ocorrências.
    contador_substr = {}
    
    # Loop externo: itera por todos os índices na string s.
    for i in range(len(s)):
        
        # Inicializa a variável atual_substr como uma string vazia.
        # variável que é usada para construir uma substring ordenada 
        # incrementalmente à medida que percorremos a string original
        atual_substr = ''
        
        # Loop interno: itera por todos os índices a partir de i.
        for j in range(i, len(s)):
            
            # Atualiza a variável atual_substr concatenando o caractere s[j], 
            # ordenando a substring resultante e armazenando-a de volta em atual_substr.
            atual_substr = ''.join(sorted(atual_substr + s[j]))
            
            # Verifica se a substring ordenada atual (atual_substr) já existe no dicionário contador_substr.
            if atual_substr in contador_substr:
                
                # Se já existe, incrementa o contador usando o valor atual associado à substring.
                contador += contador_substr[atual_substr]
                
                # Incrementa o valor associado à substring no dicionário contador_substr.
                contador_substr[atual_substr] += 1
                
            else:
                
                 # Se a substring ordenada atual não existe no dicionário, cria uma entrada para ela com o valor 1.
                contador_substr[atual_substr] = 1
            
    # Retorna a contagem total de pares de anagramas.
    return contador