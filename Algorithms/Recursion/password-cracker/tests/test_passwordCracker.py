from passwordCracker import passwordCracker

class TestePasswordCracker:
    
    def testeCaso1(self):
        
        passwords = ['because', 'can', 'do', 'must', 'we', 'what']
        loginAttempt = 'wedowhatwemustbecausewecan'
        
        esperado = 'we do what we must because we can'
        
        resultado = passwordCracker(passwords, loginAttempt)
        
        assert resultado == esperado
        
        
    def testeCaso2(self):
        
        passwords = ['hello', 'planet']
        loginAttempt = 'helloworld'
        
        esperado = 'WRONG PASSWORD'
        
        resultado = passwordCracker(passwords, loginAttempt)
        
        assert resultado == esperado
        
        
    def testeCaso3(self):
        
        passwords = ['ab', 'abcd', 'cd']
        loginAttempt = 'abcd'
        
        esperado = 'abcd'
        
        resultado = passwordCracker(passwords, loginAttempt)
        
        assert resultado == esperado
        
    def testeCaso4(self):
        
        passwords = ['ozkxyhkcst', 'xvglh', 'hpdnb', 'zfzahm']
        loginAttempt = 'zfzahm'
        
        esperado = 'zfzahm'
        
        resultado = passwordCracker(passwords, loginAttempt)
        
        assert resultado == esperado