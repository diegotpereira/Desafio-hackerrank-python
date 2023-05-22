from theLoveLetterMystery import theLoveLetterMystery

def testeCaso1():
    
    s = "abc"
    esperado = 2
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    s = "abcba"
    esperado = 0
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    s = "abcd"
    esperado = 4
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    s = "cba"
    esperado = 2
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
    
def testeCaso5():
    
    s = "lmnop"
    esperado = 6
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
def testeCaso6():
    
    s = "adslkfjas"
    esperado = 36
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
    
def testeCaso7():
    
    s = "bafhaef"
    esperado = 13
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    
    
def testeCaso8():
    
    s = "ofrhase"
    esperado = 40
    resultado = theLoveLetterMystery(s)
    
    assert resultado == esperado
    