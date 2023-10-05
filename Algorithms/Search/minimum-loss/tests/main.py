from minimumLoss import minimumLoss

if __name == '__main__':
    
    n = int(input().strip())
    
    preco = list(map(int, input().strip().split()))
    
    resultado = minimumLoss(preco)
    
    print(str(resultado + '\n'))