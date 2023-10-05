# Dado um array de segmentos, você precisa 
# encontrar o perímetro máximo de um triângulo 
# que pode ser formado usando três segmentos desse array.

# Você receberá um número inteiro positivo, n, 
# que representa o número de segmentos. Em seguida, 
# você receberá n inteiros positivos representando 
# os comprimentos dos segmentos.

# Sua tarefa é encontrar três segmentos que 
# possam ser usados para formar um triângulo 
# de perímetro máximo. Se vários triângulos de 
# perímetro máximo forem possíveis, você deve 
# imprimir o que tem o maior valor. Se não for 
# possível formar um triângulo, você deve imprimir "-1".

# def maximumPerimeterTriangle(gravetos):
    
#     # Ordena os comprimentos dos gravetos em ordem decrescente
#     gravetos.sort(reverse=True)
    
#     # Percorre a lista de gravetos, exceto os últimos dois elementos
#     for i in range(len(gravetos) - 2):
        
#         # Verifica se os comprimentos dos gravetos formam um triângulo válido
#         if gravetos[i] < gravetos[i + 1] + gravetos[i + 2]:
            
#             # Se formar um triângulo válido, retorna os comprimentos em ordem decrescente
#             return [gravetos[i + 2], gravetos[i + 1], gravetos[i]]
    
#     # Se não for possível formar um triângulo válido, retorna [-1]
#     return [-1]

# def maximumPerimeterTriangle(gravetos):
    
#     # Ordena os comprimentos dos gravetos em ordem decrescente
#     gravetos.sort(reverse=True)
    
#     # Cria uma lista vazia para armazenar os lados do triângulo
#     lista = []
    
#     # Percorre a lista de gravetos, 
#     # até o penúltimo elemento
#     for i in range(len(gravetos) - 2) :
        
#         # Verifica se os comprimentos dos gravetos formam um triângulo válido
#         if (gravetos[i] < gravetos[i + 1] + gravetos[i + 2]):
            
#             # Adiciona os comprimentos dos lados do triângulo à lista
#             lista.append(gravetos[i])
#             lista.append(gravetos[i + 1])
#             lista.append(gravetos[i + 2])
            
#             # Para a verificação, 
#             # já que encontramos o triângulo de maior perímetro
#             break 
        
#     # Ordena a lista com os lados do triângulo em ordem crescente
#     lista.sort()
    
#     # Verifica se há lados válidos na lista
#     if (len(lista) > 0):
        
#         # Retorna os lados do triângulo em ordem crescente
#         return lista 
    
#     else:
        
#         # Se não for possível formar um triângulo, 
#         # retorna [-1]
#         lista.append(-1)
        
#         return lista

def maximumPerimeterTriangle(gravetos):
    
    # Ordena os comprimentos dos gravetos em ordem decrescente
    gravetos.sort(reverse=True)
    
    # Percorre a lista de gravetos, 
    # até o penúltimo elemento
    for i in range(len(gravetos) - 2):
        
        # Atribui os comprimentos dos lados do triângulo a variáveis
        a, b, c = gravetos[i], gravetos[i + 1], gravetos[i + 2]
        
        # Verifica se os comprimentos dos lados formam um triângulo válido
        if a < b + c:
            
            # Se formar um triângulo válido, retorna os comprimentos em ordem decrescente
            return [c, b, a]
        
    # Se não for possível formar um triângulo válido, retorna [-1]
    return [-1]