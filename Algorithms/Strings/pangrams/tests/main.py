from pangrams import pangrams

if __name__ == '__main__':
    
    string = input()
    
    resultado = pangrams(string)
    
    print(resultado + '\n')