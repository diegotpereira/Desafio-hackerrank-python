from stringConstruction import stringConstruction

class TestStringConstruction:
    
    def test_empty_string(self):
        
        assert stringConstruction("") == 0
        
    def test_unico_caracter_string(self):
        
        assert stringConstruction("a") == 1
        
    def test_duplicado_caracter_string(Self):
        
        assert stringConstruction("aaabbbccc") == 3
        
    def test_all_unique_characters(self):
        assert stringConstruction("abcdefghijklmnopqrstuvwxyz") == 26