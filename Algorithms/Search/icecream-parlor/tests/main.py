from icecreamParlor import icecreamParlor

if __name__ == '__main__':
    
    idas_sorveteria = int(input().strip())
    
    for iItr in range(idas_sorveteria):
        
        saldo = int(input().strip())
        tipos_sorvete = int(input().strip())
        
        arr = list(map(int, input().rstrip().split()))
        
        resultado = icecreamParlor(saldo, arr)
        
        print(' '.join(map(str, resultado)))
        print('\n')