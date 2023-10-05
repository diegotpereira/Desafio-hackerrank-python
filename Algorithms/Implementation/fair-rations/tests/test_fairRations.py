from fairRations import fairRations

class TesteFairRations:
    
    def testeCaso1(self):
        
        B = [2, 3, 4, 5, 6]
        
        resultado = fairRations(B)
        
        assert resultado == '4'
        
    def testeCaso2(self):
        
        B = [1, 2]
        
        resultado = fairRations(B)
        
        assert resultado == 'NO'