from gameOfStones import gameOfStones

class TesteGameOfStones:
    
    def testeCaso1(self):
        
        n = 1
        
        resultado = gameOfStones(n)
        
        assert resultado == "Second"
        
        
    def testeCaso2(self):
        
        n = 2
        
        resultado = gameOfStones(n)
        
        assert resultado == "First"
        
    def testeCaso3(self):
        
        n = 7
        
        resultado = gameOfStones(n)
        
        assert resultado == "Second"
        
    def testeCaso4(self):
        
        n = 10
        
        resultado = gameOfStones(n)
        
        assert resultado == "First"