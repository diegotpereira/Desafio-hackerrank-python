from kangaroo import kangaroo

class TesteKangaroo:
    
    def test_kangaroo(self):
        
        assert kangaroo(0, 3, 4, 2) == "YES"
        assert kangaroo(0, 2, 5, 3) == "NO"