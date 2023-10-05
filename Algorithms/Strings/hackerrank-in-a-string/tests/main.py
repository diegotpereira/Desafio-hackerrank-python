from hackerrankInString import hackerrankInString

if __name__ == '__main__':
    
    consultas = int(input().strip())
    
    for qItr in range(consultas):
        
        string = input()
        
        resultado = hackerrankInString(string)
        
        print(resultado + '\n')