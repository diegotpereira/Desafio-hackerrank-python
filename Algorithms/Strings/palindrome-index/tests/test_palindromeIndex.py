from palindromeIndex import palindromeIndex

class TestePalindromeIndex:
    
    def testeCaso1(self):
        
        palavra = "aaab"
        
        resultado = palindromeIndex(palavra)
        
        assert resultado == 3
        
    def testeCaso2(self):
        
        palavra = "baa"
        
        resultado = palindromeIndex(palavra)
        
        assert resultado == 0
        
    def testeCaso3(self):
        
        palavra = "aaa"
        
        resultado = palindromeIndex(palavra)
        
        assert resultado == -1
        
    