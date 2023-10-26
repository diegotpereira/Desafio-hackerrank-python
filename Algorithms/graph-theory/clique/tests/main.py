from clique import clique

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for entrada_itr in range(entrada):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        n = int(primeira_multipla_entrada[0])
        m = int(primeira_multipla_entrada[1])
        
        resultado = clique(n, m)
        
        print(str(resultado) + '\n')