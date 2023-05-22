from theLoveLetterMystery import theLoveLetterMystery

if __name__ == "__main__":
    
    q = int(input().strip())
    
    for qItr in range(q):
        
        s = input()
        
        resultado = theLoveLetterMystery(s)
        
        print(str(resultado) + '\n')