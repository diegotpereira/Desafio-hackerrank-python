from catAndMouse import catAndMouse

class TesteCatAndMouse:
    
    def test_caso1(self):
        
        assert catAndMouse(1, 2, 3) == "Cat B"
        
    def test_caso2(self):
        
        assert catAndMouse(1, 3, 2) == "Mouse C"
        
    def test_caso3(self):
        
        assert catAndMouse(2, 1, 3) == "Cat A"