from quickSort import quickSort

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = quickSort(arr)
    
    print(' '.join(map(str, resultado)))
    print('\n')