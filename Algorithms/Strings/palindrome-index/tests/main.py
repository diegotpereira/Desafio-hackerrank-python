from palindromeIndex import palindromeIndex

if __name__ == '__main__':
    
    consulta = int(input().strip())
    
    for qItr in range(consulta):
        
        palavra = input()
        
        resultado = palindromeIndex(palavra)
        
        print(str(resultado) + '\n')