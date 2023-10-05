from getMinimumCost import getMinimumCost

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().split()
    
    n = int(primeira_multipla_entrada[0])
    
    k = int(primeira_multipla_entrada[1])
    
    c = list(map(int, input().rstrip().split()))
    
    resultado = getMinimumCost(k, c)
    
    print(str(resultado) + '\n')