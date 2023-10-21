# Dados um conjunto de números inteiros 
# e um valor inteiro alvo, sua tarefa é 
# determinar o número de pares de elementos 
# no conjunto cuja diferença seja igual ao valor alvo.

# Em termos matemáticos, você recebe um 
# array de inteiros e um número inteiro k. 
# Sua tarefa é encontrar o número de pares 
# de elementos (i, j) no array onde i ≠ j 
# e a diferença entre os elementos a[i] 
# e a[j] seja igual a k. Em outras palavras, 
# você precisa contar quantos pares de 
# números no array têm uma diferença igual a k.


# def pairs(diferenca, arr):
    
#     # Inicialize um contador para rastrear o número de pares que atendem ao critério
#     contador = 0
    
#     # Crie um conjunto a partir da lista `arr` para otimizar a pesquisa de elementos
#     conjunto_inteiros = set(arr)
    
#     # Itera através dos números na lista `arr`
#     for num in arr:
        
#         # Verifica se num - diferenca NÃO está no conjunto de inteiros
#         if num - diferenca not in conjunto_inteiros:
            
#             # Se não estiver, continue para o próximo número na lista
#             continue
        
#         # Se num - diferenca estiver no conjunto de inteiros
#         else:
            
#             # aumente o contador em 1
#             contador += 1
    
    
#     return contador

# def pairs(diferenca, arr):
    
#     # Inicialize um contador para rastrear o número de pares que atendem ao critério.
#     contar_pares = 0
    
#     # Ordene a lista 'arr' em ordem crescente para otimizar a busca binária.
#     arr = sorted(arr)
    
#     # Itere pelos elementos da lista 'arr'.
#     for i in arr:
        
#         # Verifique se i + diferença está na lista 'arr'.
#         if i + diferenca in arr:
            
#             # Se a diferença existe na lista, aumente o contador de pares em 1.
#             contar_pares += 1
            
#     return contar_pares

# def pairs(diferenca, arr):
    
#     # Inicialize um dicionário para rastrear os elementos do array 'arr'.
#     arr_dict = dict()
    
#     # Inicialize um contador para rastrear o número de pares que atendem ao critério.
#     contador = 0
    
#     # Itere pelos elementos da lista 'arr'.
#     for i in arr:
        
#         # Verifique se i + diferença existe no dicionário.
#         if arr_dict.get(i + diferenca):
            
#             # Se a diferença existe no dicionário, aumente o contador em 1.
#             contador += 1
            
#         # Verifique se i - diferença existe no dicionário.
#         if arr_dict.get(i - diferenca):
            
#             # Se a diferença existe no dicionário, aumente o contador em 1.
#             contador += 1
            
#         # Adicione o elemento atual 'i' ao dicionário, usando 'i' como a chave e o próprio 'i' como o valor.
#         arr_dict[i] = i 
        
#     return contador


# def pairs(diferenca, arr):
    
#     # Crie um conjunto a partir da lista 'arr' para otimizar a pesquisa de elementos.
#     conjunto_set = set(arr)
    
#     # Inicialize uma lista 'par' para armazenar pares que atendem ao critério.
#     par = [(avaliar, avaliar + diferenca) for avaliar in conjunto_set if avaliar + diferenca in conjunto_set]
    
#     # Retorne o comprimento da lista 'par', que representa o número de pares encontrados.
#     return len(par)

# def pairs(diferenca, arr):
    
#     # Crie um novo array 'novo_arr' que contém os elementos originais de 'arr'
#     # e também elementos criados subtraindo 'diferenca' de cada elemento em 'arr'.
#     novo_arr = arr + [i - diferenca for i in arr]
    
#     # Crie um conjunto 'reducao' a partir do 'novo_arr' para eliminar elementos duplicados.
#     reducao = set(novo_arr)
    
#     # Retorne a diferença entre o comprimento do 'novo_arr' original e o comprimento do 'reducao',
#     # que representa o número de elementos únicos no 'novo_arr'.
#     return len(novo_arr) - len(reducao)


def pairs(diferenca, arr):
    
    # Crie um conjunto a partir da lista 'arr' para eliminar elementos duplicados.
    # Crie um novo conjunto contendo elementos que, quando somados a 'diferenca',
    # estão presentes no conjunto original 'arr'.
    # Use a função 'intersection' para encontrar a interseção entre os dois conjuntos
    # e, em seguida, obtenha o comprimento dessa interseção, que representa o número de pares encontrados.
    return len(set(arr).intersection(set(x + diferenca for x in arr)))