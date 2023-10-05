from permutationEquation import permutationEquation

class TestePermutationEquation:
    
    def testeCaso1(self):
        
        p = [2, 3, 1]
        
        resultado = permutationEquation(p)
        
        assert resultado == [2, 3, 1]
        
    def testeCaso2(self):
        
        p = [4, 3, 5, 1, 2]
        
        resultado = permutationEquation(p)
        
        assert resultado == [1, 3, 5, 4, 2]
        
    def testeCaso3(self):
        
        p = [1, 4, 2, 3, 5]
        
        resultado = permutationEquation(p)
        
        assert resultado == [1, 4, 2, 3, 5]