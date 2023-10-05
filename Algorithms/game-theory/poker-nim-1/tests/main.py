from pokerNim import pokerNim

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for i in range(entrada):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        n = int(primeira_multipla_entrada[0])
        k = int(primeira_multipla_entrada[1])
        
        c = list(map(int, input().strip().split()))
        
        resultado = pokerNim(k, c)
        
        print(resultado + '\n')