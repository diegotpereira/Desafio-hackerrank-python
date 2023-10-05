from workbook import workbook

class TesteWorkbook:
    
    def testeCaso1(self):
        
        n = 5
        k = 3
        arr = [4, 2, 6, 1, 10]
        
        resultado = workbook(n, k, arr)
        
        assert resultado == 4