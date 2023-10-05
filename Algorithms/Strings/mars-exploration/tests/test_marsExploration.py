from marsExploration import marsExploration

class TestemMrsExploration:
    
    def testeCaso1(self):
        
        string = "SOSSPSSQSSOR"
        
        resposta = marsExploration(string)
        
        assert resposta == 3
        
    def testeCaso2(self):
        
        string = "SOSSOT"
        
        resposta = marsExploration(string)
        
        assert resposta == 1
        
    def testeCaso3(self):
        
        string = "SOSSOSSOS"
        
        resposta = marsExploration(string)
        
        assert resposta == 0
        
    def testeCaso4(self):
        
        string = "SOSSOSSOSSOSSOSSOSSOSSOSSOSSOSSOSSOSSOSSOSSOSSOS"
        
        resposta = marsExploration(string)
        
        assert resposta == 0
        
    def testeCaso5(self):
        
        string = "SOSOOSOSOSOSOSSOSOSOSOSOSOS"
        
        resposta = marsExploration(string)
        
        assert resposta == 12
        
        
    def testeCaso6(self):
        
        string = "SOS"
        
        resposta = marsExploration(string)
        
        assert resposta == 0