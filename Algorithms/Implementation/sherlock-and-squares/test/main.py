from squares import squares

if __name__ == "__main__":
    
    q = int(input().strip())
    
    for qItr in range(q):
        
        primeiraMultiplaEntrada = input().strip().split()
        
        a = int(primeiraMultiplaEntrada[0])
        b = int(primeiraMultiplaEntrada[1])
        
        resultado = squares(a, b)
        
        print(str(resultado) + '\n')