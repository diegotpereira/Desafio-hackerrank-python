

from icecreamParlor import icecreamParlor

class TesteIcecreamParlor:
    
    def testeCaso1(self):
        
        saldo = 4
        arr = [1, 4, 5, 3, 2]
        
        resultado = icecreamParlor(saldo, arr)
        
        assert resultado == [1, 4]
        
    def testeCaso2(self):
        
        saldo = 4
        arr = [2, 2, 4, 3]
        
        resultado = icecreamParlor(saldo, arr)
        
        assert resultado == [1, 2]
        
    def testeCaso3(self):
        
        saldo = 9
        arr = [1, 3, 4, 6, 7, 9]
        
        resultado = icecreamParlor(saldo, arr)
        
        assert resultado == [2, 4]
        
    def testeCaso4(self):
        
        saldo = 8
        arr = [1, 3, 4, 4, 6, 8]
        
        resultado = icecreamParlor(saldo, arr)
        
        assert resultado == [3, 4]
        
        
    def testeCaso5(self):
        
        saldo = 3
        arr = [1, 2]
        
        resultado = icecreamParlor(saldo, arr)
        
        assert resultado == [1, 2]