from misereNim import misereNim

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for i_tr in range(entrada):
        
        n = int(input().strip())
        
        s = list(map(int, input().rstrip().split()))
        
        resultado = misereNim(s)
        
        print(resultado + '\n')