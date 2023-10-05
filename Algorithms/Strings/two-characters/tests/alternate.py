# No problema "Two Characters" do HackerRank, a tarefa é a seguinte:

# Dada uma string contendo apenas letras minúsculas, você deve encontrar 
# o comprimento da maior subcadeia possível, onde apenas duas letras 
# distintas estão presentes e essas letras se alternam.

# Por exemplo, se a string for "abaacdabd", então a maior subcadeia 
# possível que atende aos critérios é "abab" com comprimento 4. A subcadeia 
# "abaacdabd" não atende aos critérios porque possui mais de duas letras.

# A sua tarefa é escrever um código para determinar o comprimento da maior 
# subcadeia que satisfaz essas condições. Caso não seja possível formar uma 
# subcadeia com duas letras alternadas, você deve retornar 0.


# def alternate(s):
    
#     # Cria um conjunto com as letras distintas presentes na string 's'
#     letras_distintas = set(s)
    
#     # Inicializa o tamanho máximo da subcadeia como 0
#     tamanho_maximo = 0
    
#     # Loop para selecionar a primeira letra do par de letras
#     for primeira_letra in letras_distintas:
        
#         # Loop para selecionar a segunda letra do par de letras
#         for segunda_letra in letras_distintas:
            
#             # Verifica se as letras selecionadas são diferentes
#             if primeira_letra != segunda_letra:
                
#                 # Remove todas as outras letras da string 's', mantendo apenas as duas letras do par sendo testado
#                 temp_string = ''.join(c for c in s if c == primeira_letra or c == segunda_letra)
                
#                 # Verifica se a string resultante possui caracteres alternados
#                 if eh_alternativa(temp_string):
                    
#                     # Atualiza o tamanho máximo da subcadeia, se necessário
#                     tamanho_maximo = max(tamanho_maximo, len(temp_string))
    
#     # Retorna o tamanho máximo da subcadeia
#     return tamanho_maximo

# def eh_alternativa(string):
    
#     # Loop para verificar se existem caracteres iguais consecutivos na string
#     for i in range(len(string) - 1):
        
#         if string[i] == string[i + 1]:
            
#             # Se houver caracteres iguais consecutivos, a string não é considerada alternativa
#             return False
        
#     # Se não houver caracteres iguais consecutivos, a string é considerada alternativa
#     return True


# def alternate(s):
    
#     # Cria uma lista com os caracteres únicos presentes na string 's'
#     unico_caracter = list(set(s))
    
#     # Variável para armazenar temporariamente a nova string formada pelas letras alternadas
#     nova_string = ''
    
#     # Lista para armazenar os tamanhos das subcadeias formadas pelas letras alternadas
#     tamanho = []
    
#     # Loop para selecionar o primeiro caractere do par de letras
#     for i in range(len(unico_caracter)):
        
#         # Loop para selecionar o segundo caractere do par de letras
#         for j in range(i + 1, len(unico_caracter)):
            
#             # Cria uma string temporária com os dois caracteres selecionados
#             tmp_string = unico_caracter[i] + unico_caracter[j]
            
#             # Loop para percorrer a string original 's' e manter apenas as letras do par sendo testado
#             for k in s:
                
#                 if k in tmp_string:
                    
#                     nova_string += k
                    
#             # Armazena o tamanho da nova string formada pelas letras alternadas
#             tamanho.append(len(nova_string))
            
#             # Verifica se a nova string possui caracteres consecutivos iguais
#             for j in range(len(nova_string) - 2):
                
#                 if nova_string[j] != nova_string[j + 2]:
                    
#                     # Se houver caracteres consecutivos iguais, remove o tamanho da nova string da lista 'tamanho'
#                     tamanho.remove(len(nova_string))
                    
#                     break
                
#             # Reseta a nova_string para a próxima iteração do loop
#             nova_string = ''
            
#     # Verifica se a lista de tamanhos está vazia, o que indica que não foi possível formar uma subcadeia alternada
#     if len(tamanho) == 0:
        
#         return 0
    
#     else:
        
#         # Retorna o maior tamanho encontrado na lista 'tamanho'
#         return max(tamanho)
    
    
    
def alternate(s):
    
    # Cria uma lista com os caracteres únicos presentes na string 's'
    lista_caracteres = list(set(s))
    
    # Variável para armazenar o tamanho máximo da subcadeia com letras alternadas
    maximo = 0
    
    # Loop para selecionar o primeiro caractere do par de letras
    for i in range(len(lista_caracteres)):
        
        # Loop para selecionar o segundo caractere do par de letras, 
        # começando da posição i + 1 para evitar repetições
        for j in range(i + 1, len(lista_caracteres)):
            
            # String temporária para armazenar os caracteres 
            # selecionados na ordem em que aparecem na string original
            z = ""
            
            # Loop para percorrer a string original 's' e manter apenas os caracteres do par sendo testado
            for k in range(len(s)):
                
                if s[k] == lista_caracteres[i] or s[k] == lista_caracteres[j]:
                    
                    z += s[k]
                    
            # Verifica se a nova string 'z' possui letras alternadas
            if len(z) > maximo and len(set(z[::2])) == 1 and len(set(z[1::2])) == 1:
                
                # Se a nova string é maior que a subcadeia atual e possui letras alternadas, 
                # atualiza o tamanho máximo
                maximo = len(z)
                
    # Retorna o tamanho máximo da subcadeia com letras alternadas                
    return maximo