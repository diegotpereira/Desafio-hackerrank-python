from pairs import pairs

class TestePairs:
    
    def testeCaso1(self):
        
        diferenca = 2
        arr = [1, 5, 3, 4, 2]
        
        esperado = 3
        
        resultado = pairs(diferenca, arr)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        diferenca = 1
        arr = [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793]
        
        esperado = 0
        
        resultado = pairs(diferenca, arr)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        diferenca = 2
        arr = [1, 3, 5, 8, 6, 4, 2]
        
        esperado = 5
        
        resultado = pairs(diferenca, arr)
        
        assert resultado == esperado