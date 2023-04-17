from saveThePrisoner import saveThePrisoner

class TesteSaveThePrisoner:
    
    def test_caso1(self):
        
        assert saveThePrisoner(5, 2, 1) == 2
        
    def test_caso2(self):
        
        assert saveThePrisoner(5, 2, 2) == 3
        
    def test_caso3(self):
        
        assert saveThePrisoner(7, 19, 2) == 6
        
    def test_caso4(self):
        
        assert saveThePrisoner(3, 7, 3) == 3