from maximizingXor import maximizingXor

class TesteMaximizingXor:
    
    def testeCaso1(self):
        
        l = 10
        r = 15
        
        esperado = 7
        
        resultado = maximizingXor(l, r)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        l = 11
        r = 100
        
        esperado = 127
        
        resultado = maximizingXor(l, r)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        l = 1
        r = 10
        
        esperado = 15
        
        resultado = maximizingXor(l, r)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        l = 5
        r = 6
        
        esperado = 3
        
        resultado = maximizingXor(l, r)
        
        assert resultado == esperado
        
    def testeCaso5(self):
        
        l = 1
        r = 1000
        
        esperado = 1023
        
        resultado = maximizingXor(l, r)
        
        assert resultado == esperado
        
        
    def testeCaso6(self):
        
        l = 304
        r = 313
        
        esperado = 15
        
        resultado = maximizingXor(l, r)
        
        assert resultado == esperado