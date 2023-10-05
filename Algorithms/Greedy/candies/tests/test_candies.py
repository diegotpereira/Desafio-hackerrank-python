from candies import candies

class TesteCandies:
    
    def testeCaso1(self):
        
        n = 3
        arr = [1, 2, 2]
        
        resultado = candies(n, arr)
        
        assert resultado == 4
        
    def testeCaso2(self):
        
        n = 10
        arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        
        resultado = candies(n, arr)
        
        assert resultado == 19
        
        
    def testeCaso3(self):
        
        n = 8
        arr = [2, 4, 3, 5, 2, 6, 4, 5]
        
        resultado = candies(n, arr)
        
        assert resultado == 12