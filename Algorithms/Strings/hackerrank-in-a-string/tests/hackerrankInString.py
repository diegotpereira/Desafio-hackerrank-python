# A tarefa do problema "HackerRank in a String!" é determinar 
# se uma determinada string de entrada contém uma subsequência 
# específica que forma a palavra "HACKERRANK".

# Em outras palavras, você recebe uma string como entrada e 
# precisa verificar se é possível obter a sequência "HACKERRANK" 
# mantendo a ordem relativa dos caracteres originais. A string 
# não precisa conter todos os caracteres de "HACKERRANK", 
# mas eles devem aparecer em ordem.

# def hackerrankInString(string):
    
#     # Sequência a ser encontrada
#     sequencia = "hackerrank"
    
#     # Inicializando índices para percorrer 
#     # a string de entrada e a sequência
#     i = 0
#     j = 0
    
#     # Percorrendo a string de entrada
#     while i < len(string) and j < len(sequencia):
        
#         # Verificando se o caractere atual é igual ao caractere na sequência
#         if string[i] == sequencia[j]:
            
#             # Incrementando o índice para a próxima letra da sequência
#             j += 1
            
#         # Incrementando o índice para a próxima letra da string de entrada
#         i += 1
        
#     # Verificando se todas as letras da sequência foram encontradas em ordem
#     if j == len(sequencia):
        
#         return "YES"
    
#     else:
        
#         return "NO"


# def hackerrankInString(string):
    
#     # Definindo a sequência que queremos procurar na string de entrada
#     sequencia = "hackerrank"
    
#     # Inicializando o índice a partir do qual começaremos a procurar na string de entrada
#     inicial = 0
    
#     # Percorrendo cada letra da sequência que desejamos encontrar
#     for i in range(len(sequencia)):
        
#         # Procurando a próxima ocorrência da letra atual da sequência na string de entrada
#         indice = string.find(sequencia[i], inicial)
        
#         # Se a letra não for encontrada, retornamos 'NO', pois a sequência não pode ser formada
#         if indice == -1:
            
#             return 'NO'
        
#         # Se a letra não for encontrada, retornamos 'NO', pois a sequência não pode ser formada
#         inicial = indice + 1
        
#     # Se todas as letras da sequência foram encontradas em ordem, retornamos 'YES'
#     return "YES"


# def hackerrankInString(string):
    
#     # Definindo a sequência que queremos procurar na string de entrada
#     sequencia = 'hackerrank'
    
#     # Lista para armazenar os índices onde cada letra da sequência 
#     # é encontrada na string de entrada
#     indice_lista = []
    
#      # Índice a partir do qual começaremos a procurar na string de entrada
#     inicial = 0
    
#     # Percorrendo cada letra da sequência que desejamos encontrar
#     for letra in sequencia:
        
#         # Procurando a próxima ocorrência da letra atual da sequência 
#         # na string de entrada
#         indice = string.find(letra, inicial)
        
#         # Adicionando o índice à lista
#         indice_lista.append(indice)
        
#         # Atualizando o valor de 'inicial' para a próxima posição após 
#         # a ocorrência encontrada
#         inicial = indice + 1
        
#     # Verificando se os índices estão em ordem crescente, o que 
#     # significa que a sequência está contida em ordem na string
#     if indice_lista == sorted(indice_lista):
        
#         # Se todas as letras da sequência foram encontradas em ordem, 
#         # retornamos 'YES'
#         return 'YES'
    
#     else:
        
#         # Caso contrário, retornamos 'NO'
#         return 'NO'

# import re

# def hackerrankInString(string):
    
#     # Definindo o padrão de busca usando uma expressão regular
#     # O padrão busca a palavra 'hackerrank', mas permite caracteres alfanuméricos ou "_"
#     padrao = r"\w*".join('hackerrank')
    
#     # Utilizando a função re.search() para verificar se o padrão é encontrado na string de entrada
#     # Se o padrão for encontrado, a função re.search() retorna um objeto Match, caso contrário, retorna None
#     # Utilizando a expressão condicional para retornar 'YES' se o padrão for encontrado, caso contrário, retorna 'NO'
#     return 'YES' if re.search(padrao, string) else 'NO'


# def hackerrankInString(string):
    
#     # Palavra que queremos verificar se está contida 
#     # na string de entrada
#     palavra = 'hackerrank'
    
#     # Variável para contar o número de letras que combinam 
#     # entre a string e a palavra
#     combina = 0
    
#     # Percorrendo cada letra da string de entrada
#     for letra in string:
        
#         # Verificando se a letra atual da string combina 
#         # com a letra da palavra na posição 'combina'
#         if combina < len(palavra):
            
#             # Se a letra combinar, incrementamos 'combina' em 1
#             combina += letra == palavra[combina]
            
