from flippingBits import flippingBits

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for qItr in range(entrada):
        
        n = int(input().strip())
        
        resultado = flippingBits(n)
        
        print(str(resultado) + '\n')