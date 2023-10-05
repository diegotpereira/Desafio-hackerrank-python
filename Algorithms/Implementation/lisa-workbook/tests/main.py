from workbook import workbook

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    k = int(primeira_multipla_entrada[1])
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = workbook(n, k, arr)
    
    print(str(resultado) + '\n')