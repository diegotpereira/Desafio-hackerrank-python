from maximumPerimeterTriangle import maximumPerimeterTriangle

class TesteMaximumPerimeterTriangle:
    
    def testeCaso1(self):
        
        gravetos = [1, 1, 1, 3, 3]
        
        resultado = maximumPerimeterTriangle(gravetos)
        
        assert resultado == [1, 3, 3]
        
    def testeCaso2(self):
        
        gravetos = [1, 2, 3]
        
        resultado = maximumPerimeterTriangle(gravetos)
        
        assert resultado == [-1]
        
    def testeCaso3(self):
        
        gravetos = [1, 1, 1, 2, 3, 5]
        
        resultado = maximumPerimeterTriangle(gravetos)
        
        assert resultado == [1, 1, 1]
        
    def testeCaso4(self):
        
        gravetos = [3, 9, 2, 15, 3]
        
        resultado = maximumPerimeterTriangle(gravetos)
        
        assert resultado == [2, 3, 3]
        
    def testeCaso5(self):
        
        gravetos = [50, 2430, 134, 6373, 215, 1502, 926, 10312, 351, 74, 572, 3938]
        
        resultado = maximumPerimeterTriangle(gravetos)
        
        assert resultado == [-1]
        
    def testeCaso6(self):
        
        gravetos = [9, 2015, 5294, 58768, 285, 477, 72, 13867, 97, 22445, 48, 36318, 764, 8573, 183, 3270, 81, 1251, 59, 95094]
        
        resultado = maximumPerimeterTriangle(gravetos)
        
        assert resultado == [72, 81, 97]