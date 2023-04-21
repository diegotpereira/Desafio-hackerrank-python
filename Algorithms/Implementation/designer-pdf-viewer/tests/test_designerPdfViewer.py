from designerPdfViewer import designerPdfViewer

class TesteDesignerPdfViewer:
    
    def test_caso1(self):
        
        
        altura_letras = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        palavra = "abc"
        
        assert designerPdfViewer(altura_letras, palavra) == 9
        
    def test_caso2(self):
        
        altura_letras = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
        palavra = "zaba"
        
        assert designerPdfViewer(altura_letras, palavra)
        
    def test_caso3(self):
        
        h = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        word = "abcdefghijklmnopqrstuvwxyz"
        assert designerPdfViewer(h, word) == 26