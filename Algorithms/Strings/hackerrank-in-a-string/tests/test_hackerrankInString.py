from hackerrankInString import hackerrankInString

class TesteHackerrankInString:
    
    def testeCaso1(self):
        
        string = "hackerworld"
        
        resultado = hackerrankInString(string)
        
        assert resultado == "NO"
        
        
    def testeCaso2(self):
        
        string = "hereiamstackerrank"
        
        resultado = hackerrankInString(string)
        
        assert resultado == "YES"
        
        
    def testeCaso3(self):
        
        string = "hhaacckkekraraannk"
        
        resultado = hackerrankInString(string)
        
        assert resultado == "YES"
        
        
    def testeCaso4(self):
        
        string = "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
        
        resultado = hackerrankInString(string)
        
        assert resultado == "NO"