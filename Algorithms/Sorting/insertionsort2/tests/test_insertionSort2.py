from insertionSort2 import insertionSort2

class TesteInsertionSort2:
    
    def testeCaso1(self):
        
        n = 6
        arr = [1, 4, 3, 5, 6, 2]
        esperado = [
            [1, 4, 3, 5, 6, 2],
            [1, 3, 4, 5, 6, 2],
            [1, 3, 4, 5, 6, 2],
            [1, 3, 4, 5, 6, 2],
            [1, 2, 3, 4, 5, 6]
        ]
        
        resultado = insertionSort2(n, arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        n = 8
        arr = [8, 7, 6, 5, 4, 3, 2, 1]
        esperado = [
            [7, 8, 6, 5, 4, 3, 2, 1],
            [6, 7, 8, 5, 4, 3, 2, 1],
            [5, 6, 7, 8, 4, 3, 2, 1],
            [4, 5, 6, 7, 8, 3, 2, 1],
            [3, 4, 5, 6, 7, 8, 2, 1],
            [2, 3, 4, 5, 6, 7, 8, 1],
            [1, 2, 3, 4, 5, 6, 7, 8]
        ]
        
        resultado = insertionSort2(n, arr)
        
        assert resultado == esperado
        