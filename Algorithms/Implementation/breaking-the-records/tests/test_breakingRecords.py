from breakingRecords import breakingRecords

class TesteBreakingRecords:
    
    def test_breakingRecords(self):
        
        assert breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]) == (2, 4)
        
    def test_breakingRecords1(self):
        
        assert breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == (4, 0)
        
    def test_breakingRecords2(self):
        
        assert breakingRecords([1, 1, 1, 1, 1]) == (0, 0)