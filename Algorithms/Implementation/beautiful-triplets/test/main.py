from beautifulTriplets import beautifulTriplets

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n =int(primeira_multipla_entrada[0])
    
    d = int(primeira_multipla_entrada[1])
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = beautifulTriplets(d, arr)
    
    print(str(resultado) + '\n')