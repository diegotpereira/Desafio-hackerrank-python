

from flatlandSpaceStations import flatlandSpaceStations

class TesteFlatlandSpaceStations:
    
    def testeCaso(self):
        
        n = 5
        c =[0, 4]
        
        resultado = flatlandSpaceStations(n, c)
        
        assert resultado == 2
        
        
    def testeCaso2(self):
        
        n = 6
        c =[0, 1, 2, 4, 3, 5]
        
        resultado = flatlandSpaceStations(n, c)
        
        assert resultado == 0
        
    def testeCaso3(self):
        
        n = 20
        c =[13, 1, 11, 10, 6]
        
        resultado = flatlandSpaceStations(n, c)
        
        assert resultado == 6
        
    def testeCaso4(self):
        
        n = 100
        c =[93, 41, 91, 61, 30, 6, 25, 90, 97]
        
        resultado = flatlandSpaceStations(n, c)
        
        assert resultado == 14