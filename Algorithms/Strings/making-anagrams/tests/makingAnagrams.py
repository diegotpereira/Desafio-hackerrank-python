# A tarefa do problema "Making Anagrams" 
# no HackerRank é determinar o número 
# mínimo de caracteres que precisam ser 
# deletados de duas strings para que elas 
# se tornem anagramas. Uma anagrama é uma 
# palavra ou frase formada pela reorganização 
# das letras de outra palavra ou frase, 
# usando todas as letras originais exatamente 
# uma vez. Em outras palavras, duas palavras 
# são anagramas se possuírem as mesmas letras, 
# mas em ordens diferentes.

# O problema fornece duas strings como entrada 
# e pede para calcular a quantidade mínima de 
# caracteres que devem ser removidos em ambas 
# as strings para que elas se tornem anagramas. 
# Por exemplo, se as strings de entrada forem 
# "abc" e "cde", a resposta seria 4, pois 
# teríamos que remover duas letras "a" e "b" 
# da primeira string e duas letras "d" e "e" 
# da segunda string para que ambas se tornem 
# anagramas da string "c".

# def makingAnagrams(string1, string2):
    
#     # Inicializa um contador para contar o número mínimo de 
#     # caracteres a serem removidos para formar anagramas
#     contador = 0
    
#     # Loop através dos caracteres únicos presentes na primeira 
#     # string (conjunto de caracteres)
#     for i in set(string1):
        
#         # Verifica se o caractere da primeira string também 
#         # está presente na segunda string
#         if i in string2:
            
#             # Se o caractere estiver presente nas duas strings, adiciona a diferença absoluta das contagens
#             # desse caractere em cada string ao contador (ou seja, a quantidade de vezes que esse caractere
#             # aparece em uma string, mas não na outra)
#             contador += abs(string1.count(i) - string2.count(i))
            
#         else:
            
#             # Se o caractere não estiver presente na segunda string, adiciona a contagem desse caractere na
#             # primeira string ao contador, pois precisamos remover todas as ocorrências desse caractere na
#             # primeira string para torná-la um anagrama da segunda string
#             contador += string1.count(i)
            
#     # Loop através dos caracteres únicos presentes na segunda string (conjunto de caracteres)
#     for i in set(string2):
        
#         # Verifica se o caractere da segunda string não está presente na primeira string
#         if i not in string1:
            
#             # Se o caractere não estiver presente na primeira string, adiciona a contagem desse caractere na
#             # segunda string ao contador, pois precisamos remover todas as ocorrências desse caractere na
#             # segunda string para torná-la um anagrama da primeira string
#             contador += string2.count(i)
            
#     # Retorna o contador com a quantidade mínima de caracteres a serem removidos para formar anagramas
#     return contador
    
# from collections import defaultdict

# def makingAnagrams(string1, string2):
    
#     # Criando um dicionário usando a classe defaultdict, 
#     # onde o valor padrão para novas chaves é 0
#     dicionario = defaultdict(int)
    
#     # Iterando sobre os caracteres da string1
#     for c in string1:
        
#         # Incrementando o valor associado 
#         # ao caractere no dicionário
#         dicionario[c] += 1
        
#     # Iterando sobre os caracteres da string2
#     for c in string2:
        
#         # Decrementando o valor associado 
#         # ao caractere no dicionário
#         dicionario[c] -= 1
        
#     # Retornando a soma dos valores absolutos de todas as entradas no dicionário
#     return sum(abs(v) for k, v in dicionario.items())


# def makingAnagrams(string1, string2):
    
#     # Criando listas para armazenar as contagens 
#     # dos caracteres em ambas as strings
#     palavra1 = [0] * 26
#     palavra2 = [0] * 26
    
#     # Variável para armazenar o resultado final
#     resposta = 0
    
#     # Iterando sobre os caracteres da string1
#     for letra in string1:
        
