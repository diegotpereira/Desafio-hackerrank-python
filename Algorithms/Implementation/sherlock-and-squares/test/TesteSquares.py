from squares import squares

def testeCaso1():
    a = 3
    b = 9
    esperado = 2
    
    resultado = squares(a, b)
    
    assert resultado == esperado
    
    
def testeCaso2():
    a = 17
    b = 24
    esperado = 0
    
    resultado = squares(a, b)
    
    assert resultado == esperado
    
def testeCaso3():
    a = 35
    b = 70
    esperado = 3
    
    resultado = squares(a, b)
    
    assert resultado == esperado
    
    
def testeCaso4():
    a = 100
    b = 1000
    esperado = 22
    
    resultado = squares(a, b)
    
    assert resultado == esperado