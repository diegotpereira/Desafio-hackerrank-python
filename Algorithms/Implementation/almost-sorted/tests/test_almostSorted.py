from almostSorted import almostSorted

class TesteAlmostSorted:
    
    def testeCaso1(self):
        
        arr = [4, 2]
        esperado = 'yes'
        
        resultado = almostSorted(arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        arr = [3, 1, 2]
        esperado = 'no'
        
        resultado = almostSorted(arr)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        arr = [1, 5, 4, 3, 2, 6]
        esperado = 'yes'
        
        resultado = almostSorted(arr)
        
        assert resultado == esperado