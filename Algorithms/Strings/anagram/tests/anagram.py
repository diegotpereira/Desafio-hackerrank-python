# Dada uma string, você precisa determinar 
# o número mínimo de trocas de caracteres 
# necessárias para transformá-la em um anagrama. 
# Duas strings são anagramas se puderem ser 
# obtidas uma da outra reorganizando as letras, 
# mas sem adicionar ou remover caracteres.

# def anagram(palavra):
#     # Verifica se o comprimento da palavra é ímpar.
#     if len(palavra) % 2 != 0:
#         # Se o comprimento for ímpar, retorna -1, pois não é possível formar um anagrama.
#         return -1
    
#     # Calcula o índice de divisão para obter as duas metades da palavra.
#     meio = len(palavra) // 2
#     palavra1 = palavra[:meio]
#     palavra2 = palavra[meio:]
    
#     # Cria arrays para contar as ocorrências de cada letra em cada metade da palavra.
#     contar_palavra1 = [0] * 26
#     contar_palavra2 = [0] * 26
    
#     # Preenche os arrays de contagem de letras para cada metade da palavra.
#     for caracter in palavra1:
#         contar_palavra1[ord(caracter) - ord('a')] += 1
        
#     for caracter in palavra2:
#         contar_palavra2[ord(caracter) - ord('a')] += 1
        
#     # Calcula o número de trocas necessárias para tornar as metades iguais.
#     numero_trocas = 0
#     for i in range(26):
#         numero_trocas += abs(contar_palavra1[i] - contar_palavra2[i])
        
#     # Retorna o número mínimo de trocas necessárias para formar um anagrama.
#     return numero_trocas // 2


# from collections import Counter

# def anagram(s):
    
#     # Calcula o índice de divisão para obter as duas metades da string.
#     meio_indice = len(s) // 2
    
#     # Divide a string em duas partes: a primeira parte e a segunda parte.
#     primeira_parte = s[:meio_indice]
#     segunda_parte = s[meio_indice:]
    
#     # Verifica se as duas partes têm o mesmo comprimento. 
#     if len(primeira_parte) != len(segunda_parte):
        
#         # Se não, não é possível formar um anagrama e retorna -1.
#         return -1
    
#     # Calcula as contagens de ocorrências de cada caractere em cada parte da string usando a classe Counter.
#     # A classe Counter cria um dicionário de contagens de elementos em uma sequência.
#     # Subtrai as contagens de caracteres da segunda parte da contagem de caracteres da primeira parte.
#     # O resultado é um novo dicionário com as contagens de diferenças entre as duas partes.
#     # Em seguida, soma os valores do dicionário para obter o número total de trocas necessárias para formar um anagrama.
#     return sum((Counter(primeira_parte) - Counter(segunda_parte)).values())
                           
# def anagram(palavra):
    
#     # Inicializa a variável 'count' para contar o 
#     # número de trocas necessárias para formar um anagrama.
#     contador = 0
    
#     # Verifica se o comprimento da string é par.
#     if len(palavra) % 2 == 0:
        
#         # Calcula o índice de divisão para obter as 
#         # duas metades da string.
#         meio_indice = len(palavra)//2
        
#         # Divide a string em duas partes: a primeira metade (primeira_parte) 
#         # e a segunda metade (segunda_parte).
#         primeira_parte = palavra[ :meio_indice]
#         segunda_parte = palavra[meio_indice:]
        
#         # Cria uma lista de caracteres únicos na segunda metade
#         lista_caracteres_especiais = list(set(segunda_parte))
        
#         # Para cada caractere único na segunda metade (segunda_parte), 
#         # verifica se a contagem desse caractere na segunda metade
#         # é maior do que a contagem na primeira metade (primeira_parte).
#         # Se for, adiciona a diferença entre as contagens ao contador 'count'.
#         for i in lista_caracteres_especiais:
            
#             if segunda_parte.count(i) > primeira_parte.count(i):
                
#                 contador += segunda_parte.count(i) - primeira_parte.count(i)
                
#         # Retorna o número de trocas necessárias.                  
#         return contador 
    
#     else:
        
#         # Se o comprimento da string for ímpar, não 
#         # é possível formar um anagrama e retorna -1.
#         return -1


# def anagram(palavra):
    
#     # Verifica se o comprimento da palavra é ímpar.
#     if len(palavra) % 2 != 0:
        
#         # Se o comprimento for ímpar, retorna -1, 
#         # pois não é possível formar um anagrama.
#         return -1
    
#     # Calcula o índice do meio da palavra.
#     meio_indice = int(len(palavra) // 2)
    
#     # Inicializa um dicionário para armazenar as frequências
#     # dos caracteres na primeira metade da palavra.
#     lista_frequencia = {}
    
#     # Conta a frequência de cada caractere na primeira metade da palavra.
#     for i in range(0, meio_indice):
        
#         # Obtém o caractere na posição i.
#         primeira_parte = palavra[i]
        
#         # Adiciona o caractere ao dicionário de frequência ou incrementa sua contagem.
#         lista_frequencia[primeira_parte] = lista_frequencia.get(primeira_parte, 0) + 1
        
#     # Inicializa a variável 'resposta' para contar o número de trocas necessárias 
#     # para formar um anagrama.
#     resposta = 0
    
#     # Compara a frequência dos caracteres na segunda metade da palavra com a 
#     # frequência na primeira metade.
#     for i in range(meio_indice, len(palavra)):
        
#         # Obtém o caractere na posição i (segunda metade da palavra).
#         segunda_parte = palavra[i]
        
#         # Verifica se a frequência do caractere é diferente de zero no 
#         # dicionário 'lista_frequencia'.
#         # Se for diferente de zero, decrementa a contagem no dicionário.
#         # Caso contrário, adiciona 1 à variável 'resposta' para contar o 
#         # número de trocas necessárias.
#         if lista_frequencia.get(segunda_parte, 0) != 0:
            
#             lista_frequencia[segunda_parte] -= 1
            
#         else:
            
#             resposta += 1
            
#     # Retorna o número de trocas necessárias para formar um anagrama.
#     return resposta
        
from collections import Counter
        
def anagram(palavra):
    
    # Verifica se o tamanho da palavra é ímpar; nesse caso, 
    # não é possível formar anagramas
    if len(palavra) % 2 != 0:
        
        return -1
    
    # Inicializa um dicionário vazio para contagem das letras na segunda metade da palavra
    # Note que esse dicionário pode ser substituído por um Counter (que já faz a contagem automaticamente)
    # dicionario = {}
    
    # Usa o módulo Counter para contar a ocorrência de 
    # cada letra na segunda metade da palavra
    dicionario = Counter(palavra[len(palavra) // 2:])
    contador = 0
    
    # Percorre a primeira metade da palavra 
    # e tenta formar os anagramas
    for valor in palavra[:len(palavra) // 2]:
        
        # Verifica se a letra está presente no dicionário 
        # de contagem e se ela ainda tem ocorrências disponíveis
        if valor in dicionario and dicionario[valor] != 0:
            
            # Se sim, decrementa a contagem da letra no 
            # dicionário (utiliza-se uma ocorrência dela para formar o anagrama)
            dicionario[valor] -= 1
            
    # Ao final, conta quantas ocorrências de letras restaram no 
    # dicionário (indicando letras que não puderam formar anagramas)
    for valor in dicionario.values():
        
        contador += valor 
        
    return contador