from appendAndDelete import appendAndDelete

class TesteAppendAndDelete:
    
    def test_caso1(self):
        
        assert appendAndDelete("hackerhappy", "hackerrank", 9) == "YES"
        
    def test_caso2(self):
        
        assert appendAndDelete("aba", "aba", 7) == "YES"  
        
        
    def test_caso3(self):
        
        assert appendAndDelete("ashley", "ash", 2) == "NO"
        