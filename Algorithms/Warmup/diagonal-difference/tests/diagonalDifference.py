


def diagonalDifference(arr):
    
     # Inicializa as variáveis `i` e `j`
    i = 0
    j = len(arr) - 1
    
    # Inicializa as variáveis `soma_esquerda` e `soma_direita`
    soma_esquerda = 0
    soma_direita = 0
    
    # Loop para somar os elementos das diagonais principais e secundárias
    while i < len(arr) and j >= 0:
        
        # Soma o valor do elemento na posição `[i][i]` da matriz `arr` à variável `soma_esquerda`
        soma_esquerda = soma_esquerda + arr[i][i]
        # Soma o valor do elemento na posição `[i][j]` da matriz `arr` à variável `soma_direita`
        soma_direita = soma_direita + arr[i][j]
        
        # Atualiza os índices de `i` e `j`
        i += 1
        j -= 1
        
    # Retorna a diferença absoluta entre as somas das diagonais principais e secundárias
    return abs(soma_esquerda - soma_direita)

# def diagonalDifference(arr):
    
#     # Inicializa as variáveis a e b com zero
#     a = 0
#     b = 0
    
#     # Percorre a matriz arr usando um loop for e soma os elementos das diagonais
#     for i in range(len(arr)):
        
#         # Soma o elemento da diagonal principal
#         a += arr[i][i]
#         # Soma o elemento da diagonal secundária
#         b += arr[i][-1 - i]
    
#     # Retorna a diferença absoluta entre as somas das diagonais
#     return abs(a - b)

if __name__ == "__main__":
    
    # Solicita a entrada do tamanho da matriz
    n = int(input().strip())
    
     # Inicializa a lista vazia arr
    arr = []
    
     # Solicita a entrada dos elementos da matriz
    for _  in range(n):
        
        # Converte a entrada em uma lista de inteiros e adiciona à lista arr
        arr.append(list(map(int, input().rstrip().split())))
    
    # Chama o método diagonalDifference para a matriz arr e armazena o resultado na variável resultado
    resultado = diagonalDifference(arr)
    
    # Imprime o resultado na tela   
    print(' '.join(map(resultado)))