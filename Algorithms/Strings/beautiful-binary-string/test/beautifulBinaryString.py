# A tarefa do problema no link fornecido é 
# chamada de "Beautiful Binary String" (String Binária Bonita). 
# O problema é o seguinte: dada uma string binária, você precisa 
# determinar o número mínimo de alterações necessárias para tornar 
# a string "bonita". Uma string binária é considerada "bonita" se 
# não contiver a substring "010".

# Por exemplo, se a string fornecida for "0101010", é necessário 
# alterar o segundo "1" para obter a string "0101010". Nesse caso, 
# apenas uma alteração é necessária para tornar a string "bonita".

# O objetivo é implementar uma função que recebe a string binária 
# como entrada e retorna o número mínimo de alterações necessárias 
# para tornar a string "bonita".


# def beautifulBinaryString(b):
    
#     # Retorna a contagem de ocorrências da substring "010" na string b
#     return b.count("010")


# def beautifulBinaryString(b):
    
#     # Define a substring a ser buscada
#     sub = '010'
    
#     # Inicializa o contador de alterações
#     contador = 0

#     # Inicializa o índice para percorrer a string
#     i = 0
    
#     # Percorre a string até o penúltimo caractere
#     while i < len(b) -2:
        
#         # Verifica se a substring a partir do índice atual começa com '010'
#         if b[i:].startswith(sub):
            
#             # Incrementa o contador de alterações
#             contador += 1
            
#             # Pula três caracteres após a ocorrência de '010'
#             i += 3
            
#         else: 
            
#             # Avança para o próximo caractere
#             i += 1
            
#     # Retorna o número de alterações
#     return contador


# def beautifulBinaryString(b):
    
#     # Substitui todas as ocorrências de '010' por 'x' na string
#     b = b.replace('010', 'x')
    
#     # Retorna a contagem de ocorrências da letra 'x' na string
#     return b.count('x')


import re


# def beautifulBinaryString(b):
    
#     # Compila a expressão regular '010' em um padrão de busca
#     p = re.compile('010')
    
#     # Encontra todas as ocorrências de '010' na string b
#     v = p.findall(b)
    
#     # Retorna o número de ocorrências encontradas
#     return len(v)



def beautifulBinaryString(b):
    
    # Converte a string em uma lista de caracteres
    b = list(b)
    
    # Inicializa o contador de alterações
    contador = 0
    
    # Percorre a lista até o penúltimo caractere
    for i in range(len(b) - 2):
        
        # Verifica se a sequência atual é '010'
        if b[i] == '0' and b[i + 1] == '1' and b[i + 2] == '0':
            
            # Substitui o último '0' por '1'
            b[i + 2] = '1'
            
            # Incrementa o contador de alterações
            contador += 1
            
    # Retorna o número de alterações
    return contador