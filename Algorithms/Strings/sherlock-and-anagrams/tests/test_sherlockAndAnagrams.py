from sherlockAndAnagrams import sherlockAndAnagrams

class TesteSherlockAndAnagrams:
    
    def testeCaso1(self):
        
        s = 'abba'
        esperado = 4
        
        resultado = sherlockAndAnagrams(s)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        s = 'abcd'
        esperado = 0
        
        resultado = sherlockAndAnagrams(s)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        s = 'ifailuhkqq'
        esperado = 3
        
        resultado = sherlockAndAnagrams(s)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        s = 'kkkk'
        esperado = 10
        
        resultado = sherlockAndAnagrams(s)
        
        assert resultado == esperado
        
    def testeCaso5(self):
        
        s = 'cdcd'
        esperado = 5
        
        resultado = sherlockAndAnagrams(s)
        
        assert resultado == esperado