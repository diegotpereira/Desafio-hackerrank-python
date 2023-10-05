from knightlOnAChessboard import knightlOnAChessboard

class TesteKnightlOnAChessboard:
    
    def testeCaso1(self):
        
        n = 5
        resultado = knightlOnAChessboard(n)
        
        assert resultado == [[4, 4, 2, 8], [4, 2, 4, 4], [2, 4, -1, -1], [8, 4, -1, 1]]
        
        
    def testeCaso2(self):
        
        n = 6
        resultado = knightlOnAChessboard(n)
        
        assert resultado == [[5, 4, 3, 2, 5], [4, -1, 2, -1, -1], [3, 2, -1, -1, -1], [2, -1, -1, -1, -1], [5, -1, -1, -1, 1]]