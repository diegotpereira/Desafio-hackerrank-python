

from marcsCakewalk import marcsCakewalk

class TesteMarcsCakewalk:
    
    def testeCaso1(self):
        
        caloria = [1, 3, 2]
        
        resultado = marcsCakewalk(caloria)
        
        assert resultado == 11
        
    def testeCaso2(self):
        
        caloria = [7, 4, 9, 6]
        
        resultado = marcsCakewalk(caloria)
        
        assert resultado == 79
        
    def testeCaso3(self):
        
        caloria = [504, 378, 291, 380, 728, 630, 797, 212, 32, 792, 895, 635, 850, 853, 859, 127, 653, 655, 476, 748]
        
        resultado = marcsCakewalk(caloria)
        
        assert resultado == 124138217
        
    def testeCaso4(self):
        
        caloria = [353, 726, 36, 574, 234, 746, 507, 244, 382, 349, 107, 279, 608, 87, 459, 793, 710, 73, 758, 945]
        
        resultado = marcsCakewalk(caloria)
        
        assert resultado == 73444139