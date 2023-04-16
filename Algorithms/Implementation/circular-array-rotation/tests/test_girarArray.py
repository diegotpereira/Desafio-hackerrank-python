from girarArray import girarArray

class TesteGirarArray:
    
    def test_caso1(self):
        
        assert girarArray([1, 2 ,3], 2) == [2, 3, 1]
        
        assert girarArray([5, 6, 7], 2) == [6, 7, 5]
        
        assert girarArray([8, 9, 10], 2) == [9, 10, 8]
        
        assert girarArray([11, 12, 13], 2) == [12, 13,11]
        
    def test_caso2(self):
        
        assert girarArray([1, 2, 3], 3) == [1, 2, 3]
        assert girarArray([4, 5, 6], 3) == [4, 5, 6]
        assert girarArray([7, 8, 9], 3) == [7, 8, 9]
        
    def test_caseo3(self):
        
        assert girarArray([1, 2, 3], 4) == [3, 1, 2]
        assert girarArray([4, 5, 6], 4) == [6, 4, 5]
        assert girarArray([7, 8, 9], 4) == [9, 7, 8]
        
    def test_girarArray(self):
        
        assert girarArray([1, 2, 3], 5) == [2, 3 ,1]
        assert girarArray([4, 5, 6], 5) == [5, 6, 4]
        assert girarArray([7, 8, 9], 5) == [8, 9, 7]