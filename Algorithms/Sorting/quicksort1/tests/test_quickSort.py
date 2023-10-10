from quickSort import quickSort

class TesteQuickSort:
    
    def testeCaso1(self):
        
        arr = [4, 5, 3, 7, 2]
        
        esperado = [3, 2, 4, 5, 7]
        
        resultado = quickSort(arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        arr = [0, -3, 6, 4, -10, 8, -5, 2, -7]
        
        esperado = [-3, -10, -5, -7, 0, 6, 4, 8, 2]
        
        resultado = quickSort(arr)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        arr = [2, 10, 3, 7, 9, 4, 6, 12, 8]
        
        esperado = [2, 10, 3, 7, 9, 4, 6, 12, 8]
        
        resultado = quickSort(arr)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        arr = [45, 25, 46, 48, 28, 6, 13, 5, 36, 44, 7, 4, 11, 30, 24, 34, 15, 31, 38, 49]
        
        esperado = [25, 28, 6, 13, 5, 36, 44, 7, 4, 11, 30, 24, 34, 15, 31, 38, 45, 46, 48, 49]
        
        resultado = quickSort(arr)
        
        assert resultado == esperado