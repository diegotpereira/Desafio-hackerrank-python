from utopianTree import utopianTree

class TesteUtopianTree:
    
    
    def test_case1(self):
        assert utopianTree(0) == 1
        assert utopianTree(1) == 2
    
    def test_case2(self):
        assert utopianTree(3) == 6
        assert utopianTree(4) == 7
