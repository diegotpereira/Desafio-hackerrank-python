# def sockMerchant(n, ar):
    
#     # inicializa a variável que vai contar o número total de pares
#     total_par = 0
    
#     # itera sobre o conjunto de meias únicas na lista
#     for meia in set(ar):
        
#         # conta quantas vezes a meia atual aparece na lista
#         contar_meia = ar.count(meia)
        
#         # divide o número de meias daquele tipo por dois para obter o número de pares
#         contar_par = contar_meia // 2
        
#         # adiciona a quantidade de pares encontrados à variável total_par
#         total_par += contar_par
        
#     # retorna o número total de pares encontrados
#     return total_par
        
# def sockMerchant(n, ar):
    
#     # cria um dicionário vazio
#     dic = {}
    
#     # cria uma variável para armazenar o resultado final    
#     res = 0
    
#     # percorre a lista de meias
#     for i in ar:
        
#         # se a meia já está no dicionário
#         if i in dic:
            
#             # adiciona 1 na quantidade
#             dic[i] += 1
            
#             # se a quantidade de meias daquele tipo é par
#             if dic[i] % 2 == 0:
                
#                 # incrementa o resultado final
#                 res += 1
                
#         # se a meia ainda não está no dicionário
#         else:

#             # adiciona com quantidade 1
#             dic[i] = 1
            
#     # retorna o resultado final
#     return res


# def sockMerchant(n, ar):
    
#     # Criação de variáveis para contagem
#     contar = 0
#     soma = 0
    
#     # Criação de uma lista sem elementos repetidos
#     a = list(set(ar))
    
#     # Loop para cada elemento da lista sem repetição
#     for i in range(len(a)):
        
#         # Loop para percorrer a lista original
#         for j in range(n):
            
#             # Verifica se o índice é válido e se o elemento é igual ao elemento atual da lista sem repetição
#             if j < len(ar) and a[i] == ar[j]:
#                 contar += 1
                
#         # Calcula a quantidade de pares e adiciona à variável de soma
#         soma = contar // 2 + soma
        
#         # Reseta a variável de contagem
#         contar = 0
      # Retorna a quantidade total de pares encontrados
#     return soma


from collections import Counter


def sockMerchant(n, ar):
    
    # Cria um dicionário com a contagem de cada elemento da lista
    contar = Counter(ar)
    
    # Variável para guardar a quantidade de pares
    pares = 0
    
    # Cria um conjunto com os números presentes na lista
    numeros = set(ar)
    
    # Itera pelos números presentes na lista
    for num in numeros:
        
        # Divide a contagem do número por 2 e adiciona à variável 'pares'
        pares += contar[num] // 2
        
    # Retorna a quantidade total de pares encontrados
    return pares

if __name__ == "__main__":
    
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    resultado = sockMerchant(n, ar)

    print(str(resultado) + '\n')