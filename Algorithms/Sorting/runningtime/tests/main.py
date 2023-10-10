from runningtime import runningtime

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = runningtime(arr)
    
    print(str(resultado) + '\n')