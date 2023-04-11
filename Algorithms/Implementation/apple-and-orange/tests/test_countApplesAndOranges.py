from countApplesAndOranges import countApplesAndOranges

class TestCountApplesAndOranges:
    
    def test_countApplesAndOranges1(self):
        
        s = 7
        t = 11
        a = 5
        b = 15
        apples = [-2, 2, 1]
        oranges = [5, -6]
        
        countApplesAndOranges(s, t, a, b, apples, oranges) == [1, 1]
        
        
    def test_countApplesAndOranges2(self):
        
        s = 7
        t = 11
        a = 5
        b = 15
        apples = [-2, 2, 1]
        oranges = [5, -6]
        
        countApplesAndOranges(s, t, a, b, apples, oranges) == [1, 1]
        # assert len(apples) == 1
        # assert len(oranges) == 1

        