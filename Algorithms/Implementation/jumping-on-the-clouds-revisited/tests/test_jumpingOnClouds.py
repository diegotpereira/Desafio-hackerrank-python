from jumpingOnClouds import jumpingOnClouds

class TesteJumpingOnClouds:
    
    def test_caso1(self):
        
        assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2) == 92
        
    def test_caso2(self):
        
        assert jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3) == 80