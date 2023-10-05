from caesarCipher import caesarCipher

if __name__ == '__main__':
    
    comprimento = int(input().strip())
    string = input()
    numeroGiros = int(input().strip())
    
    resultado = caesarCipher(string, numeroGiros)
    
    print(resultado + '\n')