from chessboardGame import chessboardGame

if __name__ == '__main__':
    
    t = int(input().strip())
    
    for t_itr in range(t):
        
        primeira_multipla_entrada = input().rstrip().split()
        
        x = int(primeira_multipla_entrada[0])
        
        y = int(primeira_multipla_entrada[1])
        
        resultado = chessboardGame(x, y)
        
        print(resultado + '\n')