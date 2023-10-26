from verticalRooks import verticalRooks

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for _ in range(entrada):
        
        n = int(input().strip())
        
        r1 = []
        
        for _ in range(n):
            
            r1_item = int(input().strip())
            
            r1.append(r1_item)
            
        r2 = []
        
        for _ in range(n):
            
            r2_item = int(input().strip())
            r2.append(r2_item)
            
            
        resultado = verticalRooks(r1, r2)
        
        print(resultado + '\n')