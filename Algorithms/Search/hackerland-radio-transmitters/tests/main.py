from hackerlandRadioTransmitters import hackerlandRadioTransmitters

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    k = int(primeira_multipla_entrada[1])
    x = list(map(int, input().rstrip().split()))
    
    resultado = hackerlandRadioTransmitters(x, k)
    
    print(str(resultado) + '\n')