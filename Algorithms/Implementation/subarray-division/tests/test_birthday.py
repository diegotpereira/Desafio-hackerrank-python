from birthday import birthday

class TesteBirthday:
    
    def test_caso1(self):
        
        # s = [1, 2, 1, 3, 2]
        # d = 3
        # m = 2
        
        assert birthday([1, 2, 1, 3, 2], 3, 2) == 2
        
        assert birthday([1, 1, 1, 1, 1, 1], 3, 2) == 0
        
        assert birthday([4], 4, 1) == 1