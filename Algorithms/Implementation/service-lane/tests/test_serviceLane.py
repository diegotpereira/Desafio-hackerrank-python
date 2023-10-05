from serviceLane import serviceLane

class TesteServiceLane:
    
    def testeCaso1(self):
        
        n = 8 
        # casos = 8
        casos = [2, 3, 1, 2, 3, 2, 3, 3]
        
        resultado = serviceLane(n, casos)
        
        assert resultado == 1