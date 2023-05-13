from appendAndDelete import appendAndDelete

def testeCaso1():
    
    stringInicial = "hackerhappy"
    stringDesejada = "hackerrank"
    numeroOperacoes = 9
    
    esperado = "Yes"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    stringInicial = "aba"
    stringDesejada = "aba"
    numeroOperacoes = 7
    
    esperado = "Yes"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado
    
def testeCaso3():
    
    stringInicial = "aaaaaaaaaa"
    stringDesejada = "aaaaa"
    numeroOperacoes = 7
    
    esperado = "Yes"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    stringInicial = "zzzzz"
    stringDesejada = "zzzzzzz"
    numeroOperacoes = 4
    
    esperado = "Yes"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado
    
    
def testeCaso5():
    
    stringInicial = "qwerasdf"
    stringDesejada = "qwerbsdf"
    numeroOperacoes = 6
    
    esperado = "No"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado
    
    
def testeCaso6():
    
    stringInicial = "y"
    stringDesejada = "yu"
    numeroOperacoes = 2
    
    esperado = "No"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado
    
    
def testeCaso7():
    
    stringInicial = "qwerty"
    stringDesejada = "zxcvbn"
    numeroOperacoes = 100
    
    esperado = "Yes"
    
    resultado = appendAndDelete(stringInicial, stringDesejada, numeroOperacoes)
    
    assert resultado == esperado