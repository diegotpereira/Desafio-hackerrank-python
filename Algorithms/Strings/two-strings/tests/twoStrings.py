# A tarefa do problema "Two Strings" no HackerRank é determinar se 
# há pelo menos uma substring comum entre duas strings.

# Dada uma quantidade q de pares de strings, a entrada do problema consiste 
# em q linhas, onde cada linha contém duas strings, string1 e string2. A tarefa 
# é verificar para cada par de strings se existe ao menos uma substring comum entre elas.

# Uma substring é uma sequência contígua de caracteres em uma string. Por exemplo, 
# na string "banana", "ana" e "ban" são substrings.

# A saída deve ser um array de strings, onde cada elemento é "YES" se existir uma  
# substring comum entre string1 e string2, ou "NO" se não existir.


# def twoStrings(string1, string2):
    
#     # Utilizando uma list comprehension para verificar se existe ao menos uma substring de string2 presente em string1
#     # Para isso, itera-se sobre cada substring (string3) em string2
#     # A expressão 'string3 in string1' verifica se a substring string3 está presente em string1
#     # A função any() retorna True se pelo menos uma substring for encontrada em string1
#     # Caso exista uma substring comum, a função retorna "YES"; caso contrário, retorna "NO"
#     return "YES" if any([string3 in string1 for string3 in string2]) else "NO"


# def twoStrings(string1, string2):
    
#     # Iterando sobre cada caractere (res) presente em string2
#     for res in string2:
        
#         # Verificando se o caractere (res) está presente em string1
#         if res in string1:
            
#             # Se o caractere estiver presente em string1, retorna "YES"
#             return "YES"
        
#     # Caso nenhum caractere de string2 esteja presente em string1, retorna "NO"
#     return "NO"

# def twoStrings(string1, string2):
    
#     # Criando conjuntos (sets) a partir de string1 e 
#     # string2 para obter os caracteres únicos em cada uma
#     set_string1 = set(string1)
#     set_string2 = set(string2)
    
#     # Utilizando o método intersection dos conjuntos para 
#     # verificar a interseção (caracteres comuns) entre os dois conjuntos
#     # Se a interseção for não vazia (ou seja, se houver 
#     # pelo menos um caractere em comum), retorna "YES"
#     # Caso contrário, se a interseção for vazia 
#     # (não houver caracteres em comum), retorna "NO"
#     return "YES" if set(set_string1).intersection(set(set_string2)) else "NO"

# def twoStrings(string1, string2):
    
#     # Iterando sobre cada caractere único (i) presente em string1, 
#     # obtendo um conjunto (set) de caracteres únicos
#     for i in set(string1):
        
#         # Verificando se o caractere (i) está presente em string2
#         if i in string2:
            
#             # Se o caractere estiver presente em string2, retorna "YES"
#             return "YES"
        
#     # Caso nenhum caractere de string1 esteja presente em string2, retorna "NO"
#     return "NO"


def twoStrings(string1, string2):
    
    # Convertendo string1 em um conjunto (set) de caracteres únicos usando list comprehension
    # Em seguida, fazendo a interseção entre o conjunto de string1 e o conjunto de string2
    # O resultado é um conjunto que contém os caracteres que são comuns a ambas as strings
    resultado = set([*string1]).intersection(set([*string2]))
    
    # Verificando se o conjunto resultado é não vazio (ou seja, se há pelo menos um caractere comum)
    # Se o conjunto não estiver vazio, retorna "YES", caso contrário, retorna "NO"
    return 'YES' if resultado else 'NO'