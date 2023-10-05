from largestPermutation import largestPermutation

if __name__ == '__main__':
    
    primeira_multipla_entrada = input().rstrip().split()
    
    n = int(primeira_multipla_entrada[0])
    k = int(primeira_multipla_entrada[1])
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = largestPermutation(k, arr)
    
    print(''.join(map(str, resultado)))
    print('\n')