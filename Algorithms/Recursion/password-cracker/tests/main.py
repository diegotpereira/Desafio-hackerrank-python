from passwordCracker import passwordCracker

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for _ in range(entrada):
        
        n = int(input().strip())
        
        passwords = input().rstrip().split()
        
        loginAttempt = input()
        
        resultado = passwordCracker(passwords, loginAttempt)
        
        print(resultado + '\n')
        
        
        