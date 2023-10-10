from closestNumbers import closestNumbers

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = closestNumbers(arr)
    
    print(' '.join(map(str, resultado)))