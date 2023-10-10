from insertion_sort import insertion_sort

class TesteInsertion_sort:
    
    def testeCaso1(self):
        
        arr = [4, 1, 3, 5, 6, 2]
        
        resultado = insertion_sort(arr)
        
        esperado = [1, 2, 3, 4, 5, 6]
        assert resultado == esperado
        
    def testeCaso2(self):
        
        arr = [9, 8, 6, 7, 3, 5, 4, 1, 2]
        
        resultado = insertion_sort(arr)
        
        esperado = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert resultado == esperado