#     # Verificando se todas as letras da palavra foram encontradas na string
#     # Se 'combina' for igual ao comprimento da palavra, todas as letras foram encontradas
#     # Caso contrário, não foram encontradas todas as letras em ordem na string
#     return 'YES' if len(palavra) == combina else 'NO'
    

# def hackerrankInString(string):
    
#     # Palavra que queremos verificar se está contida na string de entrada
#     palavra = 'hackerrank'
    
#     # Variável para rastrear o índice da letra atual na palavra
#     j = 0
    
#     # Percorrendo cada letra da string de entrada
#     for i in string:
        
#         # Verificando se a letra atual da string 
#         # corresponde à letra atual da palavra
#         if i == palavra[j]:
            
#             # Se houver correspondência, incrementamos o índice 'j' 
#             # em 1 para comparar a próxima letra da palavra
#             j += 1
            
#          # Verificando se já percorremos toda a palavra
#         if j == len(palavra):
            
#             # Se 'j' for igual ao comprimento da palavra, isso 
#             # significa que todas as letras foram encontradas em ordem
#             # Portanto, podemos interromper o loop
#             break 
        
#     # Verificando se todas as letras da palavra foram encontradas em 
#     # ordem na string
#     return 'YES' if j == len(palavra) else 'NO'



# def hackerrankInString(string):
    
#     # Convertendo a sequência "hackerrank" 
#     # em uma lista para iterar por cada letra
#     padrao = list('hackerrank')
    
#     # Percorrendo cada letra da string de entrada
#     for i in string:
        
#         # Obtendo a primeira letra da lista de padrão
#         chave = padrao[0]
        
#         # Verificando se a letra atual da string corresponde 
#         # à primeira letra do padrão
#         if i == chave:
            
#             # Se houver correspondência, removemos a 
#             # primeira letra do padrão
#             padrao.pop(0)
            
#         # Verificando se já encontramos todas as letras do padrão na string
#         if len(padrao) == 0:
            
#             # Se a lista do padrão estiver vazia, isso significa que todas as 
#             # letras foram encontradas em ordem
#             # Portanto, retornamos 'YES'
#             return 'YES'
        
#     # Se chegarmos aqui, significa que nem todas as letras do padrão 
#     # foram encontradas na string
#     return 'NO'

# def hackerrankInString(string):
    
#     # Palavra que queremos verificar se está contida na string de entrada
#     palavra = 'hackerrank'
    
#     # Variável para rastrear o índice da letra atual na palavra
#     i = 0
    
#     # Percorrendo cada letra da string de entrada
#     for chave in string:
        
#         # Verificando se a letra atual da string corresponde à 
#         # letra atual da palavra e se não ultrapassamos o índice final da palavra
#         if chave == palavra[i] and i < 9:
            
#             # Se houver correspondência e o índice não ultrapassou o 
#             # valor 9 (última letra da palavra), 
#             # incrementamos 'i' em 1
#             i += 1
            
#     # Verificando se todas as letras da palavra foram encontradas 
#     # em ordem na string
#     if i == 9 :
        
#         # Se o valor de 'i' for igual a 9, isso significa que todas 
#         # as letras foram encontradas em ordem
#         # Portanto, retornamos 'YES'
#         return 'YES'
    
#     # Se chegarmos aqui, significa que nem todas as letras da palavra 
#     # foram encontradas na string
#     return 'NO'
    
def hackerrankInString(string):
    
    # Palavra que queremos verificar se está contida na string de entrada
    palavra = 'hackerrank'
    
    # Variável para rastrear o número de letras que combinam entre a string 
    # e a palavra
    contador = 0
    
    # Percorrendo cada índice da string de entrada até o penúltimo índice 
    # (len(string) - 1)
    for i in range(len(string) - 1):
        
        # Enquanto o contador for menor que o penúltimo índice da palavra 
        # (len(palavra) - 1)
        # E a letra atual da string for igual à letra correspondente da palavra
        while contador < len(palavra) - 1 and string[i] == palavra[contador]:
            
            # Incrementamos o contador em 1 para comparar a próxima letra da palavra
            contador += 1
            
            # Saímos do loop while utilizando 'break' após o incremento
            break 
        
    # Verificando se todas as letras da palavra foram encontradas em ordem na string
    if contador == len(palavra) - 1:
        
        # Se o contador for igual a len(palavra) - 1, isso significa que todas as 
        # letras foram encontradas em ordem
        # Portanto, retornamos 'YES'
        return 'YES'
    
    else: 
        
        # Se chegarmos aqui, significa que nem todas as letras da palavra 
        # foram encontradas na string
        # Portanto, retornamos 'NO'
        return 'NO'