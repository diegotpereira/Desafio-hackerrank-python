from minimumAbsoluteDifference import minimumAbsoluteDifference

if __name__ == "__main__":
    
    n = int(input().strip())
    
    arr = list(map(int, input().strip().split()))
    
    resultado = minimumAbsoluteDifference(arr)
    
    print(str(resultado) + '\n')