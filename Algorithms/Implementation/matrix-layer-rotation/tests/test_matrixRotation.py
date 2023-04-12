from matrixRotation import matrixRotation

class TestMatrixRotation:
    
    def test_matrix_rotation(self):
        
        matriz = [
            
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        
        r = 1
        
        matriz_esperada = [[2, 3, 4, 8],[1, 7, 11, 12],[5, 6, 10, 16],[9, 13, 14, 15]]
        
        assert matrixRotation(matriz, r) == matriz_esperada