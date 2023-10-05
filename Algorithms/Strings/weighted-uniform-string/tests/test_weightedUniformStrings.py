from weightedUniformStrings import weightedUniformStrings

class TesteWeightedUniformStrings:
    
    def testeCaso1(self):
        
        string = "abccddde"
        consultas = [1, 3, 12, 5, 9, 10]
        
        resposta = weightedUniformStrings(string, consultas)
        
        assert resposta == ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
        
    def testeCaso2(self):
        
        string = "aaabbbbcccddd"
        consultas = [9, 7, 8, 12, 5]
        
        resposta = weightedUniformStrings(string, consultas)
        
        assert resposta == ['Yes', 'No', 'Yes', 'Yes', 'No']
        
    def testeCaso3(self):
        
        string = "l"
        consultas = [1, 12]
        
        resposta = weightedUniformStrings(string, consultas)
        
        assert resposta == ['No', 'Yes']