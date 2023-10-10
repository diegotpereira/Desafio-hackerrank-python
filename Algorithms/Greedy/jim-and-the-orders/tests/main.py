from jimOrders import jimOrders

if __name__ == '__main_':
    
    entrada = int(input().strip())
    
    pedidos = []
    
    for _ in range(entrada):
        
        pedidos.append(list(map(int, input().rstrip().split())))
        
        resultado = jimOrders(pedidos)
        
        print(' '.join(map(str, resultado)))
        print('\n')
    
    