from chessboardGame import chessboardGame

class TesteChessboardGame:
    
    def testeCaso1(self):
        
        x = 5
        y = 2
        
        resultado = chessboardGame(x, y)
        
        assert resultado == 'Second'
        
    def testeCaso2(self):
        
        x = 5
        y = 3
        
        resultado = chessboardGame(x, y)
        
        assert resultado == 'First'
        
    def testeCaso3(self):
        
        x = 8
        y = 8
        
        resultado = chessboardGame(x, y)
        
        assert resultado == 'First'
        
    def testeCaso4(self):
        
        x = 7
        y = 3
        
        resultado = chessboardGame(x, y)
        
        assert resultado == 'First'
        
    def testeCaso5(self):
        
        x = 8
        y = 12
        
        resultado = chessboardGame(x, y)
        
        assert resultado == 'First'
        
    def testeCaso6(self):
        
        x = 9
        y = 7
        
        resultado = chessboardGame(x, y)
        
        assert resultado == 'First'