from alternatingCharacters import alternatingCharacters

if __name__ == '__main__':
    
    q = int(input().strip())
    
    for q_itr in range(q):
        
        s = input()
        
        resultado = alternatingCharacters(s)
        
        print(str(resultado) + '\n')