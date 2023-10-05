from gridChallenge import gridChallenge

class TesteGridChallenge:
    
    def testeCaso1(self):
        
        grade = ['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']
        
        resultado = gridChallenge(grade)
        
        assert resultado == 'YES'
        
    def testeCaso2(self):
        
        grade = ['abc', 'lmp', 'qrt']
        
        resultado = gridChallenge(grade)
        
        assert resultado == 'YES'
        
    def testeCaso3(self):
        
        grade = ['mpxz', 'abcd', 'wlmf']
        
        resultado = gridChallenge(grade)
        
        assert resultado == 'NO'
        
    def testeCaso4(self):
        
        grade = ['abc', 'hjk', 'mpq', 'rtv']
        
        resultado = gridChallenge(grade)
        
        assert resultado == 'YES'