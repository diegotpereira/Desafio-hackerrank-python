from stones import stones

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for entrada_itr in range(entrada):
        
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        
        resultado = stones(n, a, b)
        
        print(''.join(map(str, resultado)))
        print('\n')