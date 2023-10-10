from flippingBits import flippingBits

class TesteFlippingBits:
    
    def testeCaso1(self):
        
        n = 2147483647
        esperado = 2147483648
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        n = 1
        esperado = 4294967294
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
    def testeCaso3(self):
        
        n = 0
        esperado = 4294967295
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
    def testeCaso4(self):
        
        n = 4
        esperado = 4294967291
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
    def testeCaso6(self):
        
        n = 0
        esperado = 4294967295
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
    def testeCaso7(self):
        
        n = 802743475
        esperado = 3492223820
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
    def testeCaso8(self):
        
        n = 35601423
        esperado = 4259365872
        
        resultado = flippingBits(n)
        
        assert resultado == esperado
        
        
        
    
    