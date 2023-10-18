from substringDiff import substringDiff

class TesteSubstringDiff:
    
    def testeCaso1(self):
        
        k = 2 
        s1 = 'tabriz'
        s2 = 'torino'
        
        esperado = 4
        
        resultado = substringDiff(k, s1, s2)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        k = 0
        s1 = 'abacba'
        s2 = 'abcaba'
        
        esperado = 3
        
        resultado = substringDiff(k, s1, s2)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        k = 3
        s1 = 'helloworld'
        s2 = 'yellomarin'
        
        esperado = 8
        
        resultado = substringDiff(k, s1, s2)
        
        assert resultado == esperado