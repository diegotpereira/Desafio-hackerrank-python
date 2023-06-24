from alternatingCharacters import alternatingCharacters

def testeCaso1():
    
    s = 'AAAA'
    esperado = 3
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
def testeCaso2():
    
    s = 'BBBBB'
    esperado = 4
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
    
    
def testeCaso3():
    
    s = 'ABABABAB'
    esperado = 0
    resultado = alternatingCharacters(s)
    
    
    
def testeCaso4():
    
    s = 'BABABA'
    esperado = 0
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
    
def testeCaso5():
    
    s = 'AAABBB'
    esperado = 4
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
    
def testeCaso6():
    
    s = 'AAABBBAABB'
    esperado = 6
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
    
def testeCaso7():
    
    s = 'AABBAABB'
    esperado = 4
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
    
def testeCaso8():
    
    s = 'ABABABAA'
    esperado = 1
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado
    
    
    
def testeCaso9():
    
    s = 'ABBABBAA'
    esperado = 3
    resultado = alternatingCharacters(s)
    
    assert resultado == esperado