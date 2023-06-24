from resultado import beautifulPairs

import pytest

class TestbeautifulPairs:
    
    def teste_Caso1(self):
        
        A = [1, 2, 3, 4]
        B = [1, 2, 3, 3]
        assert beautifulPairs(A, B) == 4
        
    def teste_caso2(self):
        
        A = [3, 5, 7, 11, 5, 8]
        B = [5, 7, 11, 10, 5, 8]
        
        assert beautifulPairs(A, B) == 6