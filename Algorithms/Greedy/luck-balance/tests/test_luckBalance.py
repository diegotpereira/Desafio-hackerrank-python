from luckBalance import luckBalance

class TesteLuckBalance:
    
    def testeCaso1(self):
        
        k = 3
        arr = [
            [5, 1],
            [2, 1],
            [1, 1],
            [8, 1],
            [10, 0],
            [5, 0]
        ] 
        
        esperado = 29
        
        resultado = luckBalance(k, arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        k = 5
        arr = [
            [13, 1],
            [10, 1],
            [9, 1],
            [8, 1],
            [13, 1],
            [12, 1],
            [18, 1],
            [13, 1]
        ] 
        
        esperado = 42
        
        resultado = luckBalance(k, arr)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        k = 2
        arr = [
            [5, 1],
            [4, 0],
            [6, 1],
            [2, 1],
            [8, 0]
        ] 
        
        esperado = 21
        
        resultado = luckBalance(k, arr)
        
        assert resultado == esperado
        
        