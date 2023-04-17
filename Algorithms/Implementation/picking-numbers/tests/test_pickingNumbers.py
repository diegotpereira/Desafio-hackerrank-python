from pickingNumbers import pickingNumbers

class TestePickingNumbers:
    
    def test_caso1(self):
        
        assert pickingNumbers([4, 6, 5, 3, 3, 1]) == 3
        
    def test_caso2(self):
        
        assert pickingNumbers([1, 2, 2, 3, 1, 2]) == 5