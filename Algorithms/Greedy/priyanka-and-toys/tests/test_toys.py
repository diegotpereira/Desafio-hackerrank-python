from toys import toys

class TesteToys:
    
    def testeCaso1(self):
        
        w = [1, 2, 3, 21, 7, 12, 14, 21]
        
        resultado = toys(w)
        
        assert resultado == 4
        
    def testeCaso2(self):
        
        w = [12, 15, 7, 8, 19, 24]
        
        resultado = toys(w)
        
        assert resultado == 4
        
    def testeCaso3(self):
        
        w = [16, 18, 10, 13, 2, 9, 17, 17, 0, 19]
        
        resultado = toys(w)
        
        assert resultado == 3
        
    def testeCaso4(self):
        
        w = [82, 75, 19, 35, 67, 5, 54, 7, 31, 46]
        
        resultado = toys(w)
        
        assert resultado == 8