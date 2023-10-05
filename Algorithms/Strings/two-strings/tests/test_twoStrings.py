from twoStrings import twoStrings

class TesteTwoStrings:
    
    def testeCaso1(self):
        
        string1 = "hello"
        string2 = "world"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "YES"
        
    def testeCaso2(self):
        
        string1 = "hi"
        string2 = "world"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "NO"
        
    def testeCaso3(self):
        
        string1 = "wouldyoulikefries"
        string2 = "abcabcabcabcabcabc"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "NO"
        
        
    def testeCaso4(self):
        
        string1 = "hackerrankcommunity"
        string2 = "cdecdecdecde"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "YES"
        
    def testeCaso5(self):
        
        string1 = "jackandjill"
        string2 = "wentupthehill"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "YES"
        
    def testeCaso6(self):
        
        string1 = "writetoyourparents"
        string2 = "fghmqzldbc"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "NO"
        
    def testeCaso7(self):
        
        string1 = "aardvark"
        string2 = "apple"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "YES"
        
    def testeCaso8(self):
        
        string1 = "beetroot"
        string2 = "sandals"
        
        resposta = twoStrings(string1, string2)
        
        assert resposta == "NO"
    
    