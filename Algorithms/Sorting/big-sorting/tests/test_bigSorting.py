from bigSorting import bigSorting

class TesteBigSorting:
    
    def testeCaso1(self):
        
        naoTriados = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']
        
        resultado = bigSorting(naoTriados)
        
        assert resultado == ['1', '3', '3', '5', '10', '31415926535897932384626433832795']
        
    def testeCaso2(self):
        
        naoTriados = ['1', '2', '100', '12303479849857341718340192371', '3084193741082937', '3084193741082938', '111', '200']
        
        resultado = bigSorting(naoTriados)
        
        assert resultado == ['1', '2', '100', '111', '200', '3084193741082937', '3084193741082938', '12303479849857341718340192371']