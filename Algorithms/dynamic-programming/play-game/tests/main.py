from bricksGame import bricksGame

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for _ in range(entrada) :
        
        arr_contar = int(input().strip())
        
        arr = list(map(int, input().rstrip().split()))
        
        resultado = bricksGame(arr)
        
        print(str(resultado) + '\n')