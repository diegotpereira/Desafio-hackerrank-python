maximum = 26

def initialize(s):
    
    global arr, fac, mod, M
    M = 1000000007
    n = len(s)
    
    arr = [[0 for _ in range(n + 1)] for _ in range(maximum)]
    
    for i in range(n):
        
        for j in range(maximum):
            
            arr[j][i + 1] = arr[j][i] + ((ord(s[i]) - 97) == j)
            
        
    fac = [1] * (n + 1)
    mod = [1] * (n + 1)
    
    for i in range(1, n + 1):
        
        fac[i] = (fac[i - 1] * i) % M 
        mod[i] = pow(fac[i], M - 2, M)
    