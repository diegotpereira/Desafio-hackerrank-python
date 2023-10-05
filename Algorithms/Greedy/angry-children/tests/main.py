from maxMin import maxMin

if __name__ == '__main__':
    
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    
    for _ in range(n):
        
        arr_item = int(input().strip())
        
        arr.append(arr_item)
        
        resultado = maxMin(k, arr)
        
        print(str(resultado) + '\n')