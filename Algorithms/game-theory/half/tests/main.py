from half import half

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for _ in range(entrada):
        
        n = int(input().strip())
        
        resultado = half(n)
        
        print(str(resultado) + '\n')