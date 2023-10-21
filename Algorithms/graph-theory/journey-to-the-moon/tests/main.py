from journeyToMoon import journeyToMoon

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    p = int(primeira_multipla_entrada[1])
    
    astronauta = []
    
    for _ in range(p):
        
        astronauta.append(list(map(int, input().rstrip().split())))
        
    resultado = journeyToMoon(n, astronauta)
    
    print(str(resultado) + '\n')