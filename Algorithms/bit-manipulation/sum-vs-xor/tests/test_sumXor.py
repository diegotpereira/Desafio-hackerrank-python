from sumXor import sumXor

class TesteSumXor:
    
    def testeCaso1(self):
        
        n = 5
        esperado = 2
        
        resultado = sumXor(n)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        n = 10
        esperado = 4
        
        resultado = sumXor(n)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        n = 0
        esperado = 1
        
        resultado = sumXor(n)
        
        assert resultado == esperado
        
        
    def testeCaso4(self):
        
        n = 100
        esperado = 16
        
        resultado = sumXor(n)
        
        assert resultado == esperado