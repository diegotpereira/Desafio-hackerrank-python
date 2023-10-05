from makingAnagrams import makingAnagrams

class TesteMakingAnagrams:
    
    # def testeCaso1(self):
        
    #     string1 = "cde"
    #     string2 = "abs"
        
    #     resultado = makingAnagrams(string1, string2)
        
    #     assert resultado == 4
        
    def testeCaso2(self):
        
        string1 = "absdjkvuahdakejfnfauhdsaavasdlkj"
        string2 = "djfladfhiawasdkjvalskufhafablsdkashlahdfa"
        
        resultado = makingAnagrams(string1, string2)
        
        assert resultado == 19
        
        
    def testeCaso3(self):
        
        string1 = "fcrxzwscanmligyxyvym"
        string2 = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
        
        resultado = makingAnagrams(string1, string2)
        
        assert resultado == 30
        
        
    def testeCaso4(self):
        
        string1 = "bugexikjevtubidpulaelsbcqlupwetzyzdvjphn"
        string2 = "lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk"
        
        resultado = makingAnagrams(string1, string2)
        
        assert resultado == 40
            
    def testeCaso5(self):
        
        string1 = "fsqoiaidfaukvngpsugszsnseskicpejjvytviya"
        string2 = "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget"
        
        resultado = makingAnagrams(string1, string2)
        
        assert resultado == 42
        
    def testeCaso6(self):
        
        string1 = "imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesfxkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln"
        string2 = "wfnfdassvfugqjfuruwrdumdmvxpbjcxorettxmpcivurcolxmeagsdundjronoehtyaskpwumqmpgzmtdmbvsykxhblxspgnpgfzydukvizbhlwmaajuytrhxeepvmcltjmroibjsdkbqjnqjwmhsfopjvehhiuctgthrxqjaclqnyjwxxfpdueorkvaspdnywupvmy"
        
        resultado = makingAnagrams(string1, string2)
        
        assert resultado == 102