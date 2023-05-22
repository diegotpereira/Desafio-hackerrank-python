from beautifulBinaryString import beautifulBinaryString

def testeCaso1():
    
    b = '0101010'
    esperado = 2
    resultado = beautifulBinaryString(b)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    b = '01100'
    esperado = 0
    resultado = beautifulBinaryString(b)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    b = '0100101010'
    esperado = 3
    resultado = beautifulBinaryString(b)
    
    assert resultado == esperado