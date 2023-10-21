
from gridlandMetro import gridlandMetro

class TesteGridlandMetro:
    
    def testeCaso1(self):
        
        n = 4
        m = 4
        k = 3
        pista = [[2, 2, 3], [3, 1, 4], [4, 4, 4]]
        
        esperado = 9
        resultado = gridlandMetro(n, m, k, pista)
        
        assert resultado ==  esperado
        
        
    def testeCaso2(self):
        
        n = 4
        m = 4
        k = 0
        pista = []
        
        esperado = 16
        resultado = gridlandMetro(n, m, k, pista)
        
        assert resultado ==  esperado
        
    def testeCaso3(self):
        
        n = 1
        m = 5
        k = 3
        pista = [[1, 1, 2], [1, 2, 4], [1, 3, 5]]
    
        esperado = 0
        resultado = gridlandMetro(n, m, k, pista)
        
        assert resultado ==  esperado

    def testeCaso4(self):
        
        n = 1
        m = 7
        k = 3
        pista = [[1, 1, 2], [1, 2, 4], [1, 3, 5]]
    
        esperado = 2
        resultado = gridlandMetro(n, m, k, pista)
        
        assert resultado ==  esperado