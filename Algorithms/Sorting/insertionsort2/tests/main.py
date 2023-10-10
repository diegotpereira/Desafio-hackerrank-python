from insertionSort2 import insertionSort2

if __name__== '__main__':
    
    entrada = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = insertionSort2(entrada, arr)
    
    print(resultado)
    
    
    