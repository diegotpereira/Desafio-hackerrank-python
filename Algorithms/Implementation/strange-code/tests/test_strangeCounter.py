from strangeCounter import strangeCounter

class TesteStrangeCounter:
    
    def testeCaso1(self):
        
        entrada = 4
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 6
        
    def testeCaso2(self):
        
        entrada = 17
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 5
        
    def testeCaso3(self):
        
        entrada = 1
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 3
        
    def testeCaso4(self):
        
        entrada = 1
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 3
        
        
    def testeCaso5(self):
        
        entrada = 1000
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 534
        
    def testeCaso6(self):
        
        entrada = 32434
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 16716
        
    def testeCaso7(self):
        
        entrada = 1000000000000
        
        resultado = strangeCounter(entrada)
        
        assert resultado == 649267441662