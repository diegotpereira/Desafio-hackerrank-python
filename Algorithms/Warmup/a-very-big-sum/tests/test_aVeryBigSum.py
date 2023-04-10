from aVeryBigSum import aVeryBigSum
 
class TestAVeryBigSum:
    
    def test_example1(self):
        
        assert aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 5000000015
        
    def test_example2(self):
        
        assert aVeryBigSum([999999999, 999999999, 999999999, 999999999, 999999999]) == 4999999995

    def test_example3(self):
        
        assert aVeryBigSum([1001458909, 1004570889, 1007019111, 1003302837, 1002514638, 1006431461, 1002575010, 1007514041, 1007548981, 1004402249]) == 10047338126