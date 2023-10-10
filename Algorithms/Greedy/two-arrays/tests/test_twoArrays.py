from twoArrays import twoArrays

class TesteTwoArrays:
    
    def testeCaso1(self):
        
        k = 6
        A = [2, 1, 3]
        B = [7, 8, 9]
        
        esperado = 'YES'
        
        resultado = twoArrays(k, A, B)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        k = 8
        A = [1, 2, 2, 1]
        B = [3, 3, 3, 4]
        
        esperado = 'NO'
        
        resultado = twoArrays(k, A, B)
        
        assert resultado == esperado
        
        
    def testeCaso3(self):
        
        k = 10
        A = [7, 6, 8, 4, 2]
        B = [5, 2, 6, 3, 1]
        
        esperado = 'NO'
        
        resultado = twoArrays(k, A, B)
        
        assert resultado == esperado
        
        