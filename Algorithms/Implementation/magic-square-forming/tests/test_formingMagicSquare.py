from formingMagicSquare import formingMagicSquare

class TesteFormingMagicSquare:
    
    def test_caso1(self):
        
        assert formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]) == 1