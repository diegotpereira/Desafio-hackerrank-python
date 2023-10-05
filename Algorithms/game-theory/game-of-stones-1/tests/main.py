from gameOfStones import gameOfStones

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for i in range(entrada):
        
        n = int(input().strip())
        
        resultado = gameOfStones(n)
        
        print(resultado + '\n')