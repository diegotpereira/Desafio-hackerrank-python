from initialize import initialize

maximum = 26
arr = {}
def answerQuery(l, r):
    
    global arr
    global fac, mod, M
    impar = 0
    par = 0
    divs = 1
    
    for i in range(maximum):
        
        valor = arr[i][r] - arr[i][l -1]
        impar += (valor & 1)
        par += (valor // 2)
        divs = (divs * mod[valor // 2]) % M 
        
    resultado = (fac[par] * divs) % M 
    
    if (impar > 0):
        
        resultado = (resultado * impar) % M 
        
    return resultado