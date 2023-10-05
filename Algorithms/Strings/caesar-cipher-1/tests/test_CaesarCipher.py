from caesarCipher import caesarCipher

class TesteCaesarCipher:
    
    def testeCaso1(self):
        
        string = "middle-Outz"
        numeroGiros = 2
        
        resposta = caesarCipher(string, numeroGiros)
        
        assert resposta == "okffng-Qwvb"
        
    def testeCaso2(self):
        
        string = "Always-Look-on-the-Bright-Side-of-Life"
        numeroGiros = 5
        
        resposta = caesarCipher(string, numeroGiros)
        
        assert resposta == "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
        
        
    def testeCaso3(self):
        
        string = "www.abc.xy"
        numeroGiros = 87
        
        resposta = caesarCipher(string, numeroGiros)
        
        assert resposta == "fff.jkl.gh"
        
        
    def testeCaso4(self):
        
        string = "159357lcfd"
        numeroGiros = 98
        
        resposta = caesarCipher(string, numeroGiros)
        
        assert resposta == "159357fwzx"
        
        
    def testeCaso5(self):
        
        string = "D3q4"
        numeroGiros = 0
        
        resposta = caesarCipher(string, numeroGiros)
        
        assert resposta == "D3q4"