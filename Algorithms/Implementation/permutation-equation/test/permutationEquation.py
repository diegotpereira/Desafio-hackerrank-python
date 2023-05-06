

def permutationEquation(p):
    
    cnt = 1
    array = []
    
    while cnt <= len(p):
        
        i = p.index(cnt) + 1
        j = p.index(i) + 1
        
        array.append(j)
        
        cnt += 1
    
    return array

if __name__ == '__main__':
    
    n = int(input().strip())
    
    p = list(map(int, (input().rstrip().split())))
    
    resultado = permutationEquation(p)
    
    print('\n'.join(map(str, resultado)))
    print('\n')