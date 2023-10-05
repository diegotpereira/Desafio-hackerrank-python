from balancedSums import balancedSums

class TesteBalancedSums:
    
    def testCaso1(self):
        
        arr = [1, 2, 3]
        
        resposta = balancedSums(arr)
        
        assert resposta == "NO"
        
    def testCaso2(self):
        
        arr = [1, 2, 3, 3]
        
        resposta = balancedSums(arr)
        
        assert resposta == "YES"
        
    def testCaso3(self):
        
        arr = [1, 1, 4, 1, 1]
        
        resposta = balancedSums(arr)
        
        assert resposta == "YES"
        
    def testCaso4(self):
        
        arr = [2, 0, 0, 0]
        
        resposta = balancedSums(arr)
        
        assert resposta == "YES"
        
    
    def testCaso5(self):
        
        arr = [0, 0, 2, 0]
        
        resposta = balancedSums(arr)
        
        assert resposta == "YES"
    