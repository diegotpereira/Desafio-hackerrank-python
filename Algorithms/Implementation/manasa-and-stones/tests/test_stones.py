from stones import stones

class TesteStones:
    
    def testeCaso1(self):
        
        n = 3
        a = 1
        b = 2
        
        resultado = stones(n, a, b)
        
        assert resultado == [2, 3, 4]
        
    def testeCaso2(self):
        
        n = 4
        a = 10
        b = 100
        
        resultado = stones(n, a, b)
        
        assert resultado == [30, 120, 210, 300]
        
    def testeCaso3(self):
        
        n = 7
        a = 9
        b = 11
        
        resultado = stones(n, a, b)
        
        assert resultado == [54,56, 58, 60, 62, 64, 66]
        
    def testeCaso4(self):
        
        n = 4
        a = 8
        b = 16
        
        resultado = stones(n, a, b)
        
        assert resultado == [24, 32, 40, 48]