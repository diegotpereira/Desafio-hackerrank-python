from dayOfProgrammer import dayOfProgrammer

class TesteDayOfProgrammer:
    
    def test_caso1(self):
        
        assert dayOfProgrammer(2017) == "13.09.2017"
        
    def test_caso2(self):
        
        ano = 2016
        
        assert dayOfProgrammer(ano) == "12.09.2016"
        
    def test_caso3(self):
        
        ano = 2015
        
        assert dayOfProgrammer(ano) == "13.09.2015"
        
    def test_caso4(self):
        
        assert dayOfProgrammer(2014) == "13.09.2014"
        
    def test_caso5(self):
        
        assert dayOfProgrammer(2012) == "12.09.2012"