#         # Incrementando a contagem do caractere 
#         # no índice correspondente da lista palavra1
#         palavra1[ord(letra) - 97] += 1
        
#     # Iterando sobre os caracteres da string2
#     for letra in string2:
        
#         # Incrementando a contagem do caractere no 
#         # índice correspondente da lista palavra2
#         palavra2[ord(letra) - 97] += 1
        
#     # Comparando as contagens dos caracteres nas 
#     # duas listas e calculando a resposta final
#     for i in range(26):
        
#          # Adicionando a diferença absoluta entre 
#          # as contagens à resposta
#         resposta += abs(palavra1[i] - palavra2[i])
        
#     # Retornando o resultado final
#     return resposta


# def makingAnagrams(string1, string2):
    
#     # Inicializando a variável de resposta com zero
#     resposta = 0
    
#     # Criando um conjunto (set) string3 que contém 
#     # todos os caracteres únicos presentes em string1 e string2
#     string3 = set(string1 + string2)
    
#     # Iterando sobre cada caractere presente no conjunto string3
#     for i in string3:
        
#         # Adicionando à resposta a diferença absoluta entre as 
#         # contagens do caractere em string2 e string1
#         resposta += abs(string2.count(i) - string1.count(i))
        
#     # Retornando a resposta final
#     return resposta


# def makingAnagrams(string1, string2):
    
#     # Inicializando a variável de resposta com zero
#     resposta = 0
    
#     # Concatenando as duas strings em string3
#     string3 = string1 + string2
    
#     # Convertendo a string3 para um conjunto (set) 
#     # para obter os caracteres únicos presentes nas duas strings
#     # Em seguida, transformando o conjunto de volta 
#     # em uma lista para iterar sobre seus elementos
#     for i in list(set(string3)):
        
#         # Verificando se a contagem do caractere i em 
#         # string1 é maior do que a contagem em string2
#         if string1.count(i) > string2.count(i):
            
#             # Se for maior, adiciona a diferença entre 
#             # as contagens à resposta
#             resposta += string1.count(i) - string2.count(i)
            
#         # Verificando se a contagem do caractere i em string1 
#         # é menor do que a contagem em string2
#         elif string1.count(i) < string2.count(i):
            
#             # Se for menor, adiciona a diferença entre as contagens à resposta
#             resposta += string2.count(i) - string1.count(i)
            
#     # Retornando a resposta final
#     return resposta



def makingAnagrams(string1, string2):
    
    # Criando um conjunto (set) string3 
    # contendo os caracteres únicos presentes em string1
    string3 = set(string1)
    
    # Inicializando a variável contador com zero
    contador = 0
    
    # Iterando sobre os caracteres únicos presentes 
    # em string1 (conjunto string3)
    for i in string3:
        
        # Verificando se a contagem do caractere i em 
        # string1 é igual à contagem em string2
        if string1.count(i) == string2.count(i):
            
            # Se forem iguais, adiciona a contagem 
            # de i em string2 ao contador
            contador += string2.count(i)
            
        # Verificando se a contagem do caractere i em 
        # string1 é maior do que a contagem em string2
        elif string1.count(i) > string2.count(i):
            
            # Se for maior, adiciona a contagem de i em 
            # string2 ao contador
            contador += string2.count(i)
            
        # Verificando se a contagem do caractere i em 
        # string2 é maior do que a contagem em string1
        elif string2.count(i) > string1.count(i):
            
            # Se for maior, adiciona a contagem de i em 
            # string1 ao contador
            contador += string1.count(i)
            
    # Calculando o número mínimo de caracteres a serem removidos para tornar as duas strings anagramas
    # A fórmula ((len(string1) + len(string2)) - contador * 2) representa a soma dos comprimentos das strings 
    # menos o dobro do contador (que contém a soma das contagens dos caracteres comuns nas duas strings)
    return ((len(string1) + len(string2)) - contador * 2) 