from matrixRotation import matrixRotation

class TestMatrixRotation:
        
    def test_matrix_rotation_2(self):
        
        r = 1
        # assert matrixRotation([[4, 1, 4], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] == [[2, 3, 4, 8], [1, 7, 11, 12], [5, 6, 10, 16], [9, 13, 14, 15]], r)
        # assert matrixRotation([[4, 1, 4], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], r) == [[2, 3, 4, 8], [1, 7, 11, 12], [5, 6, 10, 16], [9, 13, 14, 15]]
        # assert matrixRotation([[4, 1, 4], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], r) == [[2, 3, 4, 8], [1, 7, 11, 12], [5, 6, 10, 16], [9, 13, 14, 15]]
        # assert matrixRotation([[4, 1, 4], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], r) == [[2, 3, 4, 8], [1, 7, 11, 12], [5, 6, 10, 16], [9, 13, 14, 15]]



        matriz = [
            [4, 4, 1],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        
        r = 1
        
        matriz_esperada = [
            
            [2, 3, 4, 8],
            [1, 7, 11, 12],
            [5, 6, 10, 16],
            [9, 13, 14, 15]
        ]
        
        assert matrixRotation(matriz, r) == matriz_esperada
    
#     # Defina um método de teste
#     def test_matrix_rotation_1(self):
#         matriz = [[1]]
#         r = 0
#         matriz_esperada = 1
#         assert matrixRotation(matriz, r) == matriz_esperada
    
#     #  # Defina outro método de teste
#     # def test_matrix_rotation_2(self):
#     #     matriz = [
#     #         [4, 4, 1],
#     #         [1, 2, 3, 4],
#     #         [5, 6, 7, 8],
#     #         [9, 10, 11, 12],
#     #         [13, 14, 15, 16]
#     #     ]
#     #     r = 1
#     #     matriz_esperada = [
#     #         [2, 3, 4, 8],
#     #         [1, 7, 11, 12],
#     #         [5, 6, 10, 16],
#     #         [9, 13, 14, 15]
#     #     ]
#     #     assert matrixRotation(matriz, r) == matriz_esperada