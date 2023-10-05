from fairRations import fairRations

if __name__ == '__main__':
    
    N = int(input().strip())
    B = list(map(int, input().split()))
    
    resultado = fairRations(B)
    
    print(resultado + '\n')