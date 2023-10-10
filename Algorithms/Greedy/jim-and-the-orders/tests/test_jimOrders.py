from jimOrders import jimOrders

class TesteJimOrders:
    
    def testeCaso1(self):
        
        pedidos = [
            [1, 3],
            [2, 3],
            [3, 3]
        ]
        
        esperado = [1, 2, 3]
        
        resultado = jimOrders(pedidos)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        pedidos = [
            [8, 1],
            [4, 2],
            [5, 6],
            [3, 1],
            [4, 3]
        ]
        
        esperado = [4, 2, 5, 1, 3]
        
        resultado = jimOrders(pedidos)
        
        assert resultado == esperado
        
    def testeCaso3(self):
        
        pedidos = [
            [1, 1],
            [1, 1]
        ]
        
        esperado = [1, 2]
        
        resultado = jimOrders(pedidos)
        
        assert resultado == esperado
        
        
    def testeCaso4(self):
        
        pedidos = [
            [1, 1]
        ]
        
        esperado = [1]
        
        resultado = jimOrders(pedidos)
        
        assert resultado == esperado
