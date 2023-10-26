from bricksGame import bricksGame

class TesteBricksGame:
    
    def testeCaso1(self):
        
        arr = [999, 1, 1, 1, 0]
        
        esperado = 1001
        
        resultado = bricksGame(arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        arr = [0, 1, 1, 1, 999]
        
        esperado = 999
        
        resultado = bricksGame(arr)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        arr = [123, 4, 56, 19, 20]
        
        esperado = 183
        
        resultado = bricksGame(arr)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        arr = [15, 17, 25, 128, 95]
        
        esperado = 110
        
        resultado = bricksGame(arr)
        
        assert resultado == esperado
        
    def testeCaso5(self):
        
        arr = [15, 17, 19, 10, 100]
    
        esperado = 115
        
        resultado = bricksGame(arr)
        
        assert resultado == esperado
        
    def testeCaso6(self):
        
        arr = [397, 385, 160, 890, 541]
    
        esperado = 942
        
        resultado = bricksGame(arr)
        
        assert resultado == esperado