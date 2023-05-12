from findDigits import findDigits

def test_caso1():
    
    n = 12
    esperado = 2
    
    resultado = findDigits(n)
    
    assert  resultado == esperado
    
    
def test_caso2():
    
    n = 1012
    esperado = 3
    
    resultado = findDigits(n)
    
    assert  resultado == esperado
    
    
def test_caso3():
    
    n = 123456789
    esperado = 3
    
    resultado = findDigits(n)
    
    assert  resultado == esperado