from howManyGames import howManyGames

def testeCaso1():
    
    preco_primeiro_jogo = 20
    desconto_jogo_anterior = 3 
    custo_minimo_jogo = 6
    orcamento_inicial = 80
    esperado = 6
    resultado = howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial)
    
    assert resultado == esperado
    
    
def testeCaso2():
    
    preco_primeiro_jogo = 20
    desconto_jogo_anterior = 3 
    custo_minimo_jogo = 6
    orcamento_inicial = 85
    esperado = 7
    resultado = howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial)
    
    assert resultado == esperado
    
def testeCaso3():
    
    preco_primeiro_jogo = 16
    desconto_jogo_anterior = 2
    custo_minimo_jogo = 1
    orcamento_inicial = 9981
    esperado = 9917
    resultado = howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial)
    
    assert resultado == esperado
    
    
def testeCaso4():
    
    preco_primeiro_jogo = 100
    desconto_jogo_anterior = 1
    custo_minimo_jogo = 1
    orcamento_inicial = 99
    esperado = 0
    resultado = howManyGames(preco_primeiro_jogo, desconto_jogo_anterior, custo_minimo_jogo, orcamento_inicial)
    
    assert resultado == esperado