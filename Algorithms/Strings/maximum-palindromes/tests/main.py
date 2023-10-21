from initialize import initialize
from answerQuery import answerQuery

if __name__ == '__main__':
    
    s = input()
    
    initialize(s)
    
    q = int(input().strip())
    
    for q_itr in range(q):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        l = int(primeira_multipla_entrada[0])
        r = int(primeira_multipla_entrada[1])
        
        resultado = answerQuery(l, r)
        
        print(str(resultado) + '\n')
    
    
   