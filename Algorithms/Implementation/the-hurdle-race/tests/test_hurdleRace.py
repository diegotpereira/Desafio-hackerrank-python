from hurdleRace import hurdleRace

class TesteHurdleRace:
    
    def test_caso1(self):
        
        k = 5
        height = [1, 2, 3]
        
        assert hurdleRace(k, height) == 0
        
        
        
        assert hurdleRace(7, [2, 5, 4, 5, 2]) == 0
        
    def test_caso2(self):
        
        k = 4
        height = [1, 6, 3, 5, 2]
        
        
        assert hurdleRace(k, height) == 2
        
        
    def test_caso3(self):
        
        k = 7
        height = [2, 5, 4, 5, 2]
        
        
        assert hurdleRace(k, height) == 0
        