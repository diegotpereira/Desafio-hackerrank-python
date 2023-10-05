from missingNumbers import missingNumbers

class TesteMissingNumbers:
    
    def testeCaaso1(self):
        
        arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
        brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
        
        resultado = missingNumbers(arr, brr)
        
        assert resultado == [204, 205, 206]
        
        
    def testeCaaso2(self):
        
        arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
        brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]
        
        resultado = missingNumbers(arr, brr)
        
        assert resultado == [3, 7, 8, 10, 12]
        
        