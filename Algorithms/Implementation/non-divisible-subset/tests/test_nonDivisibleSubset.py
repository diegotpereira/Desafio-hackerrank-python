from nonDivisibleSubset import nonDivisibleSubset

class TestenonDivisibleSubset:
    
    def testeCaso1(self):
        
        divisor = 3
        matrix = [1, 7, 2, 4]
        
        resultado = nonDivisibleSubset(divisor, matrix)
        
        assert resultado == 3
        
    def testeCaso2(self):
        
        divisor = 7
        matrix = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
        
        resultado = nonDivisibleSubset(divisor, matrix)
        
        assert resultado == 11
        
    def testeCaso3(self):
        
        divisor = 5
        matrix = [2, 7, 12, 17, 22]
        
        resultado = nonDivisibleSubset(divisor, matrix)
        
        assert resultado == 5
        
    def testeCaso4(self):
        
        divisor = 9
        matrix = [422346306, 940894801, 696810740, 862741861, 85835055, 313720373]
        
        resultado = nonDivisibleSubset(divisor, matrix)
        
        assert resultado == 5