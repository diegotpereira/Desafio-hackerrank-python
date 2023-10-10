from lonelyinteger import lonelyinteger

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    resultado = lonelyinteger(arr)
    
    print(str(resultado) + '\n')
    
    