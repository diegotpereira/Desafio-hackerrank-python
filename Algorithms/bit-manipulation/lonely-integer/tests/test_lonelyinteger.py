from lonelyinteger import lonelyinteger

class TesteLonelyinteger:
    
    def testeCaso1(self):
        
        a = [1]
        esperado = 1
        
        resultado = lonelyinteger(a)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        a = [1, 1, 2]
        esperado = 2
        
        resultado = lonelyinteger(a)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        a = [0, 0, 1, 2, 1]
        esperado = 2
        
        resultado = lonelyinteger(a)
        
        assert resultado == esperado