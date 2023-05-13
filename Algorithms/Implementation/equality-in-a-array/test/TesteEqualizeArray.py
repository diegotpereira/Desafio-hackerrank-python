from equalizeArray import equalizeArray

def testeCaso1():
    
    arr = [3, 3, 2, 1, 3]
    esperado = 2
    resultado = equalizeArray(arr)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    arr = [1, 2, 3, 1, 2, 3, 3, 3]
    esperado = 4
    resultado = equalizeArray(arr)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    arr = [24, 29, 70, 43, 12, 27, 29, 24, 41, 12, 41, 43, 24, 70, 24, 100, 41, 43, 43, 100, 29, 70, 100, 43, 41, 27, 70, 70, 59, 41, 24, 24, 29, 43, 24, 27, 70, 24, 27, 70, 24, 70, 27, 24, 43, 27, 100, 41, 12, 70, 43, 70, 62, 12, 59, 29, 62, 41, 100, 43, 43, 59, 59, 70, 12, 27, 43, 43, 27, 27, 27, 24, 43, 43, 62, 43, 70, 29]
    esperado = 63
    resultado = equalizeArray(arr)
    
    assert resultado == esperado