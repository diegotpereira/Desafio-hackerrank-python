from nonDivisibleSubset import nonDivisibleSubset

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    n = int(primeira_multipla_entrada[0])
    divisor = int(primeira_multipla_entrada[1])
    matriz = list(map(int, input().rstrip().split()))
    
    resultado = nonDivisibleSubset(divisor, matriz)
    
    print(str(resultado) + '\n')