from miniMaxSum import miniMaxSum

class TestMiniMaxSum:
    
    def test_miniMaxSum(self):
        
        assert miniMaxSum([1, 2, 3, 4, 5]) == (10, 14)
        
        assert miniMaxSum([7, 69, 2, 221, 8974]) == (299, 9271)
        