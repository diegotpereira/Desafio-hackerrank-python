# Priyanka gosta de brinquedos 
# e tem muitos deles. Eles estão 
# numerados de forma sequencial 
# de 1 a n. Ela gosta de arrumar 
# os brinquedos em grupos, onde 
# cada grupo contém uma série 
# de brinquedos consecutivos. A 
# diferença entre o número máximo 
# e mínimo de brinquedos em um
# grupo não deve exceder k.

# Dado o número de brinquedos 
# n e uma lista dos preços dos 
# brinquedos, determine o número 
# mínimo de grupos que Priyanka 
# pode criar enquanto segue 
# a regra mencionada.

# def toys(w):
    
#     # Ordena a lista de preços dos brinquedos em ordem crescente
#     w.sort()
    
#     # Cria uma cópia da lista de preços
#     lista_precos = w[:]
    
#     # Inicializa um contador para o número de grupos formados
#     contador = 0
    
#     # Enquanto a lista lista_precos não estiver vazia
#     while len(lista_precos) != 0:
        
#         # Incrementa o contador de grupos
#         contador += 1
        
#         # Atualiza a lista original de preços para o valor atual de l
#         w = lista_precos[:]
        
#         # Obtém o menor preço atual
#         pequeno = w[0]
        
#         # Percorre a lista de preços
#         for e in w:
            
#             # Remove o elemento da lista l se estiver dentro do limite de diferença de 4
#             if e <= pequeno + 4:
                
#                 lista_precos.remove(e)
    
#     # Retorna o número total de grupos formados
#     return contador

# def toys(w):
    
#     # Ordena a lista de preços dos brinquedos em ordem crescente
#     w.sort()
    
#     # Obtém o preço do primeiro brinquedo
#     primeiro_elemento = w[0]
    
#     # Inicializa um contador com 1 para contar o primeiro grupo formado
#     contador = 1
    
#     # Percorre a lista de preços a partir do segundo elemento
#     for i in range(1, len(w)):
        
#         # Verifica se a diferença entre o preço atual 
#         # e o primeiro preço é maior que 4
#         if w[i] - primeiro_elemento > 4:
            
#             # Atualiza o primeiro preço com o preço atual
#             primeiro_elemento = w[i]
            
#             # Incrementa o contador para formar um novo grupo
#             contador += 1
            
#     # Retorna o número total de grupos formados
#     return contador
    
# def toys(w):
    
#     # Cria uma lista ordenada com os preços dos brinquedos
#     atual_lista = list(sorted(w))
    
#     # Inicializa um contador para o número de grupos formados
#     contador = 0
    
#     # Enquanto a lista atual não estiver vazia
#     while len(atual_lista) > 0:
        
#         # Calcula o valor máximo para a largura do grupo atual
#         max_largura = atual_lista[0] + 4
        
#         # Filtra a lista para conter apenas os preços maiores que a largura máxima
#         atual_lista = [x for x in atual_lista if x > max_largura]
        
#         # Incrementa o contador de grupos
#         contador += 1
        
#         # Verifica se o contador excedeu um limite para evitar loops infinitos
#         if contador > 1000000:
            
#             break
        
#     # Retorna o número total de grupos formados
#     return contador


def toys(w):
    
    # Cria uma lista de larguras únicas 
    # ordenadas a partir dos preços dos brinquedos
    larguras = sorted(list(set(w)))
    
    # Inicializa a variável atual para 
    # armazenar o valor da largura do grupo atual
    atual = larguras[0]
    
    # Inicializa o contador de grupos com 1, 
    # pois haverá pelo menos um grupo
    contador_container = int(len(larguras) > 0)
    
    # Percorre a lista de larguras
    for elem in larguras:
        
        # Verifica se a largura do elemento 
        # atual excede a largura do grupo atual + 4
        if elem > atual + 4:
            
            # Incrementa o contador de grupos
            contador_container += 1
           
            # Atualiza o valor da largura do grupo atual para o valor do elemento
            atual = elem
    
    # Retorna o número total de grupos formados
    return contador_container