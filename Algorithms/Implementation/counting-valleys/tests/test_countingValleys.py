from countingValleys import countingValleys

class TesteCountingValleys:
    
    def test_caso1(self):
        
        assert countingValleys(8, "UDDDUDUU") == 1
        assert countingValleys(12, "DDUUDDUDUUUD") == 2