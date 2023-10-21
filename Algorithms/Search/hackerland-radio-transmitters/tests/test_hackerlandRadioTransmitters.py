from hackerlandRadioTransmitters import hackerlandRadioTransmitters

class TesteHackerlandRadioTransmitters:
    
    def testeCaso1(self):
        
        k = 1
        x = [1, 2, 3, 4, 5]
        esperado = 2
        
        resultado = hackerlandRadioTransmitters(x, k)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        k = 2
        x = [7, 2, 4, 6, 5, 9, 12, 11]
        esperado = 3
        
        resultado = hackerlandRadioTransmitters(x, k)
        
        assert resultado == esperado
        
        
    def testeCaso3(self):
        
        k = 2
        x = [9, 5, 4, 2, 6, 15, 12]
        esperado = 4
        
        resultado = hackerlandRadioTransmitters(x, k)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        k = 2
        x = [2, 2, 2, 2, 1, 1, 1, 1]
        esperado = 1
        
        resultado = hackerlandRadioTransmitters(x, k)
        
        assert resultado == esperado
        
    def testeCaso5(self):
        
        k = 3
        x = [10, 10, 10]
        esperado = 1
        
        resultado = hackerlandRadioTransmitters(x, k)
        
        assert resultado == esperado
        
        
    def testeCaso6(self):
        
        k = 1
        x = [1]
        esperado = 1
        
        resultado = hackerlandRadioTransmitters(x, k)
        
        assert resultado == esperado
        