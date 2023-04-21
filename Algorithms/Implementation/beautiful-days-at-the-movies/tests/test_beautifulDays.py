from beautifulDays import beautifulDays

class TesteBeautifulDays:
    
    def test_caso1(self):
        
        assert beautifulDays(20, 23, 6) == 2
        
    def test_caso2(self):
        
        assert beautifulDays(13, 45, 3) == 33