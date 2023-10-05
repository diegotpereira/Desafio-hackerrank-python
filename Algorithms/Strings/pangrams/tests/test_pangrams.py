from pangrams import pangrams

class TestePangrams:
    
    def testeCaso1(self):
        
        string = 'We promptly judged antique ivory buckles for the next prize'
        
        resultado = pangrams(string)
        
        assert resultado == 'pangram'
        
    def testeCaso2(self):
        
        string = 'We promptly judged antique ivory buckles for the prize'
        
        resultado = pangrams(string)
        
        assert resultado == 'not pangram'
        
    def testeCaso3(self):
        
        string = 'a'
        
        resultado = pangrams(string)
        
        assert resultado == 'not pangram'
        
    def testeCaso4(self):
        
        string = 'qmExzBIJmdELxyOFWv LOCmefk TwPhargKSPEqSxzveiun'
        
        resultado = pangrams(string)
        
        assert resultado == 'pangram'