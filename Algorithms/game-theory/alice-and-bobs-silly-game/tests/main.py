from sillyGame import sillyGame

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for g_itr in range(entrada):
        
        n = int(input().strip())
        
        resultado = sillyGame(n)
        
        print(resultado + '\n')