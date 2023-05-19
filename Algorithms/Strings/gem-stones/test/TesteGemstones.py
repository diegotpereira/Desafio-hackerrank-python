from gemstones import gemstones

def testeCaso1():
    
    arr = ['abcdde', 'baccd', 'eeabg']
    esperado = 2
    resultado = gemstones(arr)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    arr = ['basdfj', 'asdlkjfdjsa', 'bnafvfnsd', 'oafhdlasd']
    esperado = 4
    resultado = gemstones(arr)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    arr = ['vtrjvgbj', 'mkmjyaeav', 'sibzdmsk']
    esperado = 0
    resultado = gemstones(arr)
    
    assert resultado == esperado