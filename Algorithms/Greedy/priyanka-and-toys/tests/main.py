from toys import toys

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    w = list(map(int, input().rstrip().split()))
    
    resultado = toys(w)
    
    print(str(resultado) + '\n')