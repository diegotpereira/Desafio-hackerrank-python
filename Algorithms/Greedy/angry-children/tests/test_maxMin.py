from maxMin import maxMin

class TesteMaxMin:
    
    def testeCaso1(self):
        
        k = 3
        arr = [10, 100, 300, 200, 1000, 20, 30]
        
        resultado = maxMin(k, arr)
        
        assert resultado == 20