from sherlockAndAnagrams import sherlockAndAnagrams

if __name__ == '__main__':
    
    entrada = int(input().strip())
    
    for entrada_itr in range(entrada):
        
        s = input()
        
        resultado = sherlockAndAnagrams(s)
        
        print(str(resultado) + '\n')
    