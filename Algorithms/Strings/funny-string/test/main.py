from funnyString import funnyString

if __name__ == '__main__':
    
    q = int(input().strip())
    
    for qItr in range(q):
        
        s = input()
        
        resultado = funnyString(s)
        
        print(resultado + '\n')