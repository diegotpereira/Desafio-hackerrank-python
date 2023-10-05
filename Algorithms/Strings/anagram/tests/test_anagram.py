from anagram import anagram

class TesteAnagram:
    
    def testeCaso1(self):
        
        palavra = "hhpddlnnsjfoyxpciioigvjqzfbpllssuj"
        
        resultado = anagram(palavra)
        
        assert resultado == 10
        
    def testeCaso2(self):
        
        palavra = "xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj"
        
        resultado = anagram(palavra)
        
        assert resultado == 13
        
    def testeCaso3(self):
        
        palavra = "dnqaurlplofnrtmh"
        
        resultado = anagram(palavra)
        
        assert resultado == 5
        
    def testeCaso4(self):
        
        palavra = "aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb"
        
        resultado = anagram(palavra)
        
        assert resultado == 26
        
    def testeCaso5(self):
        
        palavra = "xyyx"
        
        resultado = anagram(palavra)
        
        assert resultado == 0
        
    def testeCaso6(self):
        
        palavra = "xaxbbbxx"
        
        resultado = anagram(palavra)
        
        assert resultado == 1
        
        
    def testeCaso7(self):
        
        palavra = "lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad"
        
        resultado = anagram(palavra)
        
        assert resultado == 15
        
    def testeCaso8(self):
        
        palavra = "drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe"
        
        resultado = anagram(palavra)
        
        assert resultado == -1
        
        
          
    def testeCaso9(self):
        
        palavra = "ubulzt"
        
        resultado = anagram(palavra)
        
        assert resultado == 3
        
    def testeCaso10(self):
        
        palavra = "vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy"
        
        resultado = anagram(palavra)
        
        assert resultado == 13
        
    def testeCaso11(self):
        
        palavra = "xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa"
        
        resultado = anagram(palavra)
        
        assert resultado == 13
        
    def testeCaso12(self):
        
        palavra = "gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv"
        
        resultado = anagram(palavra)
        
        assert resultado == -1