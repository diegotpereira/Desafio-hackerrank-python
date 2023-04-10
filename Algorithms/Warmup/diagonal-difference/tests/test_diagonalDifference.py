
from diagonalDifference import diagonalDifference
class TestDiagonalDifference:
    
    def test_diagonal_difference(self):
        
        arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        assert diagonalDifference(arr) == 0
        
        
        # arr = [[1, 2], [3, 4]]
        # assert diagonalDifference(arr) == 2

        arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        assert diagonalDifference(arr) == 15
        