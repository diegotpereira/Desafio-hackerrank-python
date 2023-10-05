from minimumLoss import minimumLoss

class TesteMinimumLoss:
    
    def testeCaso1(self):
        
        preco = [5, 10, 3]
        
        resultado = minimumLoss(preco)
        
        assert resultado == 2
        
        
    def testeCaso2(self):
        
        preco = [20, 7, 8, 2, 5]
        
        resultado = minimumLoss(preco)
        
        assert resultado == 2
        
    def testeCaso3(self):
        
        preco = [2, 3, 4, 1]
        
        resultado = minimumLoss(preco)
        
        assert resultado == 1
        