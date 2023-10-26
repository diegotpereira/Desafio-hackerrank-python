from powersGame import powersGame

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for entrada_itr in range(entrada):
        
        n = int(input().strip())
        
        resultado = powersGame(n)
        
        print(resultado + '\n')