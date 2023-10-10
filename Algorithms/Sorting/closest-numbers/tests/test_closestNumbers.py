from closestNumbers import closestNumbers

class TesteClosestNumbers:
    
    def testeCaso1(self):
        
        arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
        
        esperado = [-20, 30]
        
        resultado = closestNumbers(arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        arr = [-5, 15, 25, 71, 63]
        
        esperado = [63, 71]
        
        resultado = closestNumbers(arr)
        
        assert resultado == esperado