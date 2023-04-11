from collections import deque


# def matrixRotation(matrix, r):
#     # Write your code here
    
#     print(matrix)
#     # print(r)
#     circles = min(len(matrix), len(matrix[0]))
    
#     m, n = len(matrix), len(matrix[0])
    
#     _matrix = matrix.copy()
#     for circle in range((int) (circles/2)):
#         _m = (m - 2 * circle) - 1
#         _n = (n - 2 * circle) - 1
        
#         # print(_m,_n, circle)
#         snake = []
#         snake.extend([matrix[i][circle] for i in range(circle, circle + _m)])
#         snake.extend([matrix[circle + _m][i] for i in range(circle, circle + _n)])
#         snake.extend([matrix[i][circle + _n] for i in range(circle + _m, circle, -1)])
#         snake.extend([matrix[circle][i] for i in range(circle + _n, circle, -1)])
#         # print(snake)
        
#         _r = r % len(snake)
#         snake = deque(snake)
#         snake.rotate(_r)
        
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
    
#     # print(_matrix)
#     for i in range(m):
#         print(" ".join([str(x) for x in _matrix[i]]))

# def matrixRotation(matrix, r):


#     m = len(matrix)
#     n = len(matrix[1])
#     # m2 = [([0] * n) for i in range(m)]

#     number_of_rings = min(int(m/2), int(n/2))

#     m_rings = []
#     n_rings = []

# #creating a list of ring indexes
    
#     for i in range(number_of_rings):
#         elements_in_a_ring = 2*n + 2*(m-2)
#         m_arr = []
#         n_arr = []

#         for j in range(n):
#             m_arr.append(i)
#             n_arr.append(n-j-1+i)
#         for j in range(m-1):
#             m_arr.append(j+1+i)
#             n_arr.append(i)
#         for j in range(n-1):
#             m_arr.append(m-1+i)
#             n_arr.append(j+1+i)
#         for j in range(m-2):
#             m_arr.append(m-j-2+i)
#             n_arr.append(n-1+i)
    
#     #Rotating index ring by r
		
#         m_arr = [m_arr[(i-r) % len(m_arr)] for i, x in enumerate(m_arr)]
#         n_arr = [n_arr[(i-r) % len(n_arr)] for i, x in enumerate(n_arr)]
#         m_rings.append(m_arr)
#         n_rings.append(n_arr)
#         m -= 2
#         n -= 2

#     # print(f"m rings after: {m_rings}")
#     # print(f"n rings after : {n_rings}")

#     m = len(matrix)
#     n = len(matrix[1])
#     matr2 = [([0] * n) for i in range(m)]
    
# #assign the data to the new matrix (matr2), from the data matrix (matrix) using the rotated data indexes 
#     for i in range(number_of_rings):
#         elements_in_a_ring = 2*n + 2*(m-2)

#         for j in range(n):
#             matr2[i][n-j-1+i] = matrix[m_rings[i][j]][n_rings[i][j]]
#         for j in range(m-1):
#             matr2[j+1+i][i] = matrix[m_rings[i][j+n]][n_rings[i][j+n]]
#         for j in range(n-1):
#             matr2[m-1+i][j+1+i] = matrix[m_rings[i][m+n-1+j]][n_rings[i][m+n-1+j]]
#         for j in range(m-2):
#             m_arr.append(m-j-2+i)
#             n_arr.append(n-1+i)
#             matr2[m-j-2+i][n-1+i] = matrix[m_rings[i][m+(2*n)-2+j]][n_rings[i][m+(2*n)-2+j]]

#         m -= 2
#         n -= 2

#     # print(f"m matrix 1: {matrix}")
#     # print(f"m matrix 2: {matr2}")

#     m = len(matrix)
#     for i in range(m):
#         print(*matr2[i])

# def matrixRotation(matrix, r):
#     n, m = len(matrix), len(matrix[0])
#     def to_depth_pos(i, j):
#         depth = min(i, j, n-i-1, m-j-1)
#         if j == depth:
#             pos = i - depth
#         elif i == n-1-depth:
#             pos = n - 1 + j - 3*depth
#         elif j == m-1-depth:
#             pos = 2*n + m - 3 - i - 5*depth
#         else:
#             pos = 2*n + 2*m - 4 - j - 7*depth
#         return depth, pos

#     def from_depth_pos(depth, pos):
#         pos = pos % (2*(n + m - 2 - 4*depth))
#         if pos < n-1-2*depth:
#             j, i = depth, pos+depth
#         elif pos < n + m - 2 - 4*depth:
#             i, j = n-1-depth, pos - (n - 1 - 3*depth)
#         elif pos < 2*n + m - 3 - 6*depth:
#             j, i = m-1-depth, 2*n + m - 3 - 5*depth - pos
#         else:
#             i, j = depth,     2*n + 2*m - 4 - 7*depth - pos
#         return i, j
    
#     for i in range(n):
#         for j in range(m):
#             depth, pos = to_depth_pos(i, j)
#             new_i, new_j = from_depth_pos(depth, pos-r)
#             print(matrix[new_i][new_j], end=' ')
#         print()

def matrixRotation(matrix, r):
    
    n1, n2 = len(matrix), len(matrix[0])
    for i in range(n1):
        for j in range(n2):
            l = min(min(i, j),min(n1-i-1, n2-j-1)) #current layer
            k = r % (2*(n1+n2-(4*l)-2)) #r % max_rotations
            x, y = i, j
            while k:
                if x == l and y != n2-l-1:#topleft->topright
                    inc = min(k, n2-l-y-1)
                    y += inc
                    k -= inc
                elif y == n2-l-1 and x != n1-l-1:#t_right->b_right
                    inc = min(k, n1-l-x-1)
                    x += inc
                    k -= inc
                elif x == n1-l-1 and y != l:#b_right->b_left
                    inc = min(k, y-l)
                    y -= inc
                    k -= inc
                else:#bottom left->top left
                    inc = min(k, x-l)
                    x -= inc
                    k -= inc

            print(matrix[x][y], end=" ")
        print()


        
if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)