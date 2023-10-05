# Lisa adora trabalhar em problemas de 
# matemática de seu livro de exercícios. 
# Ela segue um método específico:

# 1. Ela começa na primeira página do livro 
# de exercícios.
# 2. Ela resolve os problemas naquela página 
# e avança para a próxima página.
# 3. Ela segue esse padrão até o final do livro.
# Cada capítulo do livro contém um número variável 
# de problemas. Dado o número de capítulos em seu 
# livro, o número de problemas em cada capítulo e a 
# quantidade de problemas que Lisa deseja resolver 
# por página, você deve determinar quantas vezes 
# sua página de exercícios atual contém o número 
# do problema da página.

# Mais formalmente, você será dado o número de 
# capítulos em seu livro (n), um array representando 
# o número de problemas em cada capítulo, e a 
# quantidade de problemas por página (k). Você 
# deve determinar quantas vezes um número de 
# problema corresponde ao número da página.

# def workbook(numero_capitulos, numero_maximo_problemas_por_pagina, problemas_capitulo):
   
#     # Inicializando uma lista para armazenar os números de páginas com problemas especiais. 
#     problema_especial = []
    
#     # Inicializando uma variável para contar o número da página atual.
#     contar_pagina = 1
    
#     # Loop pelos capítulos, começando a partir do capítulo 1 até o número total de capítulos
#     for capitulo in range(1, numero_capitulos + 1):
        
#         # Obtendo o número de problemas no capítulo atual
#         sem_problemas = problemas_capitulo[capitulo - 1]
        
#         # Calculando o número de "subcapítulos" necessários para abranger todos os problemas do capítulo
#         numero_capitulos_por_capitulo = (sem_problemas + numero_maximo_problemas_por_pagina - 1) // numero_maximo_problemas_por_pagina
        
#         # Calculando o número total de problemas que serão abordados nos subcapítulos
#         problemas_maximos = numero_maximo_problemas_por_pagina * numero_capitulos_por_capitulo
        
#         # Loop pelos problemas no capítulo atual
#         for i in range(1, sem_problemas + 1):
            
#             # Verificando se o número do problema coincide com o número da página atual
#             if i == contar_pagina:
                
#                 # Adicionando o número da página à lista de problemas especiais
#                 problema_especial.append(contar_pagina)
                
#             # Verificando se é necessário avançar para a próxima página
#             if (i % numero_maximo_problemas_por_pagina == 0):
                
#                 # Incrementando o número da página
#                 contar_pagina += 1
                
#             # Verificando se o último problema do capítulo foi alcançado e se ainda não ultrapassou o número máximo de problemas
#             if (sem_problemas == i) and (i < problemas_maximos):
                
#                 # Incrementando o número da página
#                 contar_pagina += 1
    
#     # Retornando o número total de problemas especiais encontrados
#     return len(problema_especial)


def workbook(numero_capitulos, numero_maximo_problemas_por_pagina, problemas_capitulo):
    
    # Inicializando a variável para rastrear a página atual
    pagina_atual = 1
    
    # Inicializando a variável para armazenar a resposta final
    resposta = 0
    
    # Loop pelos números de problemas em cada capítulo
    for num in problemas_capitulo:
        
        # Inicializando um contador para 
        # os problemas dentro do capítulo
        i = 1
        
        # Enquanto o contador for menor 
        # ou igual ao número total de problemas no capítulo
        while i <= num:
            
            # Verificando se a última página possível para esta série de 
            # problemas é maior do que o número total de problemas no capítulo
            if i + numero_maximo_problemas_por_pagina - 1 > num:
                
                # Verificando se a página atual está dentro do intervalo 
                # de problemas para essa série de problemas
                if i <= pagina_atual <= num:
                    
                    # Incrementando a resposta, pois esta é uma página com um problema especial
                    resposta += 1
                
            # Caso contrário, verificando se a página atual está dentro do intervalo 
            # de problemas para essa série de problemas
            elif i <= pagina_atual <= i + numero_maximo_problemas_por_pagina - 1:
                
                # Incrementando a resposta, pois esta é uma página com um problema especial
                resposta += 1 
                
            # Avançando o contador para o próximo conjunto de problemas na próxima página
            i += numero_maximo_problemas_por_pagina
            
            # Avançando a página atual
            pagina_atual += 1
            
    # Retornando a resposta final
    return resposta