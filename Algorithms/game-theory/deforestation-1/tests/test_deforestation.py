from deforestation import deforestation

class TesteDeforestation:
    
    def testeCaso1(self):
        
        n = 5
        arvore = [[1, 2], [3, 1], [3, 4], [5, 4]]
        
        esperado = 'Alice'
        resultado = deforestation(n, arvore)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        n = 3
        arvore = [[1, 2], [1, 3]]
        
        esperado = 'Bob'
        resultado = deforestation(n, arvore)
        
        assert resultado == esperado