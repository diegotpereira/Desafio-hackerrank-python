from kaprekarNumbers import kaprekarNumbers

class TesteKaprekarNumbers:
    
    def testeCaso1(self):
        
        p = 1
        q = 100
        
        resultado = kaprekarNumbers(p, q)
        
        assert resultado == '1 9 45 55 99'
        
    def testeCaso2(self):
        
        p = 100
        q = 300
        
        resultado = kaprekarNumbers(p, q)
        
        assert resultado == '297'
        
    def testeCaso3(self):
        
        p = 400
        q = 700
        
        resultado = kaprekarNumbers(p, q)
        
        assert resultado == 'INVALID RANGE'
        
        
    def testeCaso4(self):
        
        p = 900
        q = 1000
        
        resultado = kaprekarNumbers(p, q)
        
        assert resultado == '999'