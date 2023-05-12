# A tarefa do problema "Find Digits" é encontrar 
# e contar os dígitos de um número que são divisíveis 
# por ele próprio. Dado um número inteiro, o objetivo é 
# determinar quantos dígitos do número são exatamente divisíveis 
# por ele. O problema fornece um número inteiro positivo e solicita 
# a contagem dos dígitos que são divisíveis pelo número original. 
# A saída esperada é o número de dígitos que atendem a essa condição.


def findDigits(n):
    
    # Variável para contar os dígitos de 'n' que são divisíveis por 'n'
    conte = 0
    
    # Converte o número 'n' em uma tupla de dígitos
    l = tuple(str(n))
    
    # Percorre cada dígito na tupla
    for i in l:
        
        # Verifica se o dígito é igual a 0
        if int(i) == 0:
            
            # Se for 0, pula para a próxima iteração
            continue
        
        else:
            
            # Verifica se 'n' é divisível pelo dígito atual
            if n % int(i) == 0:
                
                # Incrementa o contador se for divisível
                conte += 1
                
    # Retorna o contador
    return conte


# def findDigits(n):
    
#     # Retorna a soma de 1 para cada dígito diferente de zero em 'n'
#     # e que é um divisor de 'n'
#     return sum(1 for i in str(n) if i != '0' and n % int(i) == 0)


# def findDigits(n):
    
#      # Variável para contar os dígitos de 'n' que são divisíveis por 'n'
#     contar = 0

#      # Converte o número 'n' em uma lista de dígitos
#     res =list(map(int, str(n)))
    
#     # Percorre cada dígito da lista
#     for i in range(len(res)):
        
#         try:
            
#              # Verifica se o dígito é divisível por 'n'
#             if n % res[i] == 0:
              
#                # Incrementa o contador se for divisível
#               contar += 1
              
#         except:
            
#             # Exibe uma mensagem de "zero division" caso ocorra uma exceção de divisão por zero
#             print("zero division")
    
#     # Retorna o contador
#     return contar

