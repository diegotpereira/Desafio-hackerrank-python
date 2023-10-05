from towerBreakers import towerBreakers

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for i in range(entrada):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        n = int(primeira_multipla_entrada[0])
        m = int(primeira_multipla_entrada[1])
        
        resultado = towerBreakers(n, m)
        
        print(str(resultado) + '\n')