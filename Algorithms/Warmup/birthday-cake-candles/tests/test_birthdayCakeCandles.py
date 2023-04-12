from birthdayCakeCandles import birthdayCakeCandles

class TesteBirthdayCakeCandles:
    
    def test_birthdayCakeCandles(self):
        
        assert birthdayCakeCandles([3, 2, 1, 3]) == 2
        
        assert birthdayCakeCandles([3, 3, 2, 1, 3]) == 3
        
        assert birthdayCakeCandles([1, 2, 3, 4, 5]) == 1