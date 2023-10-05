from knightlOnAChessboard import knightlOnAChessboard

if __name__ == '__main__':
    
    n = int(input().strip())
    
    resultado = knightlOnAChessboard(n)
    
    print('\n'.join([' '.join(map(str, x)) for x in resultado]))
    print('\n')