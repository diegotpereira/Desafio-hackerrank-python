from jumpingOnClouds import jumpingOnClouds

def testeCaso1():
    
    c = [0, 0, 1, 0, 0, 1, 0]
    esperado = 4
    
    resultado = jumpingOnClouds(c)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    c = [0, 0, 0, 1, 0, 0]
    esperado = 3
    
    resultado = jumpingOnClouds(c)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    esperado = 6
    
    resultado = jumpingOnClouds(c)
    
    assert resultado == esperado