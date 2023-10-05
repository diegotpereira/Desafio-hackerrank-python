from permutationEquation import permutationEquation

if __name__ == '__main__':
    
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    
    resultado = permutationEquation(p)
    
    print('\n'.join(map(str, resultado)))
    print('\n')
    

