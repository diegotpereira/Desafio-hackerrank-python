# Divida a matriz em anéis concêntricos, começando pelo anel externo (mais próximo das bordas) e avançando para os anéis internos. Cada anel externo contém os elementos da primeira e última linha e coluna daquele anel.

# Para cada anel, armazene temporariamente seus elementos em uma lista.

# Rotacione os elementos da lista temporária em sentido anti-horário em r posições, onde r é o número de rotações solicitado.

# Insira os elementos rotacionados do anel na matriz resultante, seguindo a ordem anti-horária.

# Repita os passos 2-4 para todos os anéis.

# from collections import deque

# def matrixRotation(matrix, r):
    
#     # Define o número mínimo de círculos que precisamos percorrer
#     circles = min(len(matrix), len(matrix[0]))
    
#     # Define as dimensões da matriz
#     m, n = len(matrix), len(matrix[0])
    
#     # Cria uma cópia da matriz original
#     _matrix = matrix.copy()
    
#     # Percorre todos os círculos
#     for circle in range((int) (circles/2)):
        
#         # Define o tamanho das bordas para cada círculo
#         _m = (m - 2 * circle) - 1
#         _n = (n - 2 * circle) - 1
        
#         # Cria uma lista com os elementos da borda
#         snake = []
#         snake.extend([matrix[i][circle] for i in range(circle, circle + _m)])
#         snake.extend([matrix[circle + _m][i] for i in range(circle, circle + _n)])
#         snake.extend([matrix[i][circle + _n] for i in range(circle + _m, circle, -1)])
#         snake.extend([matrix[circle][i] for i in range(circle + _n, circle, -1)])
        
#         # Rotaciona a lista "snake" o número de vezes especificado em "r"
#         _r = r % len(snake)
#         snake = deque(snake)
#         snake.rotate(_r)
        
#         # Atualiza a matriz com os novos elementos na borda
#         idx = 0
#         for i in range(circle, circle + _m):
#             _matrix[i][circle] = snake[idx]
#             idx += 1
#         for i in range(circle, circle + _n):
#             _matrix[circle + _m][i] = snake[idx]
#             idx += 1
#         for i in range(circle + _m, circle, -1):
#             _matrix[i][circle + _n] = snake[idx]
#             idx += 1
#         for i in range(circle + _n, circle, -1):
#             _matrix[circle][i] = snake[idx]
#             idx += 1
    
#     # Retorna a matriz rotacionada        
#     return _matrix

def matrixRotation(matrix, r):
    
    # Armazena as dimensões da matriz
    n, m = len(matrix), len(matrix[0])
    
    # Função auxiliar para converter as coordenadas (i, j) em uma posição única com base na profundidade do elemento
    def to_depth_pos(i, j):
        
        # Profundidade do elemento (a distância mais curta até a borda da matriz)
        depth = min(i, j, n-i-1, m-j-1)
        
         # À esquerda (avança verticalmente)
        if j == depth:
            pos = i - depth
            
        # Na parte inferior (avança horizontalmente)
        elif i == n-1-depth:
            pos = n - 1 + j - 3*depth
            
        # À direita (recua verticalmente)
        elif j == m-1-depth:
            pos = 2*n + m - 3 - i - 5*depth
            
        # Na parte superior (recua horizontalmente)
        else:
            pos = 2*n + 2*m - 4 - j - 7*depth
        return depth, pos

    # Função auxiliar para converter uma posição única com base na profundidade do elemento em um par (i, j) de coordenadas
    def from_depth_pos(depth, pos):
        
        # Reduz a posição para um intervalo de tamanho adequado
        pos = pos % (2*(n + m - 2 - 4*depth))
        
        # À esquerda (avança horizontalmente)
        if pos < n-1-2*depth:
            j, i = depth, pos+depth
            
        # Na parte inferior (recua verticalmente)
        elif pos < n + m - 2 - 4*depth:
            i, j = n-1-depth, pos - (n - 1 - 3*depth)
            
        # À direita (recua horizontalmente)
        elif pos < 2*n + m - 3 - 6*depth:
            j, i = m-1-depth, 2*n + m - 3 - 5*depth - pos
            
        # Na parte superior (avança verticalmente)
        else:
            i, j = depth,     2*n + 2*m - 4 - 7*depth - pos
        return i, j
    
    # Inicializa a matriz de resultado
    result_matrix = []
    
    # Preenche a matriz de resultado
    for i in range(n):
        
        # Inicializa a linha atual
        row = []
        for j in range(m):
            
            # Calcula a profundidade e a posição do elemento atual
            depth, pos = to_depth_pos(i, j)
            
            # Calcula as novas coordenadas do elemento
            new_i, new_j = from_depth_pos(depth, pos-r)
            
            # Adiciona o elemento atualizado à linha
            row.append(matrix[new_i][new_j])
            
        # Adiciona a linha atualizada à matriz de resultado
        result_matrix.append(row)
    
    # Retorna a matriz de resultado final
    return result_matrix
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    resultado = matrixRotation(matrix, r)
    
    print(resultado)