from repeatedString import repeatedString

def testeCaso1():
    
    s = "aba"
    n = 10
    esperado = 7
    
    resultado = repeatedString(s, n)
    
    assert resultado == esperado
    
def testeCaso2():
    
    s = "a"
    n = 1000000000000
    esperado = 1000000000000
    
    resultado = repeatedString(s, n)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    s = "aab"
    n = 882787
    esperado = 588525
    
    resultado = repeatedString(s, n)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    s = "ceebbcb"
    n = 817723
    esperado = 0
    
    resultado = repeatedString(s, n)
    
    assert resultado == esperado
    
    
def testeCaso5():
    
    s = "gfcaaaecbg"
    n = 547602
    esperado = 164280
    
    resultado = repeatedString(s, n)
    
    assert resultado == esperado
    
    
def testeCaso6():
    
    s = "x"
    n = 970770
    esperado = 0
    
    resultado = repeatedString(s, n)