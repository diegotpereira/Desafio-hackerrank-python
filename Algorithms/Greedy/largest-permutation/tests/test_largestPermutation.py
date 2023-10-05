from largestPermutation import largestPermutation

class TesteLargestPermutation:
    
    def testeCaso1(self):
        
        k = 1
        arr = [4, 2, 3, 5, 1]
        
        resultado = largestPermutation(k, arr)
        
        assert resultado == [5, 2, 3, 4, 1]
        
    def testeCaso2(self):
        
        k = 1
        arr = [2, 3, 1]
        
        resultado = largestPermutation(k, arr)
        
        assert resultado == [3, 2, 1]
        
    def testeCaso3(self):
        
        k = 1
        arr = [2, 1]
        
        resultado = largestPermutation(k, arr)
        
        assert resultado == [2, 1]