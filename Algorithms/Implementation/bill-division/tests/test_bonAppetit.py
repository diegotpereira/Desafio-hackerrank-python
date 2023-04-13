from bonAppetit import bonAppetit

class TesteBonAppetit:
    
    def test_caso1(self):
        
        assert bonAppetit([3, 10, 2, 9], 1, 12) == 5
        
    def test_caso2(self):
        
        bill = [3, 10, 2, 9]
        k = 1
        b = 7
        
        assert bonAppetit(bill, k, b) == "Bon Appetit"