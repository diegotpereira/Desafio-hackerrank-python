from half import half

class TesteHalf:
    
    def testeCaso1(self):
        
        n = 1
        esperado = 1
        
        resultado = half(n)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        n = 10
        esperado = 7
        
        resultado = half(n)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        n = 6
        esperado = 2
        
        resultado = half(n)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        n = 8
        esperado = 7
        
        resultado = half(n)
        
        assert resultado == esperado
        
        
    def testeCaso5(self):
        
        n = 123456
        esperado = 32768
        
        resultado = half(n)
        
        assert resultado == esperado