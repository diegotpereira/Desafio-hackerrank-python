from cavityMap import cavityMap

class TesteCavityMap:
    
    def testeCaso1(self):
        
        grade = ['1112', '1912', '1892', '1234']
        
        resultado = cavityMap(grade)
        
        assert resultado == ['1112', '1X12', '18X2', '1234']
        
    def testeCaso2(self):
        
        grade = ['12', '12']
        
        resultado = cavityMap(grade)
        
        assert resultado == ['12', '12']
        
    def testeCaso3(self):
        
        grade = ['9']
        
        resultado = cavityMap(grade)
        
        assert resultado == ['9']
        
    def testeCaso4(self):
        
        grade = ['11', '11']
        
        resultado = cavityMap(grade)
        
        assert resultado == ['11', '11']
        
    def testeCaso5(self):
        
        grade = ['12', '11']
        
        resultado = cavityMap(grade)
        
        assert resultado == ['12', '11']
        
    def testeCaso5(self):
        
        grade = ['111', '121', '111']
        
        resultado = cavityMap(grade)
        
        assert resultado == ['111', '1X1', '111']