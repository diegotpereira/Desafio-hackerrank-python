from introTutorial import introTutorial

class TesteIntroTutorial:
    
    def testeCaso1(self):
        
        V = 4
        arr = [1, 4, 5, 7, 9, 12]
        esperado = 1
        
        resultado = introTutorial(V, arr)
        assert resultado == esperado
        
    def testeCaso2(self):
        
        V = 23
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
        esperado = 11
        
        resultado = introTutorial(V, arr)
        assert resultado == esperado
        
    def testeCaso3(self):
        
        V = 10
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        esperado = 9
        
        resultado = introTutorial(V, arr)
        assert resultado == esperado