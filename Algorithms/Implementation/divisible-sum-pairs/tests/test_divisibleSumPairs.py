from divisibleSumPairs import divisibleSumPairs

class TesteDivisibleSumPairs:
    
    def test_caso1(self):
        
        assert divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5
        
        assert divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]) == 3