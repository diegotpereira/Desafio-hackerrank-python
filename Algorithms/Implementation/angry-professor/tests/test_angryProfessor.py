from angryProfessor import angryProfessor

class TesteAngryProfessor:
    
    def test_caso1(self):
        
        assert angryProfessor(3, [-1, -3, 4, 2]) == "YES"
        
    def test_caso2(self):
        
        assert angryProfessor(2, [0, -1, 2, 1]) == "NO"