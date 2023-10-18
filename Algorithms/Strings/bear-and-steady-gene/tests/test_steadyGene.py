from steadyGene import steadyGene

class TesteSteadyGene:
    
    def testeCaso1(self):
        
        gene = 'GAAATAAA'
        
        esperado = 5
        
        resultado = steadyGene(gene)
        
        assert resultado == esperado
        
    def testeCaso2(self):
        
        gene = 'TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'
        
        esperado = 5
        
        resultado = steadyGene(gene)
        
        assert resultado == esperado