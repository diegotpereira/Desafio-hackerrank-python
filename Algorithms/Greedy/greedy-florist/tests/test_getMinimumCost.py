from getMinimumCost import getMinimumCost

class TesteGetMinimumCost:
    
    def testeCaso1(self):
        
        numero_amigos = 3
        preco_original = [2, 5, 6]
        
        resultado = getMinimumCost(numero_amigos, preco_original)
        
        assert  resultado == 13
        
    def testeCaso2(self):
        
        numero_amigos = 2
        preco_original = [2, 5, 6]
        
        resultado = getMinimumCost(numero_amigos, preco_original)
        
        assert  resultado == 15
        
    def testeCaso3(self):
        
        numero_amigos = 3
        preco_original = [1, 3, 5, 7, 9]
        
        resultado = getMinimumCost(numero_amigos, preco_original)
        
        assert  resultado == 29