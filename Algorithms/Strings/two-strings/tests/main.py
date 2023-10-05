from twoStrings import twoStrings

if __name__ == '__main__':
    
    consultas = int(input())
    
    for qItr in range(consultas):
        
        string1 = input() 
        string2 = input()
        
        resultado = twoStrings(string1, string2)
        
        print(resultado + '\n')