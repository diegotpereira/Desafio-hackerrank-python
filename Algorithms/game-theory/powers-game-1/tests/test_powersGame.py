from powersGame import powersGame

class TestePowersGame:
    
    def testeCaso1(self):
        
        n = 2
        esperado = 'First'
        
        resultado = powersGame(n)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        n = 8
        esperado = 'Second'
        
        resultado = powersGame(n)
        
        assert resultado == esperado