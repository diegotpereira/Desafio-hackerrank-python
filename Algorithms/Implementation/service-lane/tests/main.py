from serviceLane import serviceLane

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    t = int(primeira_multipla_entrada[1])
    
    width = list(map(int, input().rstrip().split()))
    
    casos = []
    
    for _ in range(t):
        
        casos.append(list(map(int, input().rstrip().split())))
        
    resultado = serviceLane(n, casos)
    
    print('\n'.join(map(str, resultado)))
    print('\n')