from libraryFine import libraryFine

def testeCaso1():
    
    d1 = 6
    m1 = 6
    y1 = 2015
    
    d2 = 9
    m2 = 6 
    y2 = 2016
    
    esperado = 0
    
    resultado = libraryFine(d1, m1, y1, d2, m2, y2)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    d1 = 9
    m1 = 6
    y1 = 2015
    
    d2 = 6
    m2 = 6
    y2 = 2015
    
    esperado = 45
    
    resultado = libraryFine(d1, m1, y1, d2, m2, y2)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    d1 = 30
    m1 = 5
    y1 = 2015
    
    d2 = 2
    m2 = 5
    y2 = 2015
    
    esperado = 420
    
    resultado = libraryFine(d1, m1, y1, d2, m2, y2)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    d1 = 2
    m1 = 5
    y1 = 2015
    
    d2 = 30
    m2 = 5
    y2 = 2015
    
    esperado = 0
    
    resultado = libraryFine(d1, m1, y1, d2, m2, y2)
    
    assert resultado == esperado
    
    
def testeCaso5():
    
    d1 = 2
    m1 = 7
    y1 = 1014
    
    d2 = 1
    m2 = 1
    y2 = 1014
    
    esperado = 3000
    
    resultado = libraryFine(d1, m1, y1, d2, m2, y2)
    
    assert resultado == esperado