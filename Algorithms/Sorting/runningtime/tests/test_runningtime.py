from runningtime import runningtime

class TesteRunningtime:
    
    def testeCaso1(self):
        
        arr = [2, 1, 3, 1, 2]
        esperado = 4
        
        resultado = runningtime(arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        arr = [1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]
        esperado = 0
        
        resultado = runningtime(arr)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        esperado = 45
        
        resultado = runningtime(arr)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        arr = [4, 4, 3, 4]
        esperado = 2
        
        resultado = runningtime(arr)
        
        assert resultado == esperado