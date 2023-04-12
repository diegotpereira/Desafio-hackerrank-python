from migratoryBirds import migratoryBirds

class TesteMigratoryBirds:
    
    def test_caso1(self):
        
        assert migratoryBirds([1, 4, 4, 4, 5, 3]) == 4
        
        assert migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) == 3
        
        assert migratoryBirds([2, 4, 3, 2, 3, 1, 2, 1, 3, 3]) == 3