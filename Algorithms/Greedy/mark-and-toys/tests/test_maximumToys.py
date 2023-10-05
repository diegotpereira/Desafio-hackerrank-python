

from maximumToys import maximumToys

class TesteMaximumToys:
    
    def testeCaso1(self):
        
        precos = [1, 12, 5, 111, 200, 1000, 10]
        k = 50
        
        resultado =  maximumToys(precos, k)
        
        assert resultado == 4
        
    def testeCaso2(self):
        
        precos = [1, 2, 3, 4]
        k = 7
        
        resultado =  maximumToys(precos, k)
        
        assert resultado == 3
        
    def testeCaso3(self):
        
        precos = [3, 7, 2, 9, 4]
        k = 15
        
        resultado =  maximumToys(precos, k)
        
        assert resultado == 3
        
    def testeCaso4(self):
        
        precos = [33324560, 77661073, 31948330, 21522343, 97176507, 5724692, 24699815, 12079402, 6479353, 28430129, 42427721, 57127004, 26256001, 29446837, 65107604, 9809008, 65846182, 8470661, 13597655, 360]
        k = 100000
        
        resultado =  maximumToys(precos, k)
        
        assert resultado == 1
        
        