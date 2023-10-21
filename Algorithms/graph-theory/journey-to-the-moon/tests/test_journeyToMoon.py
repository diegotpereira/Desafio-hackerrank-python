from journeyToMoon import journeyToMoon

class TesteJourneyToMoon:
    
    def testeCaso1(self):
        
        n = 5
        astronauta = [[0, 1], [2, 3], [0, 4]]
        
        esperado = 6
        
        resultado = journeyToMoon(n, astronauta)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        n = 4
        astronauta = [[0, 2]]
        
        esperado = 5
        
        resultado = journeyToMoon(n, astronauta)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        n = 10
        astronauta = [[0, 2],[1, 8], [1, 4], [2, 8], [2, 6], [3, 5], [6, 9]]
        
        esperado = 23
        
        resultado = journeyToMoon(n, astronauta)
        
        assert resultado == esperado
        
        
    def testeCaso4(self):
        
        n = 4
        astronauta = [[1, 2],[2, 3]]
        
        esperado = 3
        
        resultado = journeyToMoon(n, astronauta)
        
        assert resultado == esperado