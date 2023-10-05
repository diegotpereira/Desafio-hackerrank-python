from minimumNumber import minimumNumber

if __name__ == '__main__':
    
    n = int(input().strip())
    
    senha = input()
    
    resposta = minimumNumber(n, senha)
    
    print(str(resposta) + '\n')