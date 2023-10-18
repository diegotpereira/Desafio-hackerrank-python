from commonChild import commonChild

class TesteCommonChild:
    
    def testeCaso1(self):
        
        s1 = 'HARRY'
        s2 = 'SALLY'
        
        esperado = 2
        
        resultado = commonChild(s1, s2)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        s1 = 'AA'
        s2 = 'BB'
        
        esperado = 0
        
        resultado = commonChild(s1, s2)
        
        assert resultado == esperado
        
        
    def testeCaso3(self):
        
        s1 = 'SHINCHAN'
        s2 = 'NOHARAAA'
        
        esperado = 3
        
        resultado = commonChild(s1, s2)
        
        assert resultado == esperado