from nimGame import nimGame

if __name__ == '__main__':
    
    entrada = int(input().rstrip())
    
    for g_itr in range(entrada):
        
        n = int(input().strip())
        
        pilha = list(map(int, input().rstrip().split()))
        
        resultado = nimGame(pilha)
        
        print(resultado + '\n')
        