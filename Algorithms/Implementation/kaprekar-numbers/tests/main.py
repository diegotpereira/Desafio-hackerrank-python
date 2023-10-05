from kaprekarNumbers import kaprekarNumbers

if __name__ == '__main__':
    
    limite_superior = int(input().strip())
    limite_inferior = int(input().strip())
    
    resultado = kaprekarNumbers(limite_superior, limite_inferior)
    
    print(resultado)