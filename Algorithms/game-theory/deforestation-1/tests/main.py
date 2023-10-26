from deforestation import deforestation

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for itr in range(entrada):
        
        n = int(input().strip())
        
        arvore = []
        
        for  _ in range(n - 1):
            
            arvore.append(list(map(int, input().rstrip().split())))
            
        resultado = deforestation-1(n, arvore)
        
        print(resultado + '\n')