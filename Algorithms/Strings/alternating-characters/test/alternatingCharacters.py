# A tarefa do problema no link fornecido é chamada 
# de "Alternating Characters" (Caracteres Alternados). 
# O problema é o seguinte: dado uma string contendo 
# apenas os caracteres 'A' e 'B', você precisa determinar 
# o número mínimo de caracteres que devem ser deletados 
# para que a string resultante contenha apenas caracteres alternados.

# Por exemplo, se a string fornecida for "AAAA", é necessário 
# deletar três caracteres para que reste apenas um "A". Se a 
# string for "ABABABAB", não é necessário deletar nenhum caractere, 
# pois a string já contém caracteres alternados.

# O objetivo é implementar uma função que recebe a string como 
# entrada e retorna o número mínimo de caracteres que precisam 
# ser deletados.


# def alternatingCharacters(s):
    
#     # Inicializa uma pilha vazia para armazenar os caracteres
#     pilha = []
    
#     # Inicializa um contador para contar 
#     # o número de caracteres repetidos
#     contador = 0
    
#     # Percorre cada caractere na string
#     for a in s:
        
#         # Se a pilha estiver vazia, não há 
#         # caracteres para comparar ainda
#         if not pilha:
            
#             pass
        
#          # Se o caractere atual for igual ao caractere 
#          # no topo da pilha, significa que há uma repetição
#         elif (a == pilha[-1]):
            
#             # Incrementa o contador de caracteres repetidos
#             contador += 1
            
#         # Adiciona o caractere atual à pilha
#         pilha.append(a)
        
#     # Retorna o contador de caracteres repetidos
#     return contador


# def alternatingCharacters(s):
    
#     # Inicializa o contador de caracteres deletados
#     deletados = 0
    
#     # Inicializa a variável para armazenar o caractere anterior
#     previa = ''
    
#     # Percorre cada letra na string
#     for letra in s:
        
#         # Se a variável 'previa' está vazia, guarda a letra como a 'previa'
#         if previa == '':
            
#             previa = letra
            
#         else: 
            
#             # Se a letra atual for igual à 'previa', 
#             # incrementa o contador de caracteres deletados
#             if previa == letra:
                
#                 deletados += 1
                
#             else:
                
#                 # Se a letra atual for diferente da 'previa', 
#                 # atualiza a 'previa' para a letra atual
#                 previa = letra
                
#     # Retorna o número de caracteres deletados                
#     return deletados


def alternatingCharacters(s):
    
    # Inicializa o contador de caracteres deletados
    contador = 0
    
    # Converte a string em uma lista de caracteres
    lista = list(s)
    
    # Percorre a string até o penúltimo caractere
    for i in range(len(s) -1):
        
        # Verifica se o caractere atual 
        # é igual ao próximo caractere
        if s[i] == s[i + 1]:
            
            # Incrementa o contador de caracteres deletados
            contador += 1
            
            # Remove o caractere atual da lista
            lista.remove(s[i])
            
    # Imprime a lista de caracteres resultante
    print(lista)
    
    # Retorna o contador de caracteres deletados
    return contador