from happyLadybugs import happyLadybugs

class TesteHappyLadybugs:
    
    def testeCaso1(delf):
        
        b = 'RBY_YBR'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'YES'
        
    def testeCaso2(delf):
        
        b = 'X_Y__X'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'NO'
        
    def testeCaso3(delf):
        
        b = '__'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'YES'
        
    def testeCaso4(delf):
        
        b = 'B_RRBR'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'YES'
        
    def testeCaso5(delf):
        
        b = 'AABBC'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'NO'
        
    def testeCaso6(delf):
        
        b = 'AABBC_C'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'YES'
        
    def testeCaso7(delf):
        
        b = '_'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'YES'
        
    def testeCaso8(delf):
        
        b = 'DD__FQ_QQF'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'YES'
        
    def testeCaso9(delf):
        
        b = 'AABCBC'
        
        resposta = happyLadybugs(b)
        
        assert resposta == 'NO'