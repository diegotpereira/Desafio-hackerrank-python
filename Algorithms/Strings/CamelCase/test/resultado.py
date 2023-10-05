

# A tarefa do problema "CamelCase" no HackerRank é contar o número de palavras em uma string escrita no estilo "Camel Case".

# Em "Camel Case", as palavras são escritas sem espaços, e cada palavra subsequente começa com uma letra maiúscula. Por exemplo, 
# "saveChangesInTheEditor" é uma string escrita em "Camel Case" e contém 5 palavras: "save", "Changes", "In", "The", "Editor".

# O objetivo do problema é implementar uma função chamada camelcase(s) que recebe uma string s como entrada e retorna o número de palavras 
# na string escrita em "Camel Case". A contagem de palavras é obtida identificando todas as letras maiúsculas na string.

# A função deve contar o número de letras maiúsculas na string e retornar esse valor mais 1. A adição de 1 é feita para contar a primeira palavra, 
# que não começa com uma letra maiúscula, mas é considerada uma palavra completa.

# O link fornecido leva à página do HackerRank, onde você pode encontrar o enunciado completo do problema, exemplos de entrada e saída esperada, 
# e também pode realizar a implementação da função em Python para resolver o desafio.

# def camelcase(s):
    
#     # Inicializa o contador com 1 para contar o número de palavras em camelcase.
#     contador = 1
    
#     # Loop que percorre cada caractere na string s.
#     for i in s:
        
#         # Verifica se o caractere é uma letra maiúscula.
#         if (i.isupper()):
            
#             # Se for uma letra maiúscula, incrementa o contador em 1.
#             contador += 1
            
#     # Retorna o valor do contador, que representa o número de palavras em camelcase na string s.
#     return contador


# def camelcase(s):
    
#     # Utiliza uma list comprehension para criar uma lista contendo True para cada caractere maiúsculo em s,
#     # e False para cada caractere não maiúsculo.
#     # Isso cria uma lista de booleanos indicando se cada caractere é maiúsculo ou não.
#     # Por exemplo, para a string "saveChangesInTheEditor", a lista resultante seria [False, True, ... False, True].
#     uppercase_list = [x.isupper() for x in list(s)]
    
#     # Utiliza a função sum() para somar os valores True (1) presentes na lista de booleanos.
#     # A função sum() soma todos os elementos da lista e retorna a soma total.
#     # Como cada caractere maiúsculo é representado por True (1) e cada caractere não maiúsculo é False (0),
#     # a soma representa o número de letras maiúsculas na string.
#     # Por exemplo, para a string "saveChangesInTheEditor", a soma será 5, pois há 5 letras maiúsculas.
#     uppercase_count = sum(uppercase_list)
    
#     # Incrementa o resultado da contagem em 1 para contar a primeira palavra em camelcase.
#     # Uma vez que a regra geral é que a primeira palavra não começa com letra maiúscula, mas é considerada uma palavra,
#     # adicionamos 1 ao resultado final.
#     # Por exemplo, para a string "saveChangesInTheEditor", a contagem final será 6 (5 letras maiúsculas + 1).
#     return uppercase_count + 1
    
#     # return sum([x.isupper() for x in list(s)]) + 1

# import re

# def camelcase(s):
    
#     # Cria um padrão de busca com a expressão regular '[A-Z]'.
#     # O padrão '[A-Z]' busca por letras maiúsculas na string.
#     pattern = re.compile('[A-Z]')
    
#     # Utiliza o método findall do módulo 're' para encontrar todas as ocorrências do padrão na string s.
#     # O método findall retorna uma lista com todas as letras maiúsculas encontradas na string.
#     a = re.findall(pattern, s)
    
#     # Retorna o tamanho da lista encontrada mais 1 para contar a primeira palavra em camelcase.
#     # A primeira palavra não começa com letra maiúscula, mas é considerada uma palavra, então adicionamos 1 ao resultado final.
#     return len(a) + 1


# def camelcase(s):
    
#     # Inicializa uma lista vazia para armazenar as palavras em camel case.
#     palavraLista = []
    
#     # Inicializa o índice que marcará o início de cada palavra em camel case.
#     palavra_indice = 0
    
#     # Loop que percorre cada caractere na string s usando os índices.
#     for i in range(len(s)):
        
#         # Verifica se o caractere atual é uma letra maiúscula.
#         if s[i].isupper():
            
#             # Se encontrar uma letra maiúscula, adiciona a palavra encontrada (desde a posição palavra_indice até o índice atual i)
#             # na lista de palavras em camel case.
#             palavraLista.append(s[palavra_indice : i])
            
#             # Atualiza o índice da próxima palavra em camel case para ser o índice atual i.
#             palavra_indice = i
            
#     # Após o loop, adiciona a última palavra em camel case na lista, desde o último índice marcado até o final da string.
#     palavraLista.append(s[palavra_indice])
    
#     # Retorna o tamanho da lista palavraLista, que representa o número de palavras em camel case na string s.
#     return len(palavraLista)



# def camelcase(s):
    
#     # Inicializa o contador com 1, pois a primeira palavra em camel case não começa com letra maiúscula.
#     contador = 1
    
#     # Loop que percorre cada caractere na string s.
#     for i in s:
        
#         # Verifica se o caractere atual é uma letra maiúscula.
#         if i.isupper():
            
#             # Se o caractere for uma letra maiúscula, incrementa o contador em 1.
#             contador += 1
            
#     # Retorna o valor do contador, que representa o número de palavras em camel case na string s.
#     return contador


def camelcase(s):
    
    # Inicializa a variável palavras com 1, pois a primeira palavra em camel case não começa com letra maiúscula.
    palavras = 1
    
    # Imprime o resultado da comparação entre "C" e "Z".
    # O resultado será True, porque "C" é menor que "Z" na ordem lexicográfica.
    print("C" < "Z")
    
    # Loop que percorre cada caractere na string s.
    for i in s:
        
        # Verifica se o caractere atual é uma letra maiúscula.
        if (i >= "A" and i <= "Z"):
            
            # Se o caractere for uma letra maiúscula, incrementa a variável palavras em 1.
            palavras += 1
            
    # Retorna o valor da variável palavras, que representa o número de palavras em camel case na string s.
    return palavras