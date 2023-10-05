from chocolateFeast import chocolateFeast

class TesteChocolateFeast:
    
    def testeCaso1(self):
        
        n = 10
        c = 2
        m = 5
        
        resultado = chocolateFeast(n, c, m)
    
        assert resultado == 6
        
    def testeCaso2(self):
        
        n = 12
        c = 4
        m = 4
        
        resultado = chocolateFeast(n, c, m)
    
        assert resultado == 3
        
    def testeCaso3(self):
        
        n = 6
        c = 2
        m = 2
        
        resultado = chocolateFeast(n, c, m)
    
        assert resultado == 5
        
    def testeCaso4(self):
        
        n = 7
        c = 3
        m = 2
        
        resultado = chocolateFeast(n, c, m)
    
        assert resultado == 3