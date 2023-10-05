from pokerNim import pokerNim

class TestePokerNim:
    
    def testeCaso1(self):
        
        k = [2]
        c = [1, 2]
        
        resultado = pokerNim(k, c)
        
        assert resultado == 'First'
        
    def testeCaso2(self):
        
        k = [3]
        c = [2, 1, 3]
        
        resultado = pokerNim(k, c)
        
        assert resultado == 'Second'