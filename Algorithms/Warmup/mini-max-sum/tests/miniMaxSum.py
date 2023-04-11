# def miniMaxSum(arr):
    
#     soma_total = sum(arr)
    
#     soma_minima = soma_total - max(arr)
#     soma_maxima = soma_total - min(arr)
    
#     return (soma_minima, soma_maxima)

# def miniMaxSum(arr):
    
#     tamanho = len(arr)
#     maxResultado = 0
#     minResultado = 0
    
#     arr.sort()
    
#     for i in range(tamanho - 1):
        
#         minResultado += arr[i]
        
#     for i in range(1, tamanho):
        
#         maxResultado += arr[i]

#     return (minResultado, maxResultado)

def miniMaxSum(arr):
    
    arr.sort()
    
    # a função retorna a tupla com as somas calculadas usando slicing. 
    return (sum(arr[:-1]), sum(arr[1:]))
    
if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split()))
    
    
    resultado = miniMaxSum(arr)
    
    print(resultado)
    
    