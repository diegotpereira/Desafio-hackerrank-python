# A tarefa do problema "Closest Numbers" no HackerRank 
# é encontrar os pares de números em um array que têm a 
# menor diferença entre eles e, em seguida, imprimir 
# esses pares em ordem crescente.

# Aqui está um resumo da tarefa:

# Você recebe um array de números inteiros não ordenados.
# Sua tarefa é encontrar todos os pares de números no 
# array que têm a menor diferença entre eles.
# Imprima esses pares de números em ordem crescente.

# def closestNumbers(arr):
    
#     # Crie uma lista chamada 'diferenca' para armazenar 
#     # as diferenças entre os elementos adjacentes
#     diferenca = []
    
#     # Ordene o array em ordem crescente
#     arr.sort()
    
#     # Calcule as diferenças entre elementos adjacentes 
#     # e adicione-as à lista 'diferenca'
#     for i in range(len(arr) - 1):
        
#         diferenca.append(arr[i + 1] - arr[i])
        
#     # Encontre a menor diferença na lista 'diferenca'
#     minima_diferenca = min(diferenca)
    
#     # Crie uma lista chamada 'resposta' para armazenar 
#     # os pares com a menor diferença
#     resposta = []
    
#     # Percorra as diferenças e adicione os elementos 
#     # adjacentes com a menor diferença à lista 'resposta'
#     for i in range(len(diferenca)):
        
#         if diferenca[i] == minima_diferenca:
            
#             resposta.append(arr[i])
#             resposta.append(arr[i + 1])
    
#     # Retorne a lista 'resposta' contendo os pares com a menor diferença
#     return resposta

def closestNumbers(arr):
    
    # Ordene o array em ordem crescente
    arr.sort()
    
    # Inicialize a menor diferença como infinito positivo
    minima_diferenca = float('inf')
    
    # Inicialize a lista 'resultado' para armazenar os 
    # pares com a menor diferença
    resultado = []
    
    # Percorra o array, comparando elementos adjacentes 
    # para encontrar a menor diferença
    for i in range(len(arr) - 1):
        
        # Calcule a diferença entre elementos adjacentes
        diferenca = arr[i] - arr[i + 1]
        
         # Verifique se a diferença absoluta é menor 
         # que a menor diferença atual
        if abs(diferenca) < minima_diferenca:
            
            # resultado = []
            # resultado.extend([arr[i] , arr[i + 1]])
            
            # Se sim, redefina a lista 'resultado' para conter apenas os elementos atuais
            resultado = [arr[i], arr[i + 1]]
            
        # Se a diferença absoluta for igual à menor diferença atual, 
        # adicione os elementos à lista 'resultado'
        if abs(diferenca) == minima_diferenca:
            
            resultado.extend([arr[i], arr[i + 1]])
            
        # Atualize a menor diferença com o mínimo entre a menor diferença atual e a diferença absoluta
        minima_diferenca = min(minima_diferenca, abs(diferenca))
        
    # Retorne a lista 'resultado' contendo os pares com a menor diferença
    return resultado