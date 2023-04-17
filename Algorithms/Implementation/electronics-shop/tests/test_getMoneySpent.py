from getMoneySpent import getMoneySpent

class TesteGetMoneySpent:
    
    def test_caso1(self):
        
        teclados = [3, 1]
        dispositivos = [5, 2, 8]
        orcamento = 10
        
        assert getMoneySpent(teclados, dispositivos, orcamento) == 9
        
    def test_caso2(self):
        
        teclados = [5]
        dispositivos = [4]
        orcamento = 5
        
        assert getMoneySpent(teclados, dispositivos, orcamento) == -1
        