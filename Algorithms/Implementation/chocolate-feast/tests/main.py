from chocolateFeast import chocolateFeast

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for iTr in range(entrada):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        n = int(primeira_multipla_entrada[0])
        c = int(primeira_multipla_entrada[1])
        m = int(primeira_multipla_entrada[2])
        
        resultado = chocolateFeast(n, c, m)
        
        print(str(resultado) + '\n')
        