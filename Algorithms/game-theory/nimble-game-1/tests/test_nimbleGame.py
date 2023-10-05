from nimbleGame import nimbleGame

class TesteNimbleGame:
    
    def testeCaso1(self):
        
        s = [0, 2, 3, 0, 6]
        
        resultado = nimbleGame(s) 
        
        assert resultado == 'First'
        
    def testeCaso2(self):
        
        s = [0, 0, 0, 0]
        
        resultado = nimbleGame(s) 
        
        assert resultado == 'Second'