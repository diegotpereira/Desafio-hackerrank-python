from resultado import beautifulPairs

if __name__ == "__main__":
    
    n = int(input().strip())
    
    A = list(map(int, input().rstrip().split()))
    
    B = list(map(int, input().rstrip().split()))
    
    resultado = beautifulPairs(A, B)
    
    print(str(resultado) + '\n')
    
    