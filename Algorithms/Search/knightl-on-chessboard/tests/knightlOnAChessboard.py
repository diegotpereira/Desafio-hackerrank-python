# A tarefa do problema "KnightL on Chessboard" no HackerRank é a seguinte:

# Dado um tabuleiro de xadrez de tamanho n x n, onde n é um número inteiro, 
# o problema consiste em encontrar o menor número de movimentos que um cavalo 
# de xadrez pode fazer para percorrer da posição (0, 0) para a posição (n-1, n-1), 
# seguindo as regras do movimento de um cavalo.

# As regras do movimento de um cavalo no xadrez são as seguintes: O cavalo 
# pode mover-se em forma de "L", avançando 2 casas em uma direção e 1 casa 
# em uma direção perpendicular, ou avançando 1 casa em uma direção e 2 casas 
# em uma direção perpendicular.

# O problema pede para você criar uma função que, dado um tamanho de tabuleiro n, 
# retorne uma matriz de dimensões (n-1) x (n-1), onde o valor na posição (i, j) 
# representa o número mínimo de movimentos que o cavalo precisa fazer para percorrer 
# da posição (0, 0) para a posição (i, j) no tabuleiro.

from collections import defaultdict
from collections import deque

def knightlOnAChessboard(n):
    
    # Função para obter o número mínimo de movimentos do cavalo
    def obter_movimentos_minimos(a: int, b: int) -> int:
        
        # Inicializar uma fila com a posição inicial (0, 0) 
        # e a distância 0
        q = deque([((0, 0), 0)])
        
        # Conjunto para armazenar coordenadas já visitadas
        visitado = {(0, 0)}
        
        # Enquanto a fila não estiver vazia
        while q: 
            
            # Retirar a coordenada e a distância da frente da fila
            coord, dist = q.popleft()
            
            # Separar as coordenadas em i e j
            i, j = coord
            
            # Gerar as próximas coordenadas possíveis
            proxima_coord = [
                (i + a, j + b), (i + b, j + a),
                (i + a, j - b), (i + b, j - a),
                (i - a, j + b), (i - b, j + a),
                (i - a, j - b), (i - b, j - a)
            ]
            
            # Para cada nova coordenada próxima
            for ni, nj in proxima_coord:
                
                # Verificar se a nova coordenada está dentro dos limites do tabuleiro
                if 0 <= ni < n and 0 <= nj < n:
                    
                    # Se a coordenada já foi visitada, 
                    # continuar para a próxima
                    if(ni, nj) in visitado:
                        
                        continue
                    
                    # Se chegarmos à posição de destino
                    if ni == nj == n - 1:
                        
                        # Retornar a distância atual mais 1
                        return dist + 1
                    
                    # Adicionar a nova coordenada à fila com distância atualizada
                    q.append(((ni, nj), dist + 1))
                    
                    # Marcar a nova coordenada como visitada
                    visitado.add((ni, nj))
                    
        # Se não for possível alcançar a posição de destino, retornar -1
        return -1
    
    # Inicializar uma matriz para armazenar os resultados
    res = [[None] * (n - 1) for _ in range(n - 1)]
    
    # Percorrer as linhas da matriz
    for i in range(n - 1):
        
        # Percorrer as colunas da matriz até a diagonal principal
        for j in range(i + 1):
            
            # Preencher a matriz com o número mínimo de movimentos entre as posições (i, j) e (j, i)
            res[i][j] = res[j][i] = obter_movimentos_minimos(i + 1, j + 1)
            
    # Retornar a matriz de resultados
    return res