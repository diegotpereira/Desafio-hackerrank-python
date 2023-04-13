from sockMerchant import sockMerchant

class TesteSockMerchant:
    
    def testCaso1(self):
        
        assert sockMerchant(10, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
        
        assert sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]) == 4