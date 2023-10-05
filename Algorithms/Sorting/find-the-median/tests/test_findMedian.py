from findMedian import findMedian

class TesteFindMedian:
    
    def testeCaso1(self):
        
        arr = [0, 1, 2, 4, 6, 5, 3]
        
        resultado = findMedian(arr)
        
        assert resultado == 3
        
 