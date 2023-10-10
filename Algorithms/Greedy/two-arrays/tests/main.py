from twoArrays import twoArrays

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for i_itr in range(entrada):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        n = int(primeira_multipla_entrada[0])
        k = int(primeira_multipla_entrada[1])
        A = int(primeira_multipla_entrada[2])
        B = int(primeira_multipla_entrada[3])
        
        resultado = twoArrays(k, A, B)
        
        print(resultado + '\n')