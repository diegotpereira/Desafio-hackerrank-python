from substringDiff import substringDiff

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for entrada_itr in range(entrada):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        k = primeira_multipla_entrada[0]
        
        s1 = primeira_multipla_entrada[1]
        
        s2 = primeira_multipla_entrada[2]
        
        resultado = substringDiff(k, s1, s2)
        
        print(str(resultado) + '\n')