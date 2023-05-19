from minimumAbsoluteDifference import minimumAbsoluteDifference

def testeCaso1():
    
    arr = [3, -7, 0]
    esperado = 3
    
    resultado = minimumAbsoluteDifference(arr)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    esperado = 1
    
    resultado = minimumAbsoluteDifference(arr)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    arr = [1, -3, 71, 68, 17]
    esperado = 3
    
    resultado = minimumAbsoluteDifference(arr)
    
    assert resultado == esperado