from viralAdvertising import viralAdvertising

class TesteViralAdvertising:
    
    def test_caso1(self):
        
        assert viralAdvertising(3) == 9
        
    def test_caso2(self):
        
        assert viralAdvertising(4) == 15