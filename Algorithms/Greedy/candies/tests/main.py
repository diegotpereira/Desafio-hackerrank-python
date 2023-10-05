from candies import candies

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    arr = []
    
    for _ in range(entrada):
        
        arr_item = int(input().strip())
        arr.append(arr_item)
        
    resultado = candies(n, arr)
    
    print(str(resultado) + '\n')