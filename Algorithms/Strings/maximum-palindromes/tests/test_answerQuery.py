# from answerQuery import answerQuery
# from initialize import initialize
from main import initialize
from main import answerQuery
import pytest

class TesteAnswerQuery:
    
#     def setUp(self):
#         # Initialize the required data
#         s = "week"  # Replace with your input string
#         initialize(s)
    
    def testeCaso1(self):
        
        # s = 'week'
        l = 1
        r = 4
        
        esperado = 2
        
        resultado = answerQuery(l, r)
        
        assert resultado == esperado
        
    # Execute os testes com o pytest
    if __name__ == '__main__':
        pytest.main()