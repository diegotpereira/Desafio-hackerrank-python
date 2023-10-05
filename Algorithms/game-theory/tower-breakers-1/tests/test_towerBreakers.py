from towerBreakers import towerBreakers

class TesteTowerBreakers:
    
    def testeCaso1(self):
        
        n = 2
        m = 2
        
        resultado = towerBreakers(n, m)
        
        assert resultado == 2
        
    def testeCaso2(self):
        
        n = 1
        m = 4
        
        resultado = towerBreakers(n, m)
        
        assert resultado == 1
        
        
    def testeCaso3(self):
        
        n = 1
        m = 7
        
        resultado = towerBreakers(n, m)
        
        assert resultado == 1
        
    def testeCaso4(self):
        
        n = 3
        m = 7
        
        resultado = towerBreakers(n, m)
        
        assert resultado == 1