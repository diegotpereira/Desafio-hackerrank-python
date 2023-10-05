from missingNumbers import missingNumbers

if __name__ == '__main__':
    
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().split())
    brr = list(map(int, input().rstrip().split()))
    
    resultado = missingNumbers(arr, brr)
    
    print(' '.join(map(str, resultado)))
    print('\n')