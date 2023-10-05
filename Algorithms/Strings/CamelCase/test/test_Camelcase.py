from resultado import camelcase

class TesteCamelCase:
    
    def test_contagem_palavras(self):
        
        s = "saveChangesInTheEditor"
        
        resultado = camelcase(s)
        
        assert resultado == 5
        
        
    def test_contagem_palavras1(self):
        
        s = "singleword"
        
        resultado = camelcase(s)
        
        assert resultado == 1
        
    def test_contagem_palavras2(self):
        
        s = "abc"
        
        resultado = camelcase(s)
        
        assert resultado == 1
        
        
    def test_contagem_palavras3(self):
        
        s = "palavraCertaTeste"
        
        resultado = camelcase(s)
        
        assert resultado == 3
        
        
    def test_contagem_palavras4(self):
        
        s = "palavraCertaTesteAgoraAqui"
        
        resultado = camelcase(s)
        
        assert resultado == 5
        
        
    def test_contagem_palavras5(self):
        
        s = "ab"
        
        resultado = camelcase(s)
        
        assert resultado == 1