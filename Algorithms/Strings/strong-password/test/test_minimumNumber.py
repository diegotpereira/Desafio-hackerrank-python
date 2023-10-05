from minimumNumber import minimumNumber

class TesteMinimumNumber:
    
    def test_caso1(self):
        
        n = 3
        senha = "Ab1"
        
        resultado = minimumNumber(n, senha)
        
        assert resultado == 3
        
        
    def test_caso2(self):
        
        n = 11
        senha = "#HackerRank"
        
        resultado = minimumNumber(n, senha)
        
        assert resultado == 1
        
        
    def test_caso3(self):
        
        n = 1
        senha = "z"
        
        resultado = minimumNumber(n, senha)
        
        assert resultado == 5
        
    def test_caso4(self):
        
        n = 1
        senha = "9"
        
        resultado = minimumNumber(n, senha)
        
        assert resultado == 5
        
         