from cutTheSticks import cutTheSticks

if __name__ == "__main__":
    
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    resultado = cutTheSticks(arr)
    
    print('\n'.join(map(str, resultado)))
    print('\n')