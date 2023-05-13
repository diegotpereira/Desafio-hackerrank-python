from cutTheSticks import cutTheSticks

def testeCaso1():
    
    arr = [5, 4, 4, 2, 2, 8]
    esperada = [6, 4, 2, 1]
    resultado = cutTheSticks(arr)
    
    assert resultado == esperada
    
    
def testeCaso2():
    
    arr = [1, 2, 3, 4, 3, 3, 2, 1]
    esperada = [8, 6, 4, 1]
    resultado = cutTheSticks(arr)
    
    assert resultado == esperada
    
    
def testeCaso3():
    
    arr = [1, 13, 3, 8, 14, 9, 4, 4]
    esperada = [8, 7, 6, 4, 3, 2, 1]
    resultado = cutTheSticks(arr)
    
    assert resultado == esperada