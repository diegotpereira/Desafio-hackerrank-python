from separateNumbers import separateNumbers

def testeCaso1():
        
    s = ['1']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    s = ['13']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    s = ['010203']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    s = ['101103']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado
    
    
    
def testeCaso5():
    
    s = ['101103']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado
    
    
    
def testeCaso6():
    
    s = ['101103']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado
    
    
def testeCaso6():
    
    s = ['99910001001']
    esperado = ('NO')
    
    resultado = separateNumbers(s)
    
    assert resultado == esperado