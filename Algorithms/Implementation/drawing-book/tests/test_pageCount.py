from pageCount import pageCount

class TestePageCount:
    
    def test_caso1(self):
        
        assert pageCount(12, 2) == 1
        assert pageCount(5, 4) == 0    