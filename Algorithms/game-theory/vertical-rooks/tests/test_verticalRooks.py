from verticalRooks import verticalRooks

class TesteVerticalRooks:
    
    def testeCaso1(self):
        
        r1 = [1, 2, 2]
        r2 = [3, 1, 1]
        
        esperado = "player-2"
        
        resultado = verticalRooks(r1, r2)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        r1 = [3, 3, 3, 3]
        r2 = [4, 4, 4, 4]
        
        esperado = "player-1"
        
        resultado = verticalRooks(r1, r2)
        
        assert resultado == esperado