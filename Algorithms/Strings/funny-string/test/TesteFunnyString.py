from funnyString import funnyString

def testeCaso1():
    
    # A diferença entre 'a' e 'c' é |'a' - 'c'| = 2.
    # A diferença entre 'c' e 'x' é |'c' - 'x'| = 21.
    # A diferença entre 'x' e 'z' é |'x' - 'z'| = 2.
    
    # A diferença entre 'z' e 'x' é |'z' - 'x'| = 2.
    # A diferença entre 'x' e 'c' é |'x' - 'c'| = 21.
    # A diferença entre 'c' e 'a' é |'c' - 'a'| = 2.
    
    s = "acxz"
    esperado = "Funny"
    resultado = funnyString(s)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    s = "bcxz"
    esperado = "Not Funny"
    resultado = funnyString(s)
    
    assert resultado == esperado
    
    
def testeCaso3():
    
    s = "ivvkxq"
    esperado = "Not Funny"
    resultado = funnyString(s)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    s = "ivvkx"
    esperado = "Not Funny"
    resultado = funnyString(s)
    
    assert resultado == esperado
    
    
def testeCaso5():
    
    s = "ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq"
    esperado = "Funny"
    resultado = funnyString(s)
    
    assert resultado == esperado