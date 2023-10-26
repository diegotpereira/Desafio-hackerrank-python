from bobAndBen import bobAndBen

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for g_itr in range(entrada):
        
        n = int(input().strip())
        
        arvores = []
        
        for _ in range(n):
            
            arvores.append(list(map(int, input().rstrip().split())))
            
        resultado = bobAndBen(arvores)
        
        print(resultado + '\n')