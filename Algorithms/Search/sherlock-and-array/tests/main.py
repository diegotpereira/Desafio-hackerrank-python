from balancedSums import balancedSums

if __name__ == '__main__':
    
    testeCasos = int(input().strip())
    
    for itr in range(testeCasos):
        
        numeroElementosArr = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        
        resultado = balancedSums(arr)
        
        print(resultado + '\n')