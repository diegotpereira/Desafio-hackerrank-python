# Dada uma grade (ou matriz) de caracteres, 
# você precisa determinar se é possível 
# reorganizar as colunas dessa grade de modo 
# que cada coluna seja uma sequência não 
# decrescente de caracteres.

# Você pode trocar as colunas da matriz 
# entre si, mas não pode trocar os caracteres 
# dentro de uma coluna.

# def gridChallenge(grade):
    
#     # Iterando sobre as linhas da grade
#     for i in range(len(grade)):
        
#         # Ordenando os caracteres da linha 
#         # atual em ordem crescente
#         grade[i] = sorted(grade[i])
        
#     # Iterando sobre as colunas da grade
#     for coluna in range(len(grade[0])):
        
#         # Iterando sobre as linhas, começando da segunda linha
#         for linha in range(1, len(grade)):
            
#             # Verificando se o caractere na linha atual e coluna 
#             # atual é menor que o caractere na linha anterior e coluna atual
#             if grade[linha][coluna] < grade[linha - 1][coluna]:
                
#                 # Se a condição acima for verdadeira, 
#                 # retorna 'NO' indicando que a reorganização não é possível
#                 return 'NO'
    
#     # Se todas as colunas podem ser reorganizadas, 
#     # retorna 'YES'
#     return 'YES'


# 'def gridChallenge(grade):
    
#     # Inicializando uma lista 'pedido' com caracteres 
#     # 'a' do mesmo tamanho das colunas da grade
#     pedido = ['a' for j in range(len(grade[0]))]
    
#     # Iterando sobre as linhas da grade
#     for linha in range(len(grade)):
        
#         # Ordenando os caracteres da linha atual 
#         # em ordem crescente
#         grade[linha] = sorted(list(grade[linha]))
        
#         # Iterando sobre as colunas da linha atual
#         for coluna in range(len(grade[linha])):
            
#             # Verificando se o caractere na coluna atual é maior 
#             # que o caractere correspondente na lista 'pedido'
#             if pedido[coluna] > grade[linha][coluna]:
                
#                 # Se a condição acima for verdadeira, 
#                 # retorna 'NO' indicando que a 
#                 # reorganização não é possível
#                 return 'NO'
            
#             # Atualizando o caractere correspondente na lista 
#             # 'pedido' para o caractere atual
#             pedido[coluna] = grade[linha][coluna]
            
#     # Se todas as colunas podem ser reorganizadas, 
#     # retorna 'YES'
#     return 'YES''

# def gridChallenge(grade):
    
#     # Iterando sobre as linhas da grade (exceto a última linha)
#     for linha in range(len(grade) - 1):
        
#         # Iterando sobre as colunas da linha atual
#         for coluna in range(len(grade[linha])):
            
#             # Convertendo as strings das linhas em listas de caracteres
#             grade[linha] = list(grade[linha])
#             grade[linha + 1] = list(grade[linha + 1])
            
#             # Ordenando os caracteres da linha atual e da próxima 
#             # linha em ordem crescente
#             grade[linha].sort()
#             grade[linha + 1].sort()
            
#             # Verificando se o caractere na coluna atual da linha 
#             # atual é maior que o caractere correspondente na coluna da próxima linha
#             if grade[linha][coluna] > grade[linha + 1][coluna]:
                
#                 return 'NO'
            
#             # Encerrando o loop interno após a primeira verificação
#             break 
        
#     # Se todas as comparações forem bem-sucedidas, retorna 'YES'
#     return 'YES'
            
# def gridChallenge(grade):
    
#     # Criando um gerador de expressão que ordena cada linha da grade individualmente
#     classificar_linhas = (sorted(linha) for linha in grade)
    
#     # Transpondo as linhas para obter as colunas ordenadas
#     colunas = zip(* classificar_linhas)
    
#     # Verificando se todas as colunas estão em ordem crescente
#     em_ordem = all(coluna == tuple(sorted(coluna)) for coluna in colunas)
    
#     # Retorna 'YES' se todas as colunas estiverem em ordem, caso contrário, retorna 'NO'
#     return 'YES' if em_ordem else 'NO'


def gridChallenge(grade):
    
    # Ordenando cada linha da grade individualmente
    f = [sorted(x) for x in grade]
    
    # Transpondo as linhas ordenadas para obter as colunas
    c = list(zip(*f))
    
    # Iterando sobre as colunas
    for i in range(len(c)):
        
        # Verificando se a coluna ordenada é igual à coluna original
        if tuple(sorted(c[i])) != c[i]:
            
            # Se a condição acima for verdadeira, 
            # retorna 'NO' indicando que a reorganização não é possível
            return 'NO'
        
    # Se todas as colunas estiverem em ordem, 
    # retorna 'YES'
    return 'YES'