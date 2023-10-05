

from nimGame import nimGame

class TesteNimGame:
    
    def testeCaso1(self):
        
        pilha = [1, 1]
        
        resultado = nimGame(pilha)
        
        assert resultado == "Second"
        
    def testeCaso2(self):
        
        pilha = [2, 1, 4]
        
        resultado = nimGame(pilha)
        
        assert resultado == "First"
        
    def testeCaso3(self):
        
        pilha = [3, 5]
        
        resultado = nimGame(pilha)
        
        assert resultado == "First"
        
    def testeCaso4(self):
        
        pilha = [1, 3, 5, 7]
        
        resultado = nimGame(pilha)
        
        assert resultado == "Second"