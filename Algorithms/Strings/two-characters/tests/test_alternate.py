from alternate import alternate

class TesteAlternate:
    
    def teste_caso1(self):
        
        s = "beabeefeab"
        
        resultado = alternate(s)
        
        assert resultado == 5
        
        
    def teste_caso2(self):
        
        s = "asdcbsdcagfsdbgdfanfghbsfdab"
        
        resultado = alternate(s)
        
        assert resultado == 8
        
    def teste_caso3(self):
        
        s = "asvkugfiugsalddlasguifgukvsa"
        
        resultado = alternate(s)
        
        assert resultado == 0