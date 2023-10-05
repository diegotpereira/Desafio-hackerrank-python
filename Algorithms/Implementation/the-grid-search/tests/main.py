from gridSearch import gridSearch

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for itr in range(entrada):
        primeira_multipla_entrada = input().rstrip().split()
        
        R = int(primeira_multipla_entrada[0])
        C = int(primeira_multipla_entrada[1])
        G = []
        
        for _ in range(R):
            
            G_item = input()
            G.append(G_item)
            
            
        segunda_multipla_entrada = input().rstrip().split()
        
        r = int(segunda_multipla_entrada[0])
        c = int(segunda_multipla_entrada[1])
        P = []
        
        for _ in range(r):
            
            P_item = input()
            P.append(P_item)
            
        resultado = gridSearch(G, P)
        
        print(resultado + '\n')