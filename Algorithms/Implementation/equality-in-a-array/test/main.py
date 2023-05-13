from equalizeArray import equalizeArray

if __name__ == "__main__":
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    resultado = equalizeArray(arr)
    
    print(str(resultado) + '\n')