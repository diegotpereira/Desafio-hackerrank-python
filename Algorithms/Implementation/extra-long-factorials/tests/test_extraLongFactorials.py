from extraLongFactorials import extraLongFactorials 

class TesteExtraLongFactorials:
    
    def testeCaso1(self):
        
        n = 25
        
        resultado = extraLongFactorials(n)
        
        assert resultado == 15511210043330985984000000
        
    def testeCaso2(self):
        
        n = 45
        
        resultado = extraLongFactorials(n)
        
        assert resultado == 119622220865480194561963161495657715064383733760000000000
        
    def testeCaso3(self):
        
        n = 10
        
        resultado = extraLongFactorials(n)
        
        assert resultado == 3628800
   
    def testeCaso4(self):
        
        n = 4
        
        resultado = extraLongFactorials(n)
        
        assert resultado == 24
        
    def testeCaso5(self):
        
        n = 20
        
        resultado = extraLongFactorials(n)
        
        assert resultado == 2432902008176640000