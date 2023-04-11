from getTotalX import getTotalX

class TesteGetTotalX:
    
    def test_getTotalX1(self):
        
        a = [2, 4]
        b = [16, 32, 96]
        
        experado = 3
        
        assert getTotalX(a, b) == experado
        
    def test_getTotalX2(self):
        
        a = [3, 4, 6]
        b = [24, 48]
        
        experado = 2
        
        assert getTotalX(a, b) == experado
        
        
    def test_getTotalX3(self):
        
        a = [3, 4]
        b = [24, 48]
        
        experado = 2
        
        assert getTotalX(a, b) == experado