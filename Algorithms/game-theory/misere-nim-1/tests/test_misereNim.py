from misereNim import misereNim

class TesteMisereNim:
    
    def testeCaso1(self):
        
        s = [1, 1]
        
        resultado = misereNim(s)
        
        assert resultado == 'First'
        
    def testeCaso2(self):
        
        s = [2, 1, 3]
        
        resultado = misereNim(s)
        
        assert resultado == 'Second'
        
    def testeCaso2(self):
        
        s = [9, 8, 4, 4, 4, 7]
        
        resultado = misereNim(s)
        
        assert resultado == 'First'