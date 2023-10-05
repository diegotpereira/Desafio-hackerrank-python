from sillyGame import sillyGame

class TesteSillyGame:
    
    def testeCaso1(self):
        
        n = 1
        
        resultado = sillyGame(n)
        
        assert resultado == 'Bob'
        
    def testeCaso2(self):
        
        n = 2
        
        resultado = sillyGame(n)
        
        assert resultado == 'Alice'
        
    def testeCaso3(self):
        
        n = 5
        
        resultado = sillyGame(n)
        
        assert resultado == 'Alice'
        
    def testeCaso3(self):
        
        n = 92410
        
        resultado = sillyGame(n)
        
        assert resultado == 'Alice'