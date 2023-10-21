from gridlandMetro import gridlandMetro

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    m = int(primeira_multipla_entrada[1])
    k = int(int(primeira_multipla_entrada[2]))
    
    pista = []
    
    for _ in range(k):
        
        pista.append(list(map(int, input().rstrip().split())))
        
    resultado = gridlandMetro(n, m, k, pista)
    
    print(str(resultado) + '\